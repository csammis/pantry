<script setup lang="ts">
import { ref } from 'vue'
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
  <v-row dense>
    <v-col>
      <v-text-field
        :name="locationNameFieldProp"
        :disabled="!editing"
        label="Location name"
        v-model="model.name"
      />
    </v-col>
    <v-col>
      <v-text-field
        :name="locationIconFieldProp"
        :disabled="!editing"
        label="Icon (mdi:)"
        v-model="model.icon"
      />
    </v-col>
    <v-col>
      <v-checkbox
        :name="locationFreezerFieldProp"
        :disabled="!editing"
        v-model="model.is_freezer"
        label="Freezer?"
      />
    </v-col>
    <v-col>
      <v-btn v-if="editing" icon="mdi-content-save-outline" @click="saveItem" />
      <v-btn v-if="editing" icon="mdi-close-box-outline" @click="cancelItem" />
      <v-btn v-if="!editing" icon="mdi-square-edit-outline" @click="updateEditState"></v-btn>
      <v-btn v-if="!editing" icon="mdi-trash-can-outline" @click="deleteItem"></v-btn>
    </v-col>
  </v-row>
</template>
