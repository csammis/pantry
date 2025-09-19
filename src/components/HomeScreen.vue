<script setup lang="ts">
import Isotope from 'isotope-layout'
import type { IsotopeOptions } from 'isotope-layout'
import { useTemplateRef, onMounted, ref, nextTick } from 'vue'
import ItemCard from './items/ItemCard.vue'
import { Item, createBlankItem, getItems, storeItem } from '@/models/item'
import NewItemDialog from '@/views/NewItemDialog.vue'
import EditItemDialog from '@/views/EditItemDialog.vue'

const newItem = ref<Item>(createBlankItem())
const editItem = ref<Item>(createBlankItem())
const items = ref<Item[]>([])
const newItemDialogOpen = ref<boolean>(false)
const editItemDialogOpen = ref<boolean>(false)

let iso: Isotope
const isoOptions = {
  itemSelector: '.item-card',
  layoutMode: 'fitRows',
} as IsotopeOptions

function saveNewItemModel() {
  storeItem(newItem.value).then(function (item) {
    if (item) {
      items.value.push(item)
      iso?.layout()
    }
  })
}

function onAddNewItem() {
  newItem.value = createBlankItem()
  newItemDialogOpen.value = true
}

function onNewItemDismiss() {
  newItemDialogOpen.value = false
}

function onNewItemAcceptContinue() {
  saveNewItemModel()
  onAddNewItem()
}

function onNewItemAccept() {
  saveNewItemModel()
  onNewItemDismiss()
}

const gridRecentlyAdded = useTemplateRef('gridRecentlyAdded')

function onItemSelected(item: Item) {
  editItem.value = item
  editItemDialogOpen.value = true
}

function onEditItemDismiss() {
  editItemDialogOpen.value = false
}

onMounted(() => {
  iso = new Isotope(gridRecentlyAdded.value as HTMLElement, isoOptions)
})

getItems().then(async function (resource) {
  items.value = resource
  await nextTick()
  iso?.reloadItems()
  iso?.arrange(isoOptions)
})
</script>
<template>
  <div class="description">
    Pantry is a lightweight application for tracking the food items which you have on hand.
    <a href="#" @click="onAddNewItem">You should add some.</a>
  </div>
  <div class="content">
    <h2>
      Recently Added Items
      <span class="subheader">(<a href="#">view all</a>)</span>
    </h2>
    <div class="grid" ref="gridRecentlyAdded">
      <ItemCard
        v-for="item in items"
        :key="item.id"
        :item="item"
        v-on:on-selected="onItemSelected"
      />
    </div>
    <div v-if="items.length == 0" class="empty">
      No items yet! <a href="#" @click="onAddNewItem">You should add some.</a>
    </div>
  </div>

  <NewItemDialog
    :open="newItemDialogOpen"
    v-model="newItem"
    v-on:on-dismiss="onNewItemDismiss"
    v-on:on-accept="onNewItemAccept"
    v-on:on-accept-continue="onNewItemAcceptContinue"
  />
  <EditItemDialog
    :open="editItemDialogOpen"
    v-model="editItem"
    v-on:on-dismiss="onEditItemDismiss"
  />
</template>
<style lang="css" scoped>
.grid {
  width: 100%;
}

.subheader {
  font-size: smaller;
}
</style>
