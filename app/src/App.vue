<template>
  <main class="columns is-gapless is-multiline">
    <div class="column is-narrow">
      <SideBar/>
    </div>
    <div class="column is-three-quarter">
      <SuperiorBar/>
      <MainGrid/>
    </div>

  </main>
</template>

<script>
import SideBar from './components/SideBar.vue'
import SuperiorBar from './components/SuperiorBar.vue'
import MainGrid from './components/MainGrid.vue'

export default{
  name: 'App',
  components: {
    SideBar,
    SuperiorBar,
    MainGrid
  }
}
</script>

<style>
main {
  background-color: #F6F6F6;
}

</style>
