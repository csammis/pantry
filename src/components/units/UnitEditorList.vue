<script setup lang="ts">
import { ref } from 'vue'
import UnitEditor from './UnitEditor.vue'
import { Unit, createBlankUnit, deleteUnit, getUnit, getUnits, storeUnit } from '@/models/unit'
import ConfirmDialog from '../ConfirmDialog.vue'
import { ConfirmDialogOptions } from '../ConfirmDialog.vue'
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiPlusOutline } from '@mdi/js'

const units = ref<Unit[]>([])
getUnits().then((response) => (units.value = response))

function addNew() {
  // Only push a new one if there isn't already a blank item being filled in
  if (units.value.length > 0 && units.value[units.value.length - 1].id !== '') {
    units.value.push(createBlankUnit())
  }
}

function onSave(unit: Unit) {
  storeUnit(unit).then(function (response) {
    if (response !== undefined && unit.id === '') {
      const i = units.value.indexOf(unit)
      units.value[i].id = response.id
    }
  })
}

function onCancel(unit: Unit) {
  if (unit.id === '') {
    units.value?.pop()
  } else {
    // Reload the item from the backend
    getUnit(unit.id).then(function (response) {
      if (response !== undefined) {
        const i = units.value.indexOf(unit)
        units.value[i] = response
      }
    })
  }
}

const dialogOptions = ref<ConfirmDialogOptions>(new ConfirmDialogOptions())

async function onDialogAccept() {
  dialogOptions.value.visible = false
  const unit = dialogOptions.value.context as Unit
  await deleteUnit(unit).then(function (result) {
    if (result === true) {
      const i = units.value.indexOf(unit)
      units.value.splice(i, 1)
    }
  })
}

function onDialogDismiss() {
  dialogOptions.value.visible = false
}

function onDelete(unit: Unit) {
  dialogOptions.value.context = unit
  dialogOptions.value.title = 'Delete Unit'
  dialogOptions.value.message = 'Are you sure you want to delete "' + unit.name + '"?'
  dialogOptions.value.visible = true
}
</script>
<template>
  <h2>Units</h2>
  <div class="description">
    Items recorded in Pantry can optionally have units associated with them - cups, packages,
    loaves, etc. If an item has a unit associated with it then portions of that item can be consumed
    or moved between locations. If an item doesn't have an associated unit then it is represented as
    a single indivisible "thing" which can't be partially consumed or moved. <br />
    A unit has the following properties:
    <ul>
      <li><em>Name:</em> required and must be unique</li>
      <li>
        <em>Plural:</em> a modification of the name when used in a plural context. For example, if
        the name is "Loaf," the plural would be "loaves."
      </li>
    </ul>
  </div>
  <UnitEditor
    v-for="(unit, index) in units"
    :key="unit.id"
    v-model="units[index]"
    v-on:on-cancel="onCancel"
    v-on:on-delete="onDelete"
    v-on:on-save="onSave"
  />
  <div class="add-row">
    <button class="svg-button create-button" @click="addNew">
      <svg-icon type="mdi" :path="mdiPlusOutline" />
    </button>
    <span>Add new unit</span>
  </div>
  <ConfirmDialog
    :options="dialogOptions"
    v-on:on-accept="onDialogAccept"
    v-on:on-dismiss="onDialogDismiss"
  />
</template>
<style lang="css" scoped>
.description {
  margin-bottom: 2em;
}

.add-row > * {
  margin-left: 0.5em;
  display: inline-block;
  vertical-align: middle;
}
</style>
