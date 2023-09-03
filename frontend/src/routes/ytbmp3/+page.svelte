<script>
  import { Body } from "svelte-body";
  async function get_mp3() {
    const url = document.getElementById("url").value;
    const data = { url: url };
    const response = await fetch("http://127.0.0.1:5000/audio", {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    });
  }
</script>

<Body
  style="color:white; background-color: #232946; margin: 0;font-family: Arial, Helvetica, sans-serif;display: flex;flex-direction: column;justify-content: center;align-items: center;gap:50px;"
/>
<div id="main-wrap">
  <h1>Youtube to mp3</h1>
  <input id="url" placeholder="video url" />
  <button on:click={() => get_mp3()}>Convert</button>
</div>

<style>
  input {
    border: none;
    border-bottom: 2px solid #7f5af0;
    font-size: 24px;
    color: white;
    background-color: #232946;
  }
  input:focus {
    outline: none;
  }
  button {
    color: white;
    background-color: #7f5af0;
    border: none;
    padding: 20px;
    border-radius: 50px;
    font-weight: bold;
  }
  h1 {
    display: block;
    font-size: 2em;
    margin-top: 0.67em;
    margin-bottom: 0.67em;
    margin-left: 0;
    margin-right: 0;
    font-weight: bold;
  }
  #main-wrap {
    display: flex;
    flex-direction: column;
    gap: 100px;
  }
</style>
