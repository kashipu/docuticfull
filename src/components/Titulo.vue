<template>
    <nav class="navbar navbar-dark bg-dark mb-5">
        <div class="container">
            <a class="navbar-brand text-white">{{titulo}}</a>
            <form class="form-inline">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-success my-2 my-sm-0" type="submit">Buscar</button>
            </form>
        </div>
    </nav>
</template>

<script>
export default {
    name: "Titulo",
    props: {
        titulo: String
    }
}
</script>

<style>

</style>