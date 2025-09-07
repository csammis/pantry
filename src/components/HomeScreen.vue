<script setup lang="ts">
import Isotope from 'isotope-layout'
import type { IsotopeOptions } from 'isotope-layout'
import { useTemplateRef, onMounted } from 'vue'

const grid = useTemplateRef('grid')

onMounted(() => {
  const isoOptions = {
    itemSelector: '.grid-item',
    layoutMode: 'fitRows',
  } as IsotopeOptions

  const iso = new Isotope(grid.value as HTMLElement, isoOptions)
})
</script>
<template>
  <div class="description">
    Pantry is a lightweight application for tracking the food items which you have on hand.
  </div>
  <div class="content">
    <h2>What's On Hand?</h2>
    <div class="grid" ref="grid">
      <div class="grid-item">
        <div class="grid-item-name">Butter</div>
        <div class="grid-item-location">in Fridge</div>
      </div>
      <div class="grid-item">
        <div class="grid-item-name">Frozen Pizza</div>
        <div class="grid-item-location">in Chest Freezer</div>
      </div>
      <div class="grid-item">
        <div class="grid-item-name">Bread</div>
        <div class="grid-item-quantity">2 loaves</div>
        <div class="grid-item-location">in Chest Freezer</div>
      </div>
      <div class="grid-item">
        <div class="grid-item-name">Soy Sauce</div>
        <div class="grid-item-location">in Pantry</div>
      </div>
    </div>
  </div>
</template>
<style lang="css" scoped>
.grid-item {
  width: 15%;
  margin: 1em;
  border: solid 2px;
  border-radius: 5px;
  text-align: center;
}

.grid-item-name {
  font-weight: bold;
  font-size: larger;
}
</style>
