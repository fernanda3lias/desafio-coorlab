<template>
    <nav>
    <div class="panel-heading">
        <figure id="img" style="float: left" >
            <img class="header-icon" src="../assets/truck-arrow.png" alt=""/>
        </figure>  
        <p>
            Calculadora de Viagem
        </p>
    </div>

    <div class="popup-overlay" v-if="isPopupVisible">
        <div class="popup" style="width: 418px">
          <span @click="closePopup" class="close">&times;</span>
            <img class="alert-icon" src="../assets/alert.png" alt=""/>
          <p style="font-size: 22px; margin-top: 20px; text-align:center">Insira os valores para realizar <br> a cotação.</p>
          <button class="closepop button" @click="closePopup">Fechar</button>
        </div>
    </div>

    <nav class="panel backpanel columns">
        <nav class="panel boxes is-two-fifths">
        <form class="box">
            <div class="box-title">
                <figure id="img" style="float: left" >
                    <img class="title-icon" src="../assets/hand-money.png" alt=""/>
                </figure>  
                <strong class="title-text">Calcule o Valor da Viagem</strong>
            </div>
            <div class="label">
                <form class="field" @submit.prevent>
                    <label class="label">Destino</label>
                    
                    <div class="dropmargin">
                        <div class="select is-fullwidth">
                            <select class="has-text-grey-light" @change="onChange($event)">
                                <option value="" disabled selected hidden>Selecione o destino</option>
                                <option class="has-text-grey">Belo Horizonte</option>
                                <option class="has-text-grey" >Campinas</option>
                                <option class="has-text-grey">Curitiba</option>
                                <option class="has-text-grey">Fortaleza</option>
                                <option class="has-text-grey">Manaus</option>
                                <option class="has-text-grey">Natal</option>
                                <option class="has-text-grey">Recife</option>
                                <option class="has-text-grey">Rio de Janeiro</option>
                                <option class="has-text-grey">São Paulo</option>
                                <option class="has-text-grey">Salvador</option>
                            </select>
                        </div>
                        <div class="icon is-small is-right">
                            <i class=""></i>
                          </div>
                    </div>
                    <label class="second-label label">Data</label>
                    <div class="control">
                        <div class="calendar is-fullwidth">
                            <input  class="input has-text-grey-light" id="input" type="text" placeholder="Selecione a data" onfocus="(this.type='date')" onblur="(this.type='text')" />
                            
                        </div>
                    </div>
                    <button class="search button" @click="send">Buscar</button>
                </form>
            </div>
            
        </form>
        </nav>

    <ResultGrid/>
        
        
    </nav>  

    </nav>
</template>


<script>
import ResultGrid from './ResultGrid.vue'
import { updateResult } from './ResultGrid.vue'

export default { 
    name: 'MainGrid',
    data() {
    return {
      isPopupVisible: false
    };
  },
    components:{
        ResultGrid
    },
    methods: {
        showPopup() {
      this.isPopupVisible = true;
    },
    closePopup() {
      this.isPopupVisible = false;
    },
        send: function() {
            console.log('sending')
            this.day = document.getElementById('input').value 
            console.log(document.getElementById('input').value)
            if (this.selectedIndex == undefined){console.log("<empty.string>"); this.city = ""}
                else{console.log(this.selectedIndex); this.city = this.selectedIndex}

            this.submitForm()

            if (this.day != "" & this.city != ""){this.fetchData()}
            else{this.showPopup()}

            
        },

        hide: function() {
            if (document.getElementsByClassName("input").focus == true){document.getElementsByClassName("icon").style.opacity = "0.0"}
        },

        onChange: function(event) {
            this.selectedIndex =  event.target.value;
        },

        async submitForm() {

        this.formData = { city: this.city,
            day: this.day

        }
      try {
        const response = await fetch('http://localhost:3000/submit-form', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.formData)
        });
        if (!response.ok) {
          throw new Error('Error trying sending');
        }
        console.log('Success!');
      } catch (error) {
        console.error(error);
      }
    },

    async fetchData() {
        fetch('http://localhost:3000/submit-form')
        .then(response => {
            if (!response.ok) {
            throw new Error('Error searching for data');
            }

            this.results = response.json();
            this.city = this.results["city"]
            this.day = this.results[""]

            return this.results;
        })
        .then(data => {
            this.cheaper = data["cheaper"]
            this.shorter = data["shorter"]

            this.cheaperName = this.cheaper["name"]
            this.cheaperPrice = this.cheaper["price_econ"]

            updateResult(this.cheaper, this.shorter);
        })
        .catch(error => {
            console.error(error);
        });
  }
}}


</script>

<style>
.select:not(.is-multiple):not(.is-loading)::after {
    border-color: transparent;
}

.panel-heading {
    color: white;
    margin-left: 31px;
    margin-right: 31px;
    margin-top: 30px;
    margin-bottom: 0px; 
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
    margin-top: 0px;
    margin-bottom: 20px;
    height: 550px;
    background-color: #FFFFFF;
}

@media only screen and (max-width: 768px) {
    .backpanel {
        margin-top: 30px;
        background-color: #F6F6F6;
    }
}

.boxes{
    min-width: 400px;
    max-height: 490px;
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
        margin-top: 60px;
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

.dropmargin{
    margin-right: 30px;
}
.label {
    margin-left: 10px;
}
.search{
    margin-top: 40px;
    margin-left: 80px;
    width: 180px;
    color: #2B2F42;
    background-color: #04A8B5;
    border-color: #2B2F42;
    font-weight: bold;
}

.info {
    float: right;
}

.second-label {
    margin-top: 0px;
}

.calendar {
    margin-left: 10px;

}

.control {
    margin-right: 20px;
}

.popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 999;
  }
  
.popup {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
}
  
.close {
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
}

.alert-icon {
    height: 60px;
    display: inline;
    margin-left:160px;
}

.closepop {
    margin-top: 40px;
    margin-left: 100px;
    width: 180px;
    color: #2B2F42;
    background-color: #04A8B5;
    border-color: #2B2F42;
    font-weight: bold; 
}
</style>