<script setup lang="ts">
import { ref } from 'vue'
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiPlusOutline } from '@mdi/js'
import LocationEditor from './LocationEditor.vue'
import {
  Location,
  getLocations,
  getLocation,
  createBlankLocation,
  storeLocation,
} from '@/models/location'

const locations = ref<Location[]>([])
getLocations().then((response) => (locations.value = response))

function addNew() {
  // Only push a new one if there isn't already a blank item being filled in
  if (locations.value.length > 0 && locations.value[locations.value.length - 1].id !== '') {
    locations.value.push(createBlankLocation())
  }
}

function onSave(location: Location) {
  storeLocation(location)
}

function onCancel(location: Location) {
  if (location.id === '') {
    locations.value?.pop()
  } else {
    // Reload the item from the backend
    getLocation(location.id).then(function (response) {
      if (response !== undefined) {
        const i = locations.value.indexOf(location)
        locations.value[i] = response
      }
    })
  }
}
</script>
<template>
  <h2>Locations</h2>
  <div class="description">
    Items recorded in Pantry can be added to and moved between distinct locations such as "Kitchen
    Pantry," "Spice Cupboard," "Garage Fridge," etc. <br />
    A location has the following properties:
    <ul>
      <li><em>Name:</em> required and must be unique</li>
      <li>
        <em>Icon:</em> a Material Design Icon identifier to display with the location
        <a href="https://pictogrammers.com/library/mdi/" target="_blank">(MDI reference)</a>
      </li>
      <li><em>Freezer:</em> indicate if the location is freezer storage</li>
    </ul>
  </div>
  <LocationEditor
    v-for="(location, index) in locations"
    :key="location.id"
    v-model="locations[index]"
    v-on:on-save="onSave"
    v-on:on-cancel="onCancel"
  />
  <div class="add-row">
    <button class="svg-button create-button" @click="addNew">
      <svg-icon type="mdi" :path="mdiPlusOutline" />
    </button>
    <span>Add new location</span>
  </div>
</template>
<style lang="css" scoped>
.description {
  margin-bottom: 2em;
}

.add-row > * {
  margin-left: 0.5em;
  display: inline-block;
  vertical-align: middle;
}
</style>
