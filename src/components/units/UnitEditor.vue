<script setup lang="ts">
import { ref } from 'vue'
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
  <v-row dense>
    <v-col>
      <v-text-field
        :name="unitNameFieldProp"
        :disabled="!editing"
        label="Unit name"
        v-model="model.name"
      />
    </v-col>
    <v-col>
      <v-text-field
        :name="unitPluralFieldProp"
        :disabled="!editing"
        label="Plural name"
        v-model="model.plural"
      />
    </v-col>
    <v-col>
      <v-btn v-if="editing" icon="mdi-content-save-outline" @click="saveItem"></v-btn>
      <v-btn v-if="editing" icon="mdi-close-box-outline" @click="cancelItem"></v-btn>
      <v-btn v-if="!editing" icon="mdi-square-edit-outline" @click="updateEditState"></v-btn>
      <v-btn v-if="!editing" icon="mdi-trash-can-outline" @click="deleteItem"></v-btn>
    </v-col>
  </v-row>
</template>
