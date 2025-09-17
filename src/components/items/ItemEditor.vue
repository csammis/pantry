<script setup lang="ts">
import { Item } from '@/models/item'
import { getLocations, Location } from '@/models/location'
import LocationChip from '@/components/locations/LocationChip.vue'
import { ref, useTemplateRef } from 'vue'

const locations = ref<Location[]>([])

const model = defineModel<Item>({ required: true })
const props = defineProps<{
  title: string
  acceptButtonText: string
  acceptContinueButtonText: string
  dismissButtonText: string
}>()
const emit = defineEmits(['onDismiss', 'onAccept', 'onAcceptContinue'])
const locationSelectElement = useTemplateRef('location-select')

/** Force the location select change event before emitting the event to add an item.
This ensures the location ID is synchronized to the model if the user doesn't happen
to manually change it. */
function emitAddEvent(name: 'onAccept' | 'onAcceptContinue') {
  handleLocationSelectChange()
  emit(name)
}

function handleLocationSelectChange() {
  model.value.location.id = (locationSelectElement.value as HTMLSelectElement).value || ''
}

getLocations().then(function (resource) {
  locations.value = resource
})
</script>
<template>
  <div class="content">
    <h2>{{ title }}</h2>
    <div class="input-section">
      <div class="input-name">Item name</div>
      <div class="input-control"><input autofocus type="text" v-model="model.name" /></div>
    </div>
    <div class="input-section storage-location">
      <div class="storage-source">
        <div class="input-name">Stored in</div>
        <div class="input-control">
          <LocationChip :location="model.location" />
        </div>
      </div>
      <div class="storage-destination">
        <div class="input-name">Move to...</div>
        <div class="input-control">
          <select
            ref="location-select"
            @select="handleLocationSelectChange"
            @input="handleLocationSelectChange"
          >
            <option
              v-for="loc in locations"
              :key="loc.id"
              :value="loc.id"
              :selected="loc.id == model.location.id"
            >
              <LocationChip :location="loc" />
            </option>
          </select>
        </div>
      </div>
    </div>
    <div class="buttons">
      <button @click="emitAddEvent('onAccept')">{{ props.acceptButtonText }}</button>
      <button v-if="model.id === ''" @click="emitAddEvent('onAcceptContinue')">
        {{ props.acceptContinueButtonText }}
      </button>
      <button value="cancel" formmethod="dialog" @click="$emit('onDismiss')">
        {{ props.dismissButtonText }}
      </button>
    </div>
  </div>
</template>
<style lang="css" scoped>
.message {
  margin-top: 1em;
  margin-bottom: 0.5em;
}

.buttons > * {
  margin: auto 1em;
}

.input-name {
  margin-top: 0.5em;
}

.input-control {
  width: 100%;
}

select {
  width: 100%;
}

input {
  width: 100%;
}

.storage-location {
  display: flow-root;
}

.storage-source {
  float: left;
  width: 50%;
  padding-right: 1em;
}

.storage-destination {
  float: right;
  width: 50%;
  padding-left: 1em;
}

.buttons {
  text-align: center;
  width: 100%;
  margin-top: 1em;
  clear: both;
}
</style>
