<script setup lang="ts">
import { ref } from 'vue'
import LocationEditor from './LocationEditor.vue'
import { Location, getLocations } from '@/models/location'

const locations = ref<Location[]>()
getLocations().then((response) => (locations.value = response))
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
  <ul name="location-list" class="location-list" v-for="location in locations" :key="location.id">
    <LocationEditor :location="location" />
  </ul>
</template>
<style lang="css" scoped>
.description {
  margin-bottom: 2em;
}
</style>
