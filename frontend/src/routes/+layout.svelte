<script>

  import { fly } from 'svelte/transition'


export let data
</script>


<nav id="navbar">
    <a href="/"><img class="navicon" alt='dummy text' src="navbaricons/home.png"></a>
    <a href="/retrocrypto"><img class="navicon" alt='dummy text' src="navbaricons/retrocrypto.png"></a>
    <a href="/retrocrypto">selftrack</a>
  </nav>
  {#key data.url}
  <div
    in:fly={{ x: -200, duration: 300, delay: 300 }}
    out:fly={{ x: 200, duration: 300 }}
  >
    <slot />
  </div>
  
{/key}

  <style>
      #navbar{
    background-color:#7F5AF0;
    width: 100%;
    height: 100px;
    border-radius: 51% 49% 48% 52% / 0% 0% 100% 100% ;
    display:flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    font-weight: bolder;
    gap:5px;

  }
  a{
    color:white;
    text-decoration: none;
  }
  .navicon:hover{
    transform: scale(1.2);
    transition: all 0.5s;
  }
  </style>