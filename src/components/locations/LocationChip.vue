<script setup lang="ts">
/* eslint-disable @typescript-eslint/no-explicit-any */
import { Location } from '@/models/location'
import SvgIcon from '@jamescoyle/vue-icon'
import { transformKebabCaseToMdiJs } from '@/utilities/IconName'
import * as MdiIconNS from '@mdi/js'

defineProps<{ location: Location }>()

function svgPathFromLocationIcon(icon: string): string {
  const keyname = transformKebabCaseToMdiJs(icon)
  const MdiIconAccess = MdiIconNS as any
  return MdiIconAccess[keyname]
}
</script>
<template>
  <span class="location-chip">
    <svg-icon type="mdi" :path="svgPathFromLocationIcon(location.icon)" />
    {{ location.name }}
  </span>
</template>
<style lang="css" scoped>
.location-chip,
.location-chip > * {
  vertical-align: middle;
}
</style>
