<script>
  import { Body } from "svelte-body";
  let file_ready=false;
  let file_url=undefined;
  let error_produced=false;

  async function get_mp3() {
    document.getElementById("dl_button").disabled=true;
    const url = document.getElementById("url").value;
    const data = { url: url };
    const response = await fetch("http://ytbmp3/audio", {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (response.ok){
      const blob= await response.blob();
      const url=URL.createObjectURL(blob);
      file_url=url;
      file_ready=true;
    }else{error_produced=true}
  }
  function start_dl(filePath){
    const downloadLink = document.createElement('a');
    downloadLink.href = filePath;
    downloadLink.download = 'audio.mp3';
    downloadLink.click();
    document.getElementById("dl_button").disabled=false;
  }
</script>

<Body
  style="color:white; background-color: #232946; margin: 0;font-family: Arial, Helvetica, sans-serif;display: flex;flex-direction: column;justify-content: center;align-items: center;gap:50px;"
/>
<div id="main-wrap">
  <h1>Youtube to mp3</h1>
  {#if error_produced}
  <h3>There was an error please check the provided url or try again later</h3>
  {/if}
  <input id="url" placeholder="video url" />
  <button id="dl_button" on:click={() => get_mp3()}>Convert</button>
  {#if file_ready}
  <button on:click={() =>start_dl(file_url)}>Download audio</button>
  {/if}
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
  button:hover{
    cursor: pointer;
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
