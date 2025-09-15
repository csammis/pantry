<script setup lang="ts">
import { useTemplateRef, watch } from 'vue'
import { type Item } from '@/models/item'
import ItemEditor from '@/components/items/ItemEditor.vue'

defineEmits(['onDismiss', 'onAccept', 'onAcceptContinue'])
const model = defineModel<Item>({ required: true })
const props = defineProps<{ open: boolean }>()
const dialogElement = useTemplateRef('new-item-dialog')

watch(
  () => props.open,
  function (newValue: boolean) {
    if (newValue) {
      ;(dialogElement.value as HTMLDialogElement).showModal()
    } else {
      ;(dialogElement.value as HTMLDialogElement).close()
    }
  },
)

const title: string = 'Add New Item'
</script>
<template>
  <dialog
    id="new-item-dialog"
    ref="new-item-dialog"
    closedby="closerequest"
    v-on:close="$emit('onDismiss')"
  >
    <ItemEditor
      v-model="model"
      :title="title"
      v-on:on-accept="$emit('onAccept')"
      v-on:on-accept-continue="$emit('onAcceptContinue')"
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
}
</style>
