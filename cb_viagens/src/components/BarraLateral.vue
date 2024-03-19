<template>
    <header>
        <h1>
            <img class="logo" src="../assets/logo.png" alt="">
            <img class="title" src="../assets/side-title.png" alt="">
            <img class="icon" src="../../public/favicon.png" alt="">
        </h1>
    </header>

</template>

<script>

export default{
    name: 'BarraLateral'
}

</script>

<style scoped>
header {
    padding-top: 35px;
    padding-left: 23px;
    background: #2B2F42;
    width: 100%;
    height: 100vh;
  }
  @media only screen and (max-width: 1152px) and (min-width: 768px) {
    header {
      padding: 2.5rem;
      height: 100vh;
      grid-auto-rows: auto;
      display: flex;
      justify-content: center;
    }
  }

  @media only screen and (max-width: 768px) {
    header {
      padding: 2.5rem;
      height: auto;
      grid-auto-rows: auto;
      display: flex;
      justify-content: center;
    }
  }
.logo {
    width: 200px;
    height: 30.22px;
  }

  @media only screen and (max-width: 1152px) and (min-width: 768px){
    .logo {
        margin-top: 15px;
        width: 0px;
    }
}

  @media only screen and (max-width: 768px) {
    .logo {
        margin: auto;
        display: block;
    }
  }

.title {
    margin-top: 55px;
    width: 254px;
    height: 24px;
  }
  @media only screen and (max-width: 1250px) and (min-width: 768px){
    .title {
        margin-top: 15px;
        width: 0px;
    }
  }
  @media only screen and (max-width: 768px) {
    .title {
        margin-top: 15px;
    }
  }

  .icon{
    width: 0px;
  }

  @media only screen and (max-width: 1152px) and (min-width: 768px){
    .icon {
        margin-top: 0px;
        width: 72px;
        height: 72px;
    }
  }
    

</style>