<script setup lang="ts">
import { ref } from 'vue'
import SvgIcon from '@jamescoyle/vue-icon'
import {
  mdiContentSaveOutline,
  mdiCloseBoxOutline,
  mdiSquareEditOutline,
  mdiTrashCanOutline,
} from '@mdi/js'
import { Location } from '@/models/location'

const emit = defineEmits<{
  (e: 'onSave', location: Location): void
  (e: 'onCancel', location: Location): void
  (e: 'onDelete', location: Location): void
}>()

const model = defineModel<Location>({ required: true })
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
const locationNameFieldProp = 'location-name-' + model.value.id
const locationIconFieldProp = 'location-icon-' + model.value.id
const locationFreezerFieldProp = 'location-freezer-' + model.value.id
</script>
<template>
  <div class="item-editor">
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
