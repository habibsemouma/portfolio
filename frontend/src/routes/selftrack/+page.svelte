<script>
    import {Body} from "svelte-body"
    import {PUBLIC_SELFTRACK_URL} from "$env/static/public"
    import {get_activity_options} from "./Helpers.js"
    import axios from "axios"
    import { onMount } from "svelte";
    let chart=null
    let activity={}
    let activity_chart;

    let activity_options

    onMount(async () => {
      const ApexCharts = (await import('apexcharts')).default;

chart = new ApexCharts(activity_chart, activity_options);
chart.render();
})

axios.get(PUBLIC_SELFTRACK_URL)
  .then(function (response) {
    activity=response.data["activity"]


    activity_options = get_activity_options(activity)


    //activity_by_app=response.data["activity"]
    //activity=response.data["activity"]
  })
  .catch(function (error) {
    console.error('Error:', error);
  });
          



</script>
<Body style=" display: flex; flex-direction: column; justify-content: center;align-items: center;gap: 40px;background-color: #F2F4F6;font-family: Arial, Helvetica, sans-serif;color:black;margin: 0;padding: 0;" />

<div bind:this={activity_chart}></div>

<style></style>