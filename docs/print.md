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

# Prints

## JDDEM-jaargang-14-18460531

<div id="example1">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/JDDEM-jaargang-14-18460531.jpg' relativePathOutputFolder='output/JDDEM-jaargang-14-18460531' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('example1')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/> 

<details>
  <summary>Details</summary>
  <p>

<!-- Input Image: 480x320 pixels -->

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/JDDEM-jaargang-14-18460531.jpg)

Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/JDDEM-jaargang-14-18460531)


</p>
</details>  
 
## LAMODU-jaargang-23-18990201

<div id="example2">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/LAMODU-jaargang-23-18990201.jpg' relativePathOutputFolder='output/LAMODU-jaargang-23-18990201' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('example2')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/> 

<details>
  <summary>Details</summary>
  <p>

<!-- Input Image: 480x320 pixels -->

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/LAMODU-jaargang-23-18990201.jpg)

Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/LAMODU-jaargang-23-18990201)
</p>
</details>  

