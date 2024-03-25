<template>
    <header class="top">
        <h1></h1>
    </header>
</template>

<script>

export default{
    name: 'SuperiorBar'
}

</script>

<style>
.top {
    padding: 2.5rem;
    height: auto;
    grid-auto-rows: auto;
    background: #FFFFFF;
    border-style: solid;
    border-width: 0px;
    border-bottom-width: 5px;
    border-color: #B3B3B3;
  }

  @media only screen and (max-width: 768px) {
    .top {
        padding: 0;
        width: 0px;
        height: 0px;
        border-bottom-width: 0px;
    }
  }
</style>