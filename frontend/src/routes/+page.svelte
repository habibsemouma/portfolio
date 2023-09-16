
<script>
  import { writable } from 'svelte/store';
  import { fade } from 'svelte/transition';
  import {Body} from 'svelte-body'

  let titles = ['Python developer', 'Web developer', 'Networks and telecommunications graduate'];
  let count = 0;
  let title = titles[count];

  const interval = setInterval(() => {
    count = (count + 1) % 3;
    title = titles[count];

  }, 2000);

  const titleStore = writable(title);

  $: {
    titleStore.set(title);
  }
</script>

<head>
    <meta charset="UTF-8">
    <title>Home</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

</head>
<Body class="bg-slate-800" />

<div class="bg-slate-800 text-white h-full w-full">

    <div class="p-28 flex flex-col gap-4 justify-center items-center">
        <h1 class=" text-2xl font-bold border-purple-800 p-4 border-b-2">Habib</h1>
        {#key count}
        <p in:fade={{delay:0,duration:2000}} class="text-lg font-bold transition-opacity " id="rotating-text"> {title}</p>
        {/key}
      </div>

    <div class="p-28 flex items-start justify-center">
        <button id="scrollButton" class=" p-4 rounded-sm border-2 transition-all border-green-700 hover:bg-green-700">Get started</button>
    </div>

    <div class="bg-[#1A1A1A] gap-16 flex flex-col items-center justify-cente p-16">

        <h1 class="font-bold text-lg">WHAT I DO</h1>

        <div class="grid grid-cols-2 gap-10 w-full">

            <div class="flex items-center justify-center">
                <img alt="dummy text" class="border-2 rounded-full p-2 hover:bg-purple-700"
                    src="images/network.png">
            </div>
            <div class="flex items-center justify-center">
                <h1>Networking</h1>
            </div>

            <div class="flex items-center justify-center">
                <img alt="dummy text" class="border-2 rounded-full p-2 hover:bg-purple-700"
                    src="images/dev.png">

            </div>

            <div class="flex items-center justify-center">
                <h1>Web dev</h1>
            </div>


            <div class="flex items-center justify-center">
                <img alt="dummy text" class="border-2 rounded-full p-2 hover:bg-purple-700"
                    src="images/scraping.png">

            </div>

            <div class="flex items-center justify-center">
                <h1>Web scraping</h1>
            </div>


        </div>

    </div>
    

    <div class="bg-[#1A1A1A] gap-16 flex flex-col items-center justify-center p-16">
        <h1 class="font-bold text-lg">TECH STACK</h1>
        <div class="grid grid-cols-5 gap-8">
            <img alt="dummy text" class="shadow-[0_20px_50px_rgba(255,_255,_255,_0.2)] bg-white rounded-full " src="images/techstack/python.png">
            <img alt="dummy text" class="shadow-[0_20px_50px_rgba(255,_255,_255,_0.2)] bg-white rounded-full " src="images/techstack/selenium.png">
            <img alt="dummy text" class="shadow-[0_20px_50px_rgba(255,_255,_255,_0.2)] bg-white rounded-full " src="images/techstack/pandas.png">
            <img alt="dummy text" class="shadow-[0_20px_50px_rgba(255,_255,_255,_0.2)] bg-white rounded-full " src="images/techstack/tensorflow.png">
            <img alt="dummy text" class="shadow-[0_20px_50px_rgba(255,_255,_255,_0.2)] bg-white rounded-full " src="images/techstack/git.png">
            
            <img alt="dummy text" class="shadow-[0_20px_50px_rgba(255,_255,_255,_0.2)] bg-white rounded-full " src="images/techstack/html.png">
            <img alt="dummy text" class="shadow-[0_20px_50px_rgba(255,_255,_255,_0.2)] bg-white rounded-full " src="images/techstack/js.png">
            <img alt="dummy text" class="shadow-[0_20px_50px_rgba(255,_255,_255,_0.2)] bg-white rounded-full " src="images/techstack/css.png">
            <img alt="dummy text" class="shadow-[0_20px_50px_rgba(255,_255,_255,_0.2)] bg-white rounded-full " src="images/techstack/svelte.png">
            <img alt="dummy text" class="shadow-[0_20px_50px_rgba(255,_255,_255,_0.2)] bg-white rounded-full " src="images/techstack/docker.png">

        </div>

    </div>

    <div class="bg-slate-800] gap-16 flex flex-col items-center justify-center p-16">
        <h1 class="font-bold text-lg">EDUCATION</h1>
        <div class="flex flex-col items-center justify-center gap-8">
            <img alt="dummy text" class=" bg-white rounded-full " src="images/education/usto.jpeg">
            <h1 class="text-lg font-semibold">Bachelor degree, Telecommunications 2018-2021</h1>
            <h1 class="text-lg font-semibold">Master degree, Networks and Telecommunications 2021-2023</h1>
        </div>

    </div>


    <div class="bg-[#1A1A1A] gap-16 flex flex-col items-center justify-center p-16">
        <h1 class="font-bold text-lg">CONTACT</h1>
        <div class="grid grid-cols-2 gap-8">
            <i class="fa fa-envelope"><a href="mailto:habibsemouma@gmail.com"> habibsemouma@gmail.com</a> </i>
            <i class="fa fa-phone"><a href="tel:+213557369874"> +213557369874</a></i>
            <i class="fa fa-linkedin"><a href="https://www.linkedin.com/in/habib-semouma-0502b1177"> Linkedin Profile</a></i>
            <i class="fa fa-github"><a href="https://github.com/habibsemouma"> Github link</a></i>

        </div>

    </div>

</div>
<style>
  @tailwind base;
@tailwind components;
@tailwind utilities;

</style>