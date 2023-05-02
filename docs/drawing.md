---
title: Print Examples
description: Visual Comparison of Multiple Models
layout: doc
outline: [2, 4]
---

<script setup lang="ts">
import ImageSliderGithub from './components/imageslidergithub.vue' // the vue image slider example comparison component

//HTML5 Fullscreen API
const fullscreenEnabled = document.fullscreenEnabled; //check if fullscreen is possible
function enterFullscreen(elementName) {
  var element = document.getElementById(elementName);
  if(element.requestFullscreen) {
    element.requestFullscreen();
  } else if(element.msRequestFullscreen) {      // for IE11 (remove June 15, 2022)
    element.msRequestFullscreen();
  } else if(element.webkitRequestFullscreen) {  // iOS Safari
    element.webkitRequestFullscreen();
  }
}

// reset button, to keep it simple this will reset all examples. This is simply because when entering fullscreen mode, dragging/moving the image out of view, and pressing esc, the image will have 'vanished' (not in view anymore) so i thought id add a reset button
import { ref } from 'vue';
const componentKey = ref(0);

const forceRerender = () => {
  componentKey.value += 1;
};
</script>

# Drawings

## Jeuropeana_fashion_t00000380_006

<div id="example1">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_t00000380_006.jpg' relativePathOutputFolder='output/europeana_fashion_t00000380_006' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('example1')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/> 

<details>
  <summary>Details</summary>
  <p>

<!-- Input Image: 480x320 pixels -->

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_t00000380_006.jpg)

Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_t00000380_006)


</p>
</details>  
 
## europeana_fashion_t00000014_003

<div id="example2">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_t00000014_003.jpg' relativePathOutputFolder='output/europeana_fashion_t00000014_003' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('example2')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/> 

<details>
  <summary>Details</summary>
  <p>

<!-- Input Image: 480x320 pixels -->

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_t00000014_003.jpg)

Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_t00000014_003)
</p>
</details>  


### Voting

<div class="strawpoll-embed" id="strawpoll_QrgeVNGxOZp" style="height: 600px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;">
<iframe title="StrawPoll Embed" id="strawpoll_iframe_QrgeVNGxOZp" src="https://strawpoll.com/embed/polls/05ZdWq9Q4g6" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe>
<!-- <script async src="https://cdn.strawpoll.com/dist/widgets.js" charset="utf-8"></script> -->
</div>
<br/>

<!-- <div class="strawpoll-embed" id="strawpoll_05ZdWq9Q4g6" style="height: 644px; max-width: 640px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;"><iframe title="StrawPoll Embed" id="strawpoll_iframe_05ZdWq9Q4g6" src="https://strawpoll.com/embed/polls/05ZdWq9Q4g6" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe><script async src="https://cdn.strawpoll.com/dist/widgets.js" charset="utf-8"></script></div> -->