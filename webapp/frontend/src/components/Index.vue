<template>
  <h1>Tdl</h1>
  <div ref="violinPlot" style="width: 100%; height: 100%;"></div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import axios from "axios";
import Plotly from 'plotly.js-dist';

const apiUrl = import.meta.env.VITE_APP_API_URL
const violinPlot = ref(null);
const data = ref([])

const getViolin = async () => {
  try {
    const response = await axios.get(apiUrl + '/api/get_violin', {
      headers: {
        "Access-Control-Allow-Origin": "*",
      },
    });
    data.value = response.data;
    const layout = {
      yaxis: {
        zeroline: false
      }
    };

    Plotly.newPlot(violinPlot.value, data.value, layout);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

onMounted(() => {
  getViolin()
})
</script>


<script>
export default {
  name: 'MyIndex',
  props: {
    msg: String
  }
}
</script>

<style></style>