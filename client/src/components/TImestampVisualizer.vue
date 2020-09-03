<template>
    <div>
        <stillage-table :selectedCell="droneCells[currentFrame]" :width="width" :height="height" :data="currentState" :title="title" :subtitle="subtitle" />

        <br><br>
        <input class="timestamp-visualizer__frame-range" type="range" v-model="currentFrame" min="0" :max="videoBarcode.length-1">
        <span>
            {{currentFrame}} / {{videoBarcode.length-1}}
        </span>
    </div>
</template>

<script>
/* eslint-disable */
import StillageTable from '../components/StillageTable.vue'

export default {
    name: 'timestamp-visualizer',
    components: {
        StillageTable
    },
    data: function () {
        return {
            currentFrame: 0
        }
    },
    props: {
        data: Array,
        videoBarcode: Array,
        droneCells: Array,
        title: String,
        subtitle: String,
        width: Number,
        height: Number,
    },
    computed: {
        currentState: function() {
            let result = []

            for(let y = 0; y < this.height; y++) {
                result[y] = []
                for(let x = 0; x < this.width; x++) {
                    if(y == this.droneCells[this.currentFrame][0] && x == this.droneCells[this.currentFrame][1]) {
                        result[y][x] = this.videoBarcode[this.currentFrame]
                    } else {
                        result[y][x] = [-1]
                    }
                }
            }

            return result
        }
    },
    filters: {
        
    }
}
</script>

<style>

.timestamp-visualizer__current-frame {
    width: 7em;
}

.timestamp-visualizer__frame-range {
    width: calc(80% - 8em);
}

.timestamp-visualizer__frame-range {
  margin: 10px 0;
  background-color: transparent;
  -webkit-appearance: none;
}

input[type=range]:focus {
    outline: 0px;
  box-shadow: 0 0px 6px rgba(0, 255, 204, 0.5), 0 0px 6px rgba(0, 255, 204, 0.5);
}

input[type=range]::-webkit-slider-runnable-track {
  background: #22373f;
  border: none;
  border-radius: 3px;
  width: 100%;
  height: 6px;
  cursor: pointer;
}

input[type=range]::-webkit-slider-thumb {
  margin-top: -11px;
  width: 30px;
  height: 30px;
  background: #00ffcc;
  border: 1px solid #ffffff;
  border-radius: 15px;
  cursor: pointer;
  -webkit-appearance: none;
}

input[type=range]::-moz-range-thumb {
  width: 30px;
  height: 30px;
  background: #00ffcc;
  border: 1px solid #ffffff;
  border-radius: 15px;
  cursor: pointer;
}
input[type=range]::-ms-thumb {
  width: 30px;
  height: 30px;
  background: #00ffcc;
  border: 1px solid #ffffff;
  border-radius: 15px;
  cursor: pointer;
  margin-top: 0px;
  /*Needed to keep the Edge thumb centred*/
}
input[type=range]:focus::-ms-fill-lower {
  background: #424242;
}
input[type=range]:focus::-ms-fill-upper {
  background: #4f4f4f;
}


</style>