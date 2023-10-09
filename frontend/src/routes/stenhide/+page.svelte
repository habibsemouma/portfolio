<script>
  import { Body } from "svelte-body";
  import axios from "axios";
  import {SpinLine} from "svelte-loading-spinners"

  let backgroundImage_1,backgroundImage_2;
  let file_loaded_1 = false;
  let file_loaded_2 = false;
  let text, embed_image, extract_image,extract_text;
  let file_loading=false

  const handleDrop = (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    displayImage(file);
  };

  const handleFileInput = (event) => {
    const file = event.target.files[0];
    displayImage(file);
    file_loaded_1 = true;
  };

  function displayImage(file) {
    if (file && file.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.onload = (e) => {
        backgroundImage_1 = `url(${e.target.result})`;
      };
      reader.readAsDataURL(file);
    }
  }

  async function send_embed_data() {
    file_loading=true
    try {
      let formData = new FormData();

      formData.append("image", embed_image[0]);
      formData.append("type", "embed");
      formData.append("text", text);
      let response = await axios.post(
        "http://127.0.0.1:5000/stenhide",
        formData,
        {
          responseType: "blob",
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      console.log(response.data);

      let blob = response.data;
      let blobUrl = URL.createObjectURL(blob);
      let downloadLink = document.createElement("a");
      downloadLink.href = blobUrl;
      downloadLink.download = "payloaded.png";
      downloadLink.click();
      URL.revokeObjectURL(blobUrl);
    } catch (error) {
      console.log(error);
    }
    file_loading=false
  }

  async function send_extract_data() {
    file_loading=true
    try {
      let data = new FormData();
      data.append("image", extract_image[0]);
      data.append("type", "extract");
      let response = await axios.post("http://localhost:5000/stenhide", data, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      extract_text=response.data['plaintext']
    } catch (error) {
      console.log(error);
    }
    file_loading=false
  }
</script>

<Body
  style="background-color:#24292E; display: flex; flex-direction: column;gap:20px; justify-content: center;align-items: center;gap: 40px;font-family: Arial, Helvetica, sans-serif;color:black;margin: 0;padding: 0;"
/>

<div id="main-wrap">
  <h1>Upload an image and add a text to embed into the image</h1>

  <div
    role="button"
    aria-label="Image dropzone"
    class="dropzone"
    style="background-image: {backgroundImage_1};background-position:center;background-origin:content-box"
    on:dragover={(e) => e.preventDefault()}
    on:dragleave={() => {}}
    on:drop={handleDrop}
    tabindex="0"
  >
    <div style="display: {file_loaded_1 ? 'none' : 'block'};">
      <p>Drag and drop an image here or use button to browse</p>
      <input
        bind:files={embed_image}
        type="file"
        accept="image/*"
        on:change={handleFileInput}
      />
    </div>
  </div>

  <input
    bind:value={text}
    placeholder="text to embed"
    class="txtarea"
    type="text"
  />

  <button on:click={send_embed_data} class="databtn">Embed text</button>

  <div id="line" />
  {#if file_loading}
  <SpinLine />
  {/if}

  <h1>Upload an image to extract text from it</h1>

  <div
    role="button"
    aria-label="Image dropzone"
    class="dropzone"
    style="background-image: {backgroundImage_2};background-position:center;background-origin:content-box"
    on:dragover={(e) => e.preventDefault()}
    on:dragleave={() => {}}
    on:drop={handleDrop}
    tabindex="0"
  >
    <div style="display: {file_loaded_2 ? 'none' : 'block'};">
      <p>Drag and drop an image here or click to browse</p>
      <input
        bind:files={extract_image}
        type="file"
        accept="image/*"
        on:change={handleFileInput}
      />
    </div>
  </div>


  <button on:click={send_extract_data} class="databtn">extract text</button>
  <input readonly bind:value={extract_text} placeholder="Extracted text" class="txtarea" type="text" />

</div>

<style>
  h1 {
    color: white;
  }
  #main-wrap {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 25px;
    height: 100vh;
  }
  .dropzone {
    border-radius: 10px;
    padding: 20px;
    cursor: pointer;
    width: 200px;
    height: 200px;
    color: white;
    box-shadow: 1px -1px 14px 0px rgba(0, 0, 0, 0.75);
    -webkit-box-shadow: 1px -1px 14px 0px rgba(0, 0, 0, 0.75);
    -moz-box-shadow: 1px -1px 14px 0px rgba(0, 0, 0, 0.75);
  }
  .txtarea {
    background-color: #24292e;
    border: none;
    border-bottom: 1px solid orangered;
    color: white;
    font-size: 20px;
    text-align: center;
  }
  .txtarea:focus {
    outline: none;
  }
  #line {
    border-bottom: 1px solid green;
    margin-top: 10px;
    margin-bottom: 10px;
    width: 75%;
  }
  .databtn {
    font-size: 16px;
    color: white;
    font-weight: bold;
    border-radius: 20px;
    padding: 10px;
    background-color: orangered;
    border: none;
    cursor: pointer;
  }
</style>
