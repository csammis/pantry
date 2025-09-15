<script setup lang="ts">
import { defineProps } from 'vue'
import { Item } from '@/models/item'
import LocationChip from '../locations/LocationChip.vue'
import type { Unit } from '@/models/unit'
import { makeSingularOrPlural } from '@/utilities/Pluralizer'

const props = defineProps<{ item: Item }>()
const emit = defineEmits<{
  (e: 'onSelected', item: Item): void
}>()

function emitOnSelected() {
  emit('onSelected', props.item)
}

function renderQuantity(unit?: Unit, quantity?: number): string {
  if (!unit && !quantity) {
    return ''
  }
  let name = 'item'
  let plural = 'items'
  if (unit !== undefined) {
    name = unit.name.toLocaleLowerCase()
    plural = unit.plural.toLocaleLowerCase()
  }
  const amount = quantity as number
  return `${amount.toLocaleString()} ${makeSingularOrPlural(amount, name, plural)}`
}
</script>
<template>
  <div class="item-card" @click="emitOnSelected">
    <div class="item-card-name">{{ item.name }}</div>
    <div class="item-card-quantity">{{ renderQuantity(item.unit, item.unit_quantity) }}</div>
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
  cursor: pointer;
}

.item-card-name {
  font-weight: bold;
  font-size: larger;
}
</style>
