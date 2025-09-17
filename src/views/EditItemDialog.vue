<script setup lang="ts">
import { useTemplateRef, watch } from 'vue'
import { getItem, type Item } from '@/models/item'
import ItemEditor from '@/components/items/ItemEditor.vue'

const emit = defineEmits(['onDismiss', 'onAccept', 'onAcceptContinue'])
const model = defineModel<Item>({ required: true })
const props = defineProps<{ open: boolean }>()
const dialogElement = useTemplateRef('edit-item-dialog')

watch(
  () => props.open,
  async function (newValue: boolean) {
    if (newValue) {
      ;(dialogElement.value as HTMLDialogElement).showModal()
    } else {
      ;(dialogElement.value as HTMLDialogElement).close()
    }
  },
)

/** Reload the model from the backend */
function onDismiss() {
  getItem(model.value.id).then(function (response: Item | undefined) {
    if (response) {
      model.value = response
      emit('onDismiss')
    }
  })
}

const title: string = 'Edit Item'
const updateButtonText: string = 'Update'
const updateAnotherButtonText: string = ''
const dismissButtonText: string = 'Cancel'
</script>
<template>
  <dialog
    id="edit-item-dialog"
    ref="edit-item-dialog"
    closedby="closerequest"
    v-on:close="$emit('onDismiss')"
  >
    <ItemEditor
      v-model="model"
      :title="title"
      :accept-button-text="updateButtonText"
      :accept-continue-button-text="updateAnotherButtonText"
      :dismiss-button-text="dismissButtonText"
      v-on:on-accept="$emit('onAccept')"
      v-on:on-dismiss="onDismiss"
    />
  </dialog>
</template>
<style lang="css" scoped>
dialog {
  background-color: var(--color-background-soft);
  color: var(--color-text);
  border: 1px solid #888;
  padding: 1em 2em;
  margin: auto;
  min-width: 30%;
}
</style>
