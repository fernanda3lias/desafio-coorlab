<template>
  <main class="columns is-gapless is-multiline">
    <div class="column is-one-fifth">
      <BarraLateral/>
    </div>
    <div class="column is-three-quarter">
      <BarraSuperior/>
      <MainGrid/>
    </div>

  </main>
</template>

<script>
import BarraLateral from './components/BarraLateral.vue'
import BarraSuperior from './components/BarraSuperior.vue'
import MainGrid from './components/MainGrid.vue'

export default{
  name: 'App',
  components: {
    BarraLateral,
    BarraSuperior,
    MainGrid
  }
}
</script>

<style>
main {
  background-color: #F6F6F6;
}

</style>
