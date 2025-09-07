<script setup lang="ts">
import { ref } from 'vue'
import SvgIcon from '@jamescoyle/vue-icon'
import {
  mdiContentSaveOutline,
  mdiCloseBoxOutline,
  mdiSquareEditOutline,
  mdiTrashCanOutline,
} from '@mdi/js'
import { Unit } from '@/models/unit'

const emit = defineEmits<{
  (e: 'onSave', unit: Unit): void
  (e: 'onCancel', unit: Unit): void
  (e: 'onDelete', unit: Unit): void
}>()

const model = defineModel<Unit>({ required: true })
const editing = ref(false)

function cancelItem() {
  emit('onCancel', model.value)
  updateEditState()
}

function saveItem() {
  emit('onSave', model.value)
  updateEditState()
}

function deleteItem() {
  emit('onDelete', model.value)
}

function updateEditState() {
  editing.value = !editing.value
}

// Start out editing when a blank (no ID) item has been set
editing.value = model.value.id === ''

// Create DOM-unique names for the fields
const unitNameFieldProp = 'unit-name-' + model.value.id
const unitPluralFieldProp = 'unit-plural-' + model.value.id
</script>
<template>
  <div class="row unit-editor">
    <input
      type="text"
      :name="unitNameFieldProp"
      :disabled="!editing"
      placeholder="Unit name"
      v-model="model.name"
    />
    <input
      type="text"
      :name="unitPluralFieldProp"
      :disabled="!editing"
      placeholder="Plural name"
      v-model="model.plural"
    />
    <button v-if="editing" class="svg-button save-button" @click="saveItem">
      <svg-icon type="mdi" :path="mdiContentSaveOutline" />
    </button>
    <button v-if="editing" class="svg-button cancel-button" @click="cancelItem">
      <svg-icon type="mdi" :path="mdiCloseBoxOutline" />
    </button>
    <button v-if="!editing" class="svg-button edit-button" @click="updateEditState">
      <svg-icon type="mdi" :path="mdiSquareEditOutline" />
    </button>
    <button v-if="!editing" class="svg-button delete-button" @click="deleteItem">
      <svg-icon type="mdi" :path="mdiTrashCanOutline" />
    </button>
  </div>
</template>
<style scoped>
.row {
  margin: 0.25em;
  width: 100%;
}

.unit-editor > * {
  display: inline-block;
  vertical-align: middle;
}

.unit-editor > input {
  margin-right: 0.5em;
  margin-left: 0.5em;
}

.unit-editor > button {
  margin-right: 0.25em;
  margin-left: 0.25em;
  padding: 0px;
  border: 0px;
}

.cancel-button {
  background-color: firebrick;
}

.save-button {
  background-color: darkgreen;
}
</style>
