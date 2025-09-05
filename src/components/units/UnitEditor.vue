<script setup lang="ts">
import { ref } from 'vue'
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiContentSaveOutline, mdiCloseBoxOutline, mdiSquareEditOutline } from '@mdi/js'
import { Unit } from '@/models/unit'

const props = defineProps({
  unit: {
    type: Unit,
    required: true,
  },
})

const editing = ref(false)

function cancel() {
  //todo discard changes
  updateEditState()
}

function save() {
  //todo persist changes
  updateEditState()
}

function updateEditState() {
  editing.value = !editing.value
}
</script>
<template>
  <div class="row unit-editor">
    <input
      type="text"
      :disabled="!editing"
      placeholder="Unit name (cup, pint, loaf)"
      :value="props.unit.name"
    />
    <input
      type="text"
      :disabled="!editing"
      placeholder="Plural name (cups, pints, loaves)"
      :value="props.unit.plural"
    />
    <button v-if="editing" class="svgBtn saveBtn" @click="save">
      <svg-icon type="mdi" :path="mdiContentSaveOutline" />
    </button>
    <button v-if="editing" class="svgBtn cancelBtn" @click="cancel">
      <svg-icon type="mdi" :path="mdiCloseBoxOutline" />
    </button>
    <button v-else class="svgBtn editBtn" @click="updateEditState">
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

.svgBtn {
  height: 24px;
  width: 24px;
  color: whitesmoke;
  background-color: transparent;
  border-radius: 3px;
  filter: brightness(75%);
}

.svgBtn:hover {
  filter: brightness(100%);
}

.cancelBtn {
  background-color: firebrick;
}

.saveBtn {
  background-color: darkgreen;
}
</style>
