<template>
    <div class="container">
        <div class="row">
            <div class="buttonbox col-12">
                <button type="button" class="btn btn-success" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
                    Crear Documento</button>
            </div>
        </div>
        <div class="row my-4">
            <div class="formbox border p-4 bg-light col-12 my-2 collapse" id="collapseExample">
                <form>
                    <div class="form-group">
                        <label for="formGroupExampleInput">Nombre del documento</label>
                        <input type="text" class="form-control" id="formGroupExampleInput" placeholder="Nombre">
                    </div>
                    <div class="form-group">
                        <label for="formGroupExampleInput2">Descripción del documento</label>
                        <input type="text" class="form-control" id="formGroupExampleInput2" placeholder="Descripción">
                    </div>
                    <div class="form-group">
                        <p>Elija el archivo</p>
                        <div class="custom-file">
                            <label class="custom-file-label" for="customFile"></label>
                            <input type="file" class="custom-file-input" id="customFile">
                        </div>
                    </div>
                    <button type="button" class="btn btn-info px-5">Enviar</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>