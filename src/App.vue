<script setup lang="ts">
import { ref } from 'vue'
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiFridgeOutline, mdiCup, mdiHomeOutline } from '@mdi/js'
import { Slide } from 'vue3-burger-menu'
import HomeScreen from './components/HomeScreen.vue'
import LocationsList from './components/locations/LocationsList.vue'
import UnitsList from './components/units/UnitsList.vue'

interface NavMenuItem {
  icon: string
  name: string
  hidden: boolean
}

const navMenu = ref([
  {
    icon: mdiHomeOutline,
    name: 'Home',
    hidden: false,
  },
  {
    icon: mdiFridgeOutline,
    name: 'Locations',
    hidden: true,
  },
  {
    icon: mdiCup,
    name: 'Units',
    hidden: true,
  },
])

function showElement(navItem: NavMenuItem) {
  for (const item of navMenu.value.values()) {
    item.hidden = true
    if (item.name === navItem.name) {
      item.hidden = false
    }
  }
}
</script>

<template>
  <div id="main">
    <header>
      <h1>Pantry</h1>
      <h3>Where is all my food please</h3>
    </header>
    <main>
      <Slide>
        <span class="nav-menu-item" v-for="item in navMenu" :key="item.name">
          <svg-icon type="mdi" :path="item.icon" />
          <a href="#" @click.stop="showElement(item)">{{ item.name }}</a>
        </span>
      </Slide>
      <HomeScreen v-if="navMenu[0].hidden == false" />
      <LocationsList v-if="navMenu[1].hidden == false" />
      <UnitsList v-if="navMenu[2].hidden == false" />
    </main>
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
  text-align: center;
}

.main {
  padding-left: 3em;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

.nav-menu-item > a,
a:visited {
  color: var(--color-text);
  text-decoration: none;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
