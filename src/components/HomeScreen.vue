<script setup lang="ts">
import Isotope from 'isotope-layout'
import type { IsotopeOptions } from 'isotope-layout'
import { useTemplateRef, onMounted, ref } from 'vue'
import ItemCard from './items/ItemCard.vue'
import { Item } from '@/models/item'
import { Location } from '@/models/location'
import { Unit } from '@/models/unit'

const gridRecentlyAdded = useTemplateRef('gridRecentlyAdded')

onMounted(() => {
  const isoOptions = {
    itemSelector: '.item-card',
    layoutMode: 'fitRows',
  } as IsotopeOptions

  const iso = new Isotope(gridRecentlyAdded.value as HTMLElement, isoOptions)
})

const freezerLoc = new Location('1', 'Chest Freezer', 'snowflake', true)
const fridgeLoc = new Location('2', 'Fridge', 'fridge', false)
const loafUnit = new Unit('1', 'Loaf', 'Loaves')

const items = ref<Item[]>([])
items.value.push(new Item('1', 'Frozen Pizza', freezerLoc, undefined, 2))
items.value.push(new Item('2', 'Bread', freezerLoc, loafUnit, 2))
items.value.push(new Item('3', 'Butter', fridgeLoc, undefined, undefined))
items.value.push(new Item('4', 'Bread', fridgeLoc, loafUnit, 1))
</script>
<template>
  <div class="description">
    Pantry is a lightweight application for tracking the food items which you have on hand.
  </div>
  <div class="content">
    <h2>Recently Added</h2>
    <div class="grid" ref="gridRecentlyAdded">
      <ItemCard v-for="item in items" :key="item.id" :item="item" />
    </div>
  </div>
</template>
<style lang="css" scoped></style>
