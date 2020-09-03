<template>
    <div>
        <h1 class="stillage-table__title"> {{ title }} </h1>
        <p class="stillage-table__subtitle"> {{ subtitle }} </p>

        <table class="stillage-table">
            <tbody>
                <tr class="stillage-table__row" v-for="(row, index) in data.slice().reverse()" :key="index">

                    <td class="stillage-table__row-index"> {{ data.length - index - 1 }} </td>

                    <template v-for="(section, si) in row">
                        <td v-if="section.length > 0 && section[0] > 0 && selectedCell[0] == data.length - index - 1 && selectedCell[1] == si" class="stillage-table__cell stillage-table__cell--barcode stillage-table__cell--selected" :key="si">
                            <p v-for="(b, i) in section" :key="i"> {{ b | barcode }} </p>
                        </td>
                        <td v-else-if="section.length > 0 && section[0] > 0" class="stillage-table__cell stillage-table__cell--barcode" :key="si">
                            <p v-for="(b, i) in section" :key="i"> {{ b | barcode }} </p>
                        </td>
                        <td v-else-if="section.length > 0" class="stillage-table__cell stillage-table__cell--na" :key="si">
                            N/A
                        </td>
                        <td v-else-if="selectedCell[0] == data.length - index - 1 && selectedCell[1] == si" class="stillage-table__cell  stillage-table__cell--empty stillage-table__cell--selected" :key="section">
                            Пусто
                        </td>
                        <td v-else class="stillage-table__cell  stillage-table__cell--empty" :key="section">
                            Пусто
                        </td>
                    </template>

                    <td></td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td></td>
                    <td class="stillage-table__col-index" v-for="i in 16" :key="i">
                        {{ i-1 }}
                    </td>
                </tr>
            </tfoot>
        </table>
    </div>
</template>

<script>

/* eslint-disable */
export default {
    name: 'stillage-table',
    data: function () {
        return {
            
        }
    },
    props: {
        data: Array,
        width: Number,
        height: Number,
        title: String,
        subtitle: String,
        selectedCell: {
            type: Array,
            default: [-1 , -1]
        }
    },
    filters: {
        reverse: function (array) {
            return array.slice().reverse()
        },
        barcode: function (source) {
            var text = source + '';

            while(text.length < 7)
                text = '0' + text;
            return text;
        }
    }
}
</script>

<style>

.stillage-table {
    border-collapse: collapse;
    width: 90%;
    margin: 0 auto;
    position: relative;
    table-layout: fixed;
    border: none;
    font-size: small;
}

.stillage-table__row {
    height: 3.5em;
}

.stillage-table__cell {
    background: white;
    border: 1px solid #ccc;
    transition: all 0.5s ease-in-out;
    overflow: hidden;
    cursor: default;
}

.stillage-table__cell:hover {
    font-size: 110%;
}

.stillage-table__cell--barcode:hover {
    background: #d8fff7;
}

.stillage-table__cell--selected {
    background: #00ffcc;
    color: #22373f;
    font-weight: bold;
}

.stillage-table__cell--selected:hover {
    background: #00ffcc;
}

.stillage-table__cell--empty {
    color: #ff3300;
}

.stillage-table__cell--empty:hover {
    background: #ffefeb;
}

.stillage-table__cell--na {
    color: #999;
    background: #fff;
}

.stillage-table__cell--na:hover {
    background: #e5eef1;
}

.stillage-table__row-index {
    text-align: right;
    padding-right: 1em;
}

.stillage-table__col-index {
    text-align: center;
    padding-top: 1em;
}

.stillage-table__title {
    color: #22373f;
    margin-bottom: .4em;
}

.stillage-table__subtitle {
    color: #666;
    margin-bottom: 1em;
}

</style>