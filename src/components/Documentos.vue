<template>
  <div class="container">
      <div class="lead">
          <h2>Documentos</h2>
      </div>
    <div class="row">
        <div class="doculist">
            <div class="card m-3" v-for="(value, index) in datos">
                <img :src="value.file_img" class="card-img-top" alt="">
                <div class="card-body">
                    <h5 class="card-title">{{ value.file_name }} </h5>
                    <p class="card-text">{{ value.file_description}}</p>
                    <p>{{ value.file_id}}</p>
                    <p>{{ value.file_type }}</p>
                    <p>{{ value.file_size }}</p>
                    <div>
                        <a href="#" class="btn ml-0 btn-sm btn-warning">Editar</a>
                        <a href="#" class="btn mx-2 btn-sm btn-danger">Eliminar</a>
                        <a href="#" class="btn mx-2 btn-sm btn-info">Descargar</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
    import axios from "axios"

export default {
    data() {
        return {
            datos: null
                }
    },
    methods: {
        async getData() {
            let data = await axios.get('https://docutic.herokuapp.com/list-files')
            this.datos = await data.data
        }
    }, 
    created(){
        this.getData()
    }
  }

</script>

<style>
.doculist {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
}

@media only screen and (max-width: 995px) {
.doculist {
    display: grid;
    grid-template-columns: 1fr 1fr;
}
}

@media only screen and (max-width: 767px) {
.doculist {
    display: grid;
    grid-template-columns: 1fr;
}
}


</style>
