<template>
  <div id="app">
    <Titulo titulo="DOCUTIC 0.1"/>
    <CrudDocumentos/>
    <Documentos/>  

    </div>
</template>

<script>
import Titulo from './components/Titulo'
import CrudDocumentos from './components/CrudDocumentos'
import Documentos from './components/Documentos'

export default {
  name: 'App',
  components: {
    Titulo,
    Documentos,
    CrudDocumentos
  }
}
</script>

<style>

</style>
