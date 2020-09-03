<template>
    <div сlass="settings-block">
        <span сlass="settings-block__label">Погрешность: </span>
        <input type="number" min="0" max="50" step="0.5" v-model="error">
        <span сlass="settings-block__unit">% </span>
        <span сlass="settings-block__label">Заполнение: </span>
        <input type="number" min="0" max="100" step="0.5" v-model="fill">
        <span сlass="settings-block__unit">% </span>
        <span сlass="settings-block__label">Скорость дрона: </span>
        <input type="number" min="0.1" max="1.5" step="0.05" v-model="speed">
        <span сlass="settings-block__unit">м/с </span>
        <span сlass="settings-block__label">Частота: </span>
        <input type="number" min="5" max="15" step="0.5" v-model="freq">
        <span сlass="settings-block__unit">Гц </span>
        
        <br><br>
        
        <button> Обновить </button>
    </div>
</template>

<script>

/* eslint-disable */
export default {
    name: 'settings-block',
    data: function () {
        return {
            error: 10,
            fill: 80,
            speed: 1,
            freq: 10
        }
    },
    props: {
    },
    filters: {
    }
}
</script>

<style>

.settings-block {
    font-size: large;
}

.settings-block__label {
    font-size: large;
}

</style>