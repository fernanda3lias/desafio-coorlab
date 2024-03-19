<template>
  <main class="columns is-gapless is-multiline">
    <div class="column is-one-fifth">
      <BarraLateral/>
    </div>
    <div class="column is-three-quarter">

    </div>
  </main>
</template>

<script>
import BarraLateral from './components/BarraLateral.vue'

export default{
  name: 'App',
  components: {
    BarraLateral
  }
}
</script>
