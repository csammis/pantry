<script lang="ts">
export class ConfirmDialogOptions {
  public title: string
  public message: string
  public visible: boolean
  public acceptText: string
  public dismissText: string
  public context: object | undefined

  public constructor() {
    this.title = ''
    this.message = ''
    this.visible = false
    this.acceptText = 'Yes'
    this.dismissText = 'No'
    this.context = undefined
  }
}
</script>

<script setup lang="ts">
import { ref, watch } from 'vue'

const dialogStyle = ref('dialog-hidden')

const props = defineProps<{
  options: ConfirmDialogOptions
}>()

defineEmits(['onDismiss', 'onAccept'])

watch(
  () => props.options.visible,
  function (newValue: boolean, oldValue: boolean) {
    if (newValue === true) {
      dialogStyle.value = 'dialog-visible'
    } else {
      dialogStyle.value = 'dialog-hidden'
    }
  },
)
</script>
<template>
  <div id="confirm-dialog" :class="dialogStyle">
    <div class="content">
      <a class="close" @click="$emit('onDismiss')">&times;</a>
      <h2>{{ options.title }}</h2>
      <div class="message">{{ options.message }}</div>
      <span class="buttons">
        <button @click="$emit('onDismiss')">{{ options.dismissText }}</button>
        <button @click="$emit('onAccept')">{{ options.acceptText }}</button>
      </span>
    </div>
  </div>
</template>
<style lang="css" scoped>
#confirm-dialog {
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
}

.dialog-hidden {
  display: none;
}

.dialog-visible {
  display: block;
}

.content {
  background-color: var(--color-background-soft);
  margin: 15% auto;
  border: 1px solid #888;
  width: 25%;
  padding: 2em;
}

.close {
  float: right;
  font-size: x-large;
  font-weight: bold;
  margin-top: -1em;
  margin-right: -0.5em;
  text-decoration: none;
}

.close:hover {
  cursor: pointer;
}

.message {
  margin-top: 1em;
  margin-bottom: 0.5em;
}

.buttons {
  text-align: center;
  width: 100%;
}

.buttons > * {
  margin: auto 1em;
}
</style>
