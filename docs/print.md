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

<div id="examplea">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/JDDEM-jaargang-14-18460531.jpg' relativePathOutputFolder='output/JDDEM-jaargang-14-18460531' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('examplea')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
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

<div id="exampleb">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/LAMODU-jaargang-23-18990201.jpg' relativePathOutputFolder='output/LAMODU-jaargang-23-18990201' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('exampleb')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
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

## JDDEM-jaargang-04-18360910_small.jpg

<div id="example1">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/JDDEM-jaargang-04-18360910_small.jpg' relativePathOutputFolder='output/JDDEM-jaargang-04-18360910_small' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example1')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/JDDEM-jaargang-04-18360910_small.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/JDDEM-jaargang-04-18360910_small)
</p>
</details>

## LMI-jaargang-47-19060902.jpg

<div id="example2">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/LMI-jaargang-47-19060902.jpg' relativePathOutputFolder='output/LMI-jaargang-47-19060902' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example2')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/LMI-jaargang-47-19060902.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/LMI-jaargang-47-19060902)
</p>
</details>

## 1993.16.0005.jpg

<div id="example3">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/1993.16.0005.jpg' relativePathOutputFolder='output/1993.16.0005' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example3')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/1993.16.0005.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/1993.16.0005)
</p>
</details>

## 2006.16.0030.jpg

<div id="example4">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2006.16.0030.jpg' relativePathOutputFolder='output/2006.16.0030' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example4')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2006.16.0030.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2006.16.0030)
</p>
</details>

## 2005.16.0093.jpg

<div id="example5">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0093.jpg' relativePathOutputFolder='output/2005.16.0093' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example5')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0093.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0093)
</p>
</details>

## 1976.16.0003.jpg

<div id="example6">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/1976.16.0003.jpg' relativePathOutputFolder='output/1976.16.0003' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example6')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/1976.16.0003.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/1976.16.0003)
</p>
</details>

## LAMODU-jaargang-23-18990201.jpg

<div id="example7">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/LAMODU-jaargang-23-18990201.jpg' relativePathOutputFolder='output/LAMODU-jaargang-23-18990201' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example7')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/LAMODU-jaargang-23-18990201.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/LAMODU-jaargang-23-18990201)
</p>
</details>

## LAMODU-jaargang-22-18981101.jpg

<div id="example8">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/LAMODU-jaargang-22-18981101.jpg' relativePathOutputFolder='output/LAMODU-jaargang-22-18981101' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example8')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/LAMODU-jaargang-22-18981101.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/LAMODU-jaargang-22-18981101)
</p>
</details>

## 2006.16.0010.jpg

<div id="example9">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2006.16.0010.jpg' relativePathOutputFolder='output/2006.16.0010' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example9')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2006.16.0010.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2006.16.0010)
</p>
</details>

## LAMODU-jaargang-20-18960501.jpg

<div id="example10">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/LAMODU-jaargang-20-18960501.jpg' relativePathOutputFolder='output/LAMODU-jaargang-20-18960501' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example10')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/LAMODU-jaargang-20-18960501.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/LAMODU-jaargang-20-18960501)
</p>
</details>

## 2005.16.0296.jpg

<div id="example11">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0296.jpg' relativePathOutputFolder='output/2005.16.0296' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example11')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0296.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0296)
</p>
</details>

## JDDEM-jaargang-14-18460531.jpg

<div id="example12">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/JDDEM-jaargang-14-18460531.jpg' relativePathOutputFolder='output/JDDEM-jaargang-14-18460531' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example12')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/JDDEM-jaargang-14-18460531.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/JDDEM-jaargang-14-18460531)
</p>
</details>

## JDDEM-jaargang-04-18360710.jpg

<div id="example13">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/JDDEM-jaargang-04-18360710.jpg' relativePathOutputFolder='output/JDDEM-jaargang-04-18360710' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example13')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/JDDEM-jaargang-04-18360710.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/JDDEM-jaargang-04-18360710)
</p>
</details>

## LMI-jaargang-27-18861212.jpg

<div id="example14">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/LMI-jaargang-27-18861212.jpg' relativePathOutputFolder='output/LMI-jaargang-27-18861212' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example14')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/LMI-jaargang-27-18861212.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/LMI-jaargang-27-18861212)
</p>
</details>

## LMI-jaargang-47-19060812.jpg

<div id="example15">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/LMI-jaargang-47-19060812.jpg' relativePathOutputFolder='output/LMI-jaargang-47-19060812' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example15')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/LMI-jaargang-47-19060812.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/LMI-jaargang-47-19060812)
</p>
</details>

## 2005.16.0200.jpg

<div id="example16">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0200.jpg' relativePathOutputFolder='output/2005.16.0200' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example16')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0200.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0200)
</p>
</details>

## 2006.16.0039.jpg

<div id="example17">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2006.16.0039.jpg' relativePathOutputFolder='output/2006.16.0039' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example17')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2006.16.0039.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2006.16.0039)
</p>
</details>

## JDDEM-jaargang-15-18470101.jpg

<div id="example18">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/JDDEM-jaargang-15-18470101.jpg' relativePathOutputFolder='output/JDDEM-jaargang-15-18470101' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example18')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/JDDEM-jaargang-15-18470101.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/JDDEM-jaargang-15-18470101)
</p>
</details>

## 2006.16.0060.jpg

<div id="example19">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2006.16.0060.jpg' relativePathOutputFolder='output/2006.16.0060' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example19')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2006.16.0060.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2006.16.0060)
</p>
</details>

## JDDEM-jaargang-29-18611101.jpg

<div id="example20">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/JDDEM-jaargang-29-18611101.jpg' relativePathOutputFolder='output/JDDEM-jaargang-29-18611101' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example20')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/JDDEM-jaargang-29-18611101.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/JDDEM-jaargang-29-18611101)
</p>
</details>

### Voting

<div class="strawpoll-embed" id="strawpoll_NMnQ5VRKwn6" style="height: 600px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;">
<iframe title="StrawPoll Embed" id="strawpoll_iframe_NMnQ5VRKwn6" src="https://strawpoll.com/embed/polls/NMnQ5VRKwn6" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe>
<!-- <script async src="https://cdn.strawpoll.com/dist/widgets.js" charset="utf-8"></script> -->
</div>
<br/>