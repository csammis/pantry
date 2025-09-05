<script setup lang="ts">
import { ref } from 'vue'
import UnitEditor from './UnitEditor.vue'
import { Unit, getUnits } from '@/models/unit'

const units = ref<Unit[]>()
getUnits().then((response) => (units.value = response))
</script>
<template>
  <ul name="unit-list" class="unit-list" v-for="unit in units" :key="unit.id">
    <UnitEditor :unit="unit" />
  </ul>
</template>
