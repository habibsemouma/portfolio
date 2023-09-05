<script>
  import {Body} from 'svelte-body'
    export let current_encoding = "Choose an encoding";
    export let output_text="";
  
    function change_encoding(encoding) {
      current_encoding = encoding;
    }
  
      async function send_data(data){
          const res = await fetch('http://localhost:4000/api/items', {
              method: 'POST',
              headers: {
            'Content-Type': 'application/json',
          },
              body: JSON.stringify(data)
          })
          
          const json = await res.json()
  
          output_text=json['text']
          
  
      }
    
  
    async function prepare_data(type) {
      let data={
          "text":document.getElementById('inptext').value,
          "encoding":current_encoding,
          "type":type
      }
      if ((current_encoding == "caesar")) {
          data['encodingtype']="caesar"
          data['shift']=document.getElementById("shift").value
      }
      if ((current_encoding == "atbash")) {
          data['encodingtype']="atbash"
      }
      if ((current_encoding == "railfence")) {
          data['encodingtype']="railfence"
          data['rails']=document.getElementById("rails").value
      }
      if ((current_encoding == "vigenere")) {
          data['encodingtype']="vigenere"
          data['keyword']=document.getElementById("keyword").value
      }
      console.log(data);
      send_data(data);
    }
  </script>
  
  <head />
 <Body style=" display: flex; flex-direction: column; justify-content: center;align-items: center;gap: 40px;background-color: #F2F4F6;font-family: Arial, Helvetica, sans-serif;color:black;margin: 0;padding: 0;" />
    <div>
      <h1>{current_encoding}</h1>
    </div>
  
    <div>
      <button
        on:click={() => {
          change_encoding("caesar");
        }}
        class="handle">Caesar</button
      >
      <button
        on:click={() => {
          change_encoding("atbash");
        }}
        class="handle">Atbash</button
      >
      <button
        on:click={() => {
          change_encoding("railfence");
        }}
        class="handle">Railfence</button
      >
      <button
        on:click={() => {
          change_encoding("vigenere");
        }}
        class="handle">Vigenere</button
      >
      <button class="handle"
        on:click={() => {
          prepare_data("encode");
        }}
        id="encodebtn">Encode</button
      >
      <button class="handle" on:click={() => {
          prepare_data("decode");
        }} id="decodebtn">Decode</button>
    </div>
  
    <div>
      {#if current_encoding == "Choose an encoding"}
        <p />
      {:else if current_encoding == "caesar"}
        <input id="shift" placeholder="Caesar shift" type="number" />
      {:else if current_encoding == "atbash"}
        <p />
      {:else if current_encoding == "railfence"}
        <input id="rails" placeholder="Rails" type="number" />
      {:else if current_encoding == "vigenere"}
        <input id="keyword" placeholder="Keyword" />
      {/if}
    </div>
  
    <div id="docs">
      <textarea placeholder="text goes here" class="textdisp" id="inptext" />
      <textarea readonly placeholder="result goes here" class="textdisp" id="outtext" value="{output_text}" />
    </div>
 
  
  <style>

 

    .textdisp{
      height: 500px;
      width: 300px;
      padding:10px;
      color:black;
      font-size: 24px;
      border: none;
      margin: 1rem;
      -webkit-box-shadow: 0px 2px 21px -6px rgba(0,0,0,0.75);
  -moz-box-shadow: 0px 2px 21px -6px rgba(0,0,0,0.75);
  box-shadow: 0px 2px 21px -6px rgba(0,0,0,0.75);
  
    }
    .textdisp:focus{
      outline: none;
    }
    .handle{
      background-color: #7f5af0;
      font-weight: bold;
      border:none;
      padding: 1rem;
      border-radius: 2rem;
      color:white;
    }
    .handle:hover{
      transform: translateY(-5px);
      cursor: pointer;
    }
    #encodebtn{
      background-color:#2cb67d;
    }
    #decodebtn{
      background-color: red;
    }
    input{
      color:black;
      border: none;
      border-bottom: 1px solid #2CB67D;
  background-color: #F2F4F6;
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 24px;
    }
    input:focus{
      outline: 0;
    }
    h1{
      display: block;
  font-size: 2em;
  margin-top: 0.67em;
  margin-bottom: 0.67em;
  margin-left: 0;
  margin-right: 0;
  font-weight: bold;
    }
  </style>
  