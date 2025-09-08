<script setup lang="ts">
import { defineProps } from 'vue'
import { Item } from '@/models/item'
import LocationChip from '../locations/LocationChip.vue'

defineProps<{ item: Item }>()
</script>
<template>
  <div class="item-card">
    <div class="item-card-name">{{ item.name }}</div>
    <div class="item-card-quantity"></div>
    <div class="item-card-location">in <LocationChip :location="item.location" /></div>
  </div>
</template>
<style lang="css" scoped>
.item-card {
  width: 15%;
  margin: 1em;
  border: solid 2px;
  border-radius: 5px;
  text-align: center;
}
.item-card-name {
  font-weight: bold;
  font-size: larger;
}
</style>
