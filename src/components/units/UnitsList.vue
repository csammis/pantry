<script setup lang="ts">
import { ref } from 'vue'
import UnitEditor from './UnitEditor.vue'
import { Unit, getUnits } from '@/models/unit'

const units = ref<Unit[]>()
getUnits().then((response) => (units.value = response))
</script>
<template>
  <h2>Units</h2>
  <div class="description">
    Items recorded in Pantry can optionally have units associated with them - cups, packages,
    loaves, etc. If an item has a unit associated with it then portions of that item can be consumed
    or moved between locations. If an item doesn't have an associated unit then it is represented as
    a single indivisible "thing" which can't be partially consumed or moved.
  </div>
  <ul name="unit-list" class="unit-list" v-for="unit in units" :key="unit.id">
    <UnitEditor :unit="unit" />
  </ul>
</template>
