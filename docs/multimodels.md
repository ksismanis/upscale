---
title: Multi Models
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

# Multiple Models

<!-- If you want the filterable version of this page where you can type and search for specific models then head on to the [filterable models page](./multimodelsfilterable.md), be aware that it takes a while to load so you need to be patient.

This page contains the full examples of images that have been upscaled with multiple different models for you to visually compare the outputs of these models against each other. If you would like to see a smaller selection, head on over to my [favorites page](./favorites.md).

Here I demonstrate how I was comparing different model outputs with each other, it features my oldest example which included only around 20 universal upscaling models. The examples on this page are newer and now contain some 300+ outputs in comparison.

<iframe width="100%" height="315" src="https://www.youtube.com/embed/0TYRDmQ5LZk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->

## Examples

These examples feature 300+ model ouputs and display all of my generated output from the respective github folder. Bear in mind that some of these models serve a different purpose than upscaling, like for example some 1x denoising models. You find the links to the input image and all the generated outputs in the 'Details' Section beneath each example, in case you wanted to do your own upscaling comparison.

> Example Controls: Left mouse button to drag the image or to move the slider, mouse wheel to zoom in, right mouse button to toggle left model on/off, releasing middle mouse button will activate a short flicker test for the left side of the slider. Do not work on mobile.

### Photo

<br/>

<!-- #### Lala

<div id="lalaExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/lala.jpg' relativePathOutputFolder='output/lala' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('lalaExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/> 

<details>
  <summary>Details</summary>
  <p>

Input Image: 480x320 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/photos/buddy.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/photos/buddy)

  </p>
</details>   -->

 #### Lala

<div id="lalaExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/lala.jpg' relativePathOutputFolder='output/lala' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('lalaExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/> 

<details>
  <summary>Details</summary>
  <p>

Input Image: 480x320 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/photos/buddy.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/photos/buddy)

  </p>
</details>  





<!-- 
#### Buddy

<div id="buddyExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/photos/buddy.jpg' relativePathOutputFolder='output/lossless/photos/buddy' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('buddyExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 480x320 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/photos/buddy.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/photos/buddy)

  </p>
</details>

#### Grosser Mythen

<div id="mythenExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/photos/grossermythen.jpg' relativePathOutputFolder='output/lossless/photos/grossermythen' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('mythenExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 427x320 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/photos/grossermythen.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/photos/grossermythen)

  </p>
</details>
 -->

