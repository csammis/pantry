<script setup lang="ts">
import { ref } from 'vue'
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiFridgeOutline, mdiCup, mdiHomeOutline, mdiDatabaseSettingsOutline } from '@mdi/js'
import { Slide } from 'vue3-burger-menu'
import HomeScreen from './components/HomeScreen.vue'
import LocationEditorList from './components/locations/LocationEditorList.vue'
import UnitEditorList from './components/units/UnitEditorList.vue'

interface NavMenuItem {
  icon: string
  name: string
  hidden: boolean
}

const navMenu = ref<NavMenuItem[]>([
  {
    icon: mdiHomeOutline,
    name: 'Home',
    hidden: false,
  },
])

const settingsMenu = ref<NavMenuItem[]>([
  {
    icon: mdiCup,
    name: 'Units',
    hidden: true,
  },
  {
    icon: mdiFridgeOutline,
    name: 'Locations',
    hidden: true,
  },
])

function showNavElement(navItem: NavMenuItem) {
  for (const item of settingsMenu.value.values()) {
    item.hidden = true
  }
  for (const item of navMenu.value.values()) {
    item.hidden = true
    if (item.name === navItem.name) {
      item.hidden = false
    }
  }
}

function showSettingsElement(navItem: NavMenuItem) {
  for (const item of navMenu.value.values()) {
    item.hidden = true
  }
  for (const item of settingsMenu.value.values()) {
    item.hidden = true
    if (item.name === navItem.name) {
      item.hidden = false
    }
  }
}
</script>

<template>
  <div class="banner">
    <header>Pantry</header>
  </div>
  <div class="main">
    <main>
      <Slide :closeOnNavigation="true">
        <div class="nav-menu-item" v-for="item in navMenu" :key="item.name">
          <svg-icon type="mdi" :path="item.icon" />
          <a href="#" @click="showNavElement(item)">{{ item.name }}</a>
        </div>
        <div class="nav-menu-item">
          <svg-icon type="mdi" :path="mdiDatabaseSettingsOutline" />
          Settings
        </div>
        <div class="nav-menu-item indent1" v-for="item in settingsMenu" :key="item.name">
          <svg-icon type="mdi" :path="item.icon" />
          <a href="#" @click="showSettingsElement(item)">{{ item.name }}</a>
        </div>
      </Slide>
      <HomeScreen v-if="navMenu[0].hidden == false" />
      <UnitEditorList v-if="settingsMenu[0].hidden == false" />
      <LocationEditorList v-if="settingsMenu[1].hidden == false" />
    </main>
  </div>
</template>

<style scoped>
header {
  font-size: 3em;
  position: absolute;
  top: 0px;
  margin: 0px;
  /* These values line up with the hamburger menu I'm using */
  line-height: 30px;
  padding-top: 36px;
  padding-left: 96px;
  padding-bottom: 30px;
  vertical-align: middle;
  background-color: var(--color-banner);
  width: 100%;
}

.main {
  padding-left: 2em;
  padding-top: 7em;
}

svg {
  width: 24px;
  height: 24px;
  margin-right: 0.5em;
}

.nav-menu-item {
  padding: 0.5em;
}

.nav-menu-item,
.nav-menu-item > a,
.nav-menu-item > svg {
  vertical-align: middle;
}

.nav-menu-item > a,
a:visited {
  color: var(--vt-teal-ligthen-5);
  text-decoration: underline;
}

.indent1 {
  margin-left: 1em;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
