<template>
  <div id="app">

    <button class="app__update-button" @click="update()"> ОБНОВИТЬ </button> <br><br>

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
import axios from 'axios'
import StillageTable from './components/StillageTable.vue'
import TimestampVisualizer from './components/TImestampVisualizer.vue'
import SettingsBlock from './components/SettingsBlock.vue'

export default {
  name: 'App',
  data: function() {
    return {
      data: JSON.parse(json_str),
    }
  },
  methods: {
    update() {
      axios
      .get('http://localhost:5000/cb')
      .then(response => {
        console.log(response);
        this.data = response.data;
      });
    }
  },
  mounted() {
    this.update();
  },
  components: {
    StillageTable,
    TimestampVisualizer,
    SettingsBlock
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
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.app__update-button {
  color: #22373f;
  background: #00ffcc;
  font-size: x-large;
  border: none;
  padding: 16px;
  padding-left: 32px;
  padding-right: 32px;
  border-radius: 50px;
  transition: all 0.2s ease-in-out;
  cursor: pointer;
}

.app__update-button:hover {
  background: #27ffd4;
  color: #29424c;
}

.app__update-button:active {
  background: #00ebbc;
  color: #111;
}

.app__update-button:focus {
  outline: 0px;
}

</style>
