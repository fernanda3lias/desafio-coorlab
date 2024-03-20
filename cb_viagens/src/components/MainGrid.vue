<template>
    <nav class="panel backpanel">
        <div class="panel-heading">
            <figure id="img" style="float: left" >
                <img class="header-icon" src="../assets/truck-arrow.png" alt=""/>
            </figure>  
            <p>
                Calculadora de Viagem
            </p>
        </div>
        <nav class="panel boxes">
        <form class="box">
            <div class="box-title">
                <figure id="img" style="float: left" >
                    <img class="title-icon" src="../assets/hand-money.png" alt=""/>
                </figure>  
                <strong class="title-text">Calcule o Valor da Viagem</strong>
            </div>
            <div class="label">
                <form class="field">
                    <label class="label">Destino</label>
                    <div class="control has-icons-right">
                        <div class="select is-fullwidth">
                            <select>
                                <option >Selecione o destino</option>
                            </select>
                        </div>
                        <div class="icon is-small is-right">
                            <i class="fas fa-globe"></i>
                          </div>
                    </div>
                    <label class="label">Data</label>
                    <div class="control has-icons-right">
                        <div class="select is-fullwidth">
                            <select>
                                <option>Selecione a data</option>
                            </select>
                        </div>
                    </div>
                </form>
            </div>
        </form>
        </nav>
    </nav>  
</template>

<script>

export default{
    name: 'MainGrid'
}

</script>

<style>
.panel-heading {
    color: white;
    background-color: hsl(230, 21%, 21%);
}
@media only screen and (max-width: 768px) {
    .panel-heading {
        padding: 0;
        max-width: 0px;
        max-height: 0px;
        visibility: hidden;
    }
}

.backpanel {
    margin-left: 31px;
    margin-right: 31px;
    margin-top: 63px;
    margin-bottom: 20px;
    height: 600px;
    background-color: #FFFFFF;
}

@media only screen and (max-width: 768px) {
    .backpanel {
        margin-top: 30px;
    }
}

.boxes{
    max-width: 407px;
    margin-left: 25px;
    margin-right: 25px;
    margin-top: 29px;
}

.box{
    background-color: hsl(0, 0%, 96%);
    min-height: 490px;
}

.box-title{
        font-size: 22px;
        margin-top: 76px;
        margin-left: 20px;
}

@media only screen and (max-width: 768px) {
    .box-title {
        font-size: 19px;
        margin-left: 8px;
    }
}

.label {
    margin-top: 30px;
    font-size: 15px;
}

.header-icon {
    max-height:50px;
    width: 33px;
    margin-right: 10px;
    margin-left: 30px;
}

.title-text {
    text-align: center;
    vertical-align: middle;
}

.title-icon{
    vertical-align: middle;
    margin-right: 10px;
}

.select {
    margin-left: 10px;
}

.control{
    margin-right: 30px;
}
.label {
    margin-left: 10px;
}

</style>