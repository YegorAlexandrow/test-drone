<template>
  <div id="app">
    <stillage-table :width="data.width" :height="data.height" :data="data.cellsBarcodes" title="Cells barcodes" subtitle="Отфильтрованные данные баркодов" />

    <br><br><br>

    <stillage-table :width="data.width" :height="data.height" :data="data.sourceBarcodes" title="Source barcodes" subtitle="Исходное расположение баркодов" />

    <br><br><br>

    <timestamp-visualizer :data="data.sourceBarcodes" :width="data.width" :height="data.height" :video-barcode="data.videoBarcode" :drone-cells="data.droneCells" title="Timestamp" subtitle="Текущая ячейка и распознанные неотфильтрованные баркоды в выбранный момент времени" />

    <br><br><br>

  </div>
</template>
<script>
/* eslint-disable */
import StillageTable from './components/StillageTable.vue'
import TimestampVisualizer from './components/TImestampVisualizer.vue'

export default {
  name: 'App',
  data: function() {
    return {
      data: JSON.parse(json_str),
    }
  },
  components: {
    StillageTable,
    TimestampVisualizer
  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css?family=Baloo+Chettan+2&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap');

/* ------------------------------------ */
* {
  font-family: 'Ubuntu mono', monospace;
	margin: 0px; 
	padding: 0px; 
	box-sizing: border-box;
}

body, html {
    background: #fafafa;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
