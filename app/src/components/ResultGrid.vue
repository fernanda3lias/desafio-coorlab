<template>
    <form id="master" class="column is-two-fifths"> 
        <nobr id="no-data-message" class="no-data">Nenhum dado selecionado.</nobr>
        <nobr id="id-text-trip" class="text-trip">Estas são as melhores alternativas de <br> viagem para a data selecionada</nobr>
        <nav class="" style="display: flex; width: 650px">
        <nav id="res-back" class="res panel is-two-fifths columns" style="background-color:#E5E5E5; margin-left: 0px; display: none">
            <nav class="panel is-two-fifty" style="background-color: #000; height: 105px; width: 78px; background-color: #04A8B5">
                <img class="eco-image" src="../assets/hand-money-white.png" alt=""/>
            </nav>
            <nav style="float:right; margin-left: 40px; margin-top: 16px">
            <strong ><p id="trans-name1">NOME DA TRANSPORTADORA</p></strong>
                <p id="trans1">Poltrona: </p>
            <p id="time1">Tempo estimado:</p>
            </nav>
        </nav>
        <nav id="pp1" class="price panel" style=" display: none">
            <nav style="float:left; margin-left: 40px; margin-top: 25px">
                <strong>Preço</strong>
                <p id="price1">R$ Preço</p>
                </nav>
        </nav>
        </nav>

        <nav class="" style="display: flex; width: 650px">
        <nav id="res-back-nd" class="res-nd panel columns" style="background-color:#F6F6F6; margin-left: 0px; display: none">
            <nav class="panel is-two-fifty" style="background-color: #000; height: 105px; width: 78px; background-color: #04A8B5">
                <img class="eco-image-nd" src="../assets/time-check.png" alt=""/>
            </nav>
            <nav style="float:right; margin-left: 40px; margin-top: 16px">
            <strong><p id="trans-name2">NOME DA TRANSPORTADORA</p></strong>
            <p id="trans2">Leito: </p>
            <p id="time2">Tempo estimado:</p>
            </nav>
        </nav>
        <nav id="pp2" class="price panel" style="margin-top: 40px; background-color: #F6F6F6; display: none">
            <nav style="float:left; margin-left: 40px; margin-top: 25px">
                <strong>Preço</strong>
                <p id="price2">R$ Preço</p>
                </nav>
        </nav>
    </nav>
    
    </form>


</template>

<script>
export default{
    name: 'ResultGrid',
    methods: {
            
        }
        
    }
    function updateResult(cheaper, shorter){
        document.getElementById('id-text-trip').style.fontSize = "20px";
        document.getElementById('id-text-trip').style.display = 'inline-block';
        document.getElementById('res-back').style.display = '';
        document.getElementById('res-back-nd').style.display = '';
        document.getElementById('pp1').style.display = '';
        document.getElementById('pp2').style.display = '';
       
       
        document.getElementById( 'no-data-message' ).style.display = 'none';
        document.getElementById('no-data-message').style.height = 0;

        var Name1 = document.getElementById("trans-name1");
        var Trans1 = document.getElementById("trans1");
        var Time1 = document.getElementById("time1");
        var Price1 = document.getElementById("price1");

        var cheaperName = Object.values(cheaper)[1]
        var cheaperSeat = Object.values(cheaper)[6]
        var cheaperTime = Object.values(cheaper)[5]
        var cheaperPrice = Object.values(cheaper)[3]

        Trans1.textContent = `Poltrona: ${cheaperSeat}`;
        Time1.textContent = `Tempo Estimado: ${cheaperTime}`;
        Name1.textContent = `${cheaperName.toUpperCase()}`;
        Price1.textContent = `${cheaperPrice.toUpperCase()}`;

        var Name2 = document.getElementById("trans-name2");
        var Trans2 = document.getElementById("trans2");
        var Time2 = document.getElementById("time2");
        var Price2 = document.getElementById("price2");

        var shorterName = Object.values(shorter)[1]
        var shorterSeat = Object.values(shorter)[7]
        var shorterTime = Object.values(shorter)[5]
        var shorterPrice = Object.values(shorter)[2]

        Trans2.textContent = `Poltrona: ${shorterSeat}`;
        Time2.textContent = `Tempo Estimado: ${shorterTime}`;
        Name2.textContent = `${shorterName.toUpperCase()}`;
        Price2.textContent = `${shorterPrice.toUpperCase()}`;



        console.log(cheaper)
        console.log(shorter)
    }

    export{updateResult}
</script>

<style>
.no-data {
    display: inline-block;
    margin-top: 235px;
    margin-left: 230px;
    font-size: 20px;
}

@media only screen and (max-width: 1400px) and (min-width: 768px){
    .no-data {
      height: 0px;
      margin: auto;
      display: none;
    }
}

.text-trip {
    display: none;
    font-size: 20px;
    margin-top: 80px;
}

.res{
    margin-top: 25px;
    height: 105px;
    width: 425px;
    display: none;
}

.res-nd{
    margin-top: 40px;
    height: 105px;
    width: 425px;
    display: none;
}

.eco-image {
    height: 45px;
    margin-left: 15px;
    margin-top: 25px;
}

.eco-image-nd {
    height: 45px;
    margin-left: 15px;
    margin-top: 28px;
}

.price {
    margin-left: 30px;
    margin-right: 0px;
    height: 105px;
    width: 212px;
    margin-top:25px;
    background-color:#E5E5E5;
}

</style>

