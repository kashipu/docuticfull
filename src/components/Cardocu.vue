<template>
    <div class="foo">
        <hr>Hi I'm a Foo component with the headline:
        <h2>{{block.id}}</h2>
    </div>
</template>

<script>
export default {
    props: {
        block: Object
    },
    name: "cardocu"
};
</script>