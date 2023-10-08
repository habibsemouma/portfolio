<script>
  import { Body } from "svelte-body";
  import { get_activity_options } from "./Activity.js";
  import { get_activity_app_options } from "./ActivityApp.js";
  import { get_check_count_options } from "./CheckCount.js";
  import { get_check_count_time_options } from "./CheckCountTime.js";
  import axios from "axios";
  import { onMount } from "svelte";

  let days = null;
  let data_loaded = false;

  let activity = {};
  let activity_chart;
  let activity_options;

  let activity_by_app_chart;
  let activity_by_app_options;

  let check_count_chart;
  let check_count_options;

  let check_count_time_chart;
  let check_count_time_options;

  function last_n_dates(dates, n_dates) {
    const currentYear = new Date().getFullYear();
    const datesWithYear = dates.map(date => date + '/' + currentYear);
    const dateObjects = datesWithYear.map((dateString) => new Date(dateString));
    dateObjects.sort((a, b) => b - a);
    const result_dates = dateObjects.slice(0, n_dates);
    const result_dates_strings = result_dates.map((date) => {
      const day = String(date.getDate()).padStart(2, "0");
      const month = String(date.getMonth() + 1).padStart(2, "0");
      return `${month}/${day}`;
    });
    return result_dates_strings;
  }

  function specific_day(event) {
    let value_update = event.target.value;
    let new_data = [
      {
        name: value_update,
        data: activity[value_update]["duration"],
      },
    ];
    activity_chart.updateSeries(new_data);
  }

  function batch_days(event) {
    let value_update = parseInt(event.target.value);
    let new_data = [];

    let dates = last_n_dates(days, value_update);

    dates.forEach((day) => {
      new_data.push({
        data: activity[day]["duration"],
        name: day,
      });
    });
    activity_chart.updateSeries(new_data);
  }

  onMount(async () => {
    try {
    const response = await axios.get("/exporter");
    const {
        activity,
        activity_by_app,
        check_count,
    } = response.data;

    activity_options = get_activity_options(activity);
    days = Object.keys(activity);
    activity_by_app_options = get_activity_app_options(activity_by_app);
    check_count_options = get_check_count_options(check_count);
    check_count_time_options = get_check_count_time_options(check_count);

    data_loaded = true;
} catch (error) {
    console.error("Error:", error);
}


    const ApexCharts = (await import("apexcharts")).default;

    activity_chart = new ApexCharts(activity_chart, activity_options);
    activity_by_app_chart = new ApexCharts(
      activity_by_app_chart,
      activity_by_app_options
    );
    check_count_chart = new ApexCharts(check_count_chart, check_count_options);
    check_count_time_chart = new ApexCharts(check_count_time_chart, check_count_time_options);

    activity_by_app_chart.render();
    activity_chart.render();
    check_count_chart.render();
    check_count_time_chart.render();
  });
</script>

<Body
  style=" display: block;background-color: #ffffff;font-family: Arial, Helvetica, sans-serif;color:black;margin: 0;padding: 0;"
/>

<div id="wrapper">
  <div class="chart" id="mainchart" bind:this={activity_chart} />
  <div class="chart" id="maincharthandles">
    {#if data_loaded}
      <p>Choose a specific day</p>
      <select on:change={specific_day}>
        {#each days as day}
          <option value={day}>{day}</option>
        {/each}
      </select>
      <p>Or get the last</p>
      <input min="1" max="11" type="number" on:change={batch_days} />
      <p>Days</p>
    {/if}
  </div>
  <div class="chart" id="bigchart" bind:this={activity_by_app_chart} />
  <div class="chart"  id="smallchart1" bind:this={check_count_chart}/>
  <div class="chart" id="smallchart2" bind:this={check_count_time_chart}/>
</div>

<style>
  .chart {
    padding: 0.5rem;
    background: rgba(255, 251, 251, 0.05);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    backdrop-filter: blur(4.5px);
    -webkit-backdrop-filter: blur(4.5px);
    border-radius: 10px;
  }
  #wrapper {
    padding: 1rem;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(3, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    gap: 1rem;
  }

  #mainchart {
    grid-area: 1 / 1 / 2 / 4;
  }
  #maincharthandles {
    grid-area: 1 / 4 / 2 / 5;
    display: flex;
    flex-direction: column;
  }
  #bigchart {
    grid-area: 2 / 1 / 3 / 5;
    padding-bottom: 0;
    height: 100%;
  }
  #smallchart1 {
    grid-area: 3 / 1 / 4 / 3;
  }
  #smallchart2 {
    grid-area: 3 / 3 / 4 / 5;
  }
  select{
    text-align: center;
  }
  input {
    border: none;
    border-bottom: 1px solid green;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
  }
  input:focus {
    outline: none;
  }
  p {
    font-weight: bold;
    text-align: center;
    
  }
</style>
