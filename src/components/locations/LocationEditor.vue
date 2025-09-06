<script setup lang="ts">
import { ref } from 'vue'
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiContentSaveOutline, mdiCloseBoxOutline, mdiSquareEditOutline } from '@mdi/js'
import { Location } from '@/models/location'

const emit = defineEmits<{
  (e: 'onSave', location: Location): void
  (e: 'onCancel', location: Location): void
}>()

const model = defineModel<Location>({ required: true })
const editing = ref(false)

function cancel() {
  emit('onCancel', model.value)
  updateEditState()
}

function save() {
  emit('onSave', model.value)
  updateEditState()
}

function updateEditState() {
  editing.value = !editing.value
}

// Start out editing when a blank (no ID) item has been set
editing.value = model.value.id === ''

// Create DOM-unique names for the fields
const locationNameFieldProp = 'location-name-' + model.value.id
const locationIconFieldProp = 'location-icon-' + model.value.id
const locationFreezerFieldProp = 'location-freezer-' + model.value.id
</script>
<template>
  <div class="row unit-editor">
    <input
      type="text"
      :name="locationNameFieldProp"
      :disabled="!editing"
      placeholder="Location name"
      v-model="model.name"
    />
    <input
      type="text"
      :name="locationIconFieldProp"
      :disabled="!editing"
      placeholder="Icon (mdi:)"
      v-model="model.icon"
    />
    <span><em>Freezer?</em></span>
    <input
      type="checkbox"
      :name="locationFreezerFieldProp"
      :disabled="!editing"
      v-model="model.is_freezer"
    />
    <button v-if="editing" class="svg-button save-button" @click="save">
      <svg-icon type="mdi" :path="mdiContentSaveOutline" />
    </button>
    <button v-if="editing" class="svg-button cancel-button" @click="cancel">
      <svg-icon type="mdi" :path="mdiCloseBoxOutline" />
    </button>
    <button v-else class="svg-button edit-button" @click="updateEditState">
      <svg-icon type="mdi" :path="mdiSquareEditOutline" />
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
