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

# Color Photos

## 1997.16.0021

<div id="examplea">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/1997.16.0021.jpg' relativePathOutputFolder='output/1997.16.0021' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('examplea')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/> 

<details>
  <summary>Details</summary>
  <p>

<!-- Input Image: 480x320 pixels -->

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/1997.16.0021.jpg)

Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/1997.16.0021)


</p>
</details>  
 
## 2004.16.0006

<div id="exampleb">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2004.16.0006.jpg' relativePathOutputFolder='output/2004.16.0006' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('exampleb')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/> 

<details>
  <summary>Details</summary>
  <p>

<!-- Input Image: 480x320 pixels -->

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2004.16.0006.jpg)

Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2004.16.0006)
</p>
</details>  


## 18477R.jpg

<div id="example1">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/18477R.jpg' relativePathOutputFolder='output/18477R' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example1')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/18477R.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/18477R)
</p>
</details>

## 2004.16.0006.jpg

<div id="example2">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2004.16.0006.jpg' relativePathOutputFolder='output/2004.16.0006' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example2')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2004.16.0006.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2004.16.0006)
</p>
</details>

## 18124R.jpg

<div id="example3">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/18124R.jpg' relativePathOutputFolder='output/18124R' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example3')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/18124R.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/18124R)
</p>
</details>

## 49058.jpg

<div id="example4">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/49058.jpg' relativePathOutputFolder='output/49058' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example4')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/49058.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/49058)
</p>
</details>

## 34988.jpg

<div id="example5">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/34988.jpg' relativePathOutputFolder='output/34988' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example5')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/34988.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/34988)
</p>
</details>

## 15949R.jpg

<div id="example6">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/15949R.jpg' relativePathOutputFolder='output/15949R' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example6')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/15949R.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/15949R)
</p>
</details>

## MG8527.jpg

<div id="example7">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/MG8527.jpg' relativePathOutputFolder='output/MG8527' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example7')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/MG8527.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/MG8527)
</p>
</details>

## 34722.jpg

<div id="example8">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/34722.jpg' relativePathOutputFolder='output/34722' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example8')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/34722.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/34722)
</p>
</details>

## MG8938.jpg

<div id="example9">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/MG8938.jpg' relativePathOutputFolder='output/MG8938' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example9')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/MG8938.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/MG8938)
</p>
</details>

## 2001.16.0030.jpg

<div id="example10">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2001.16.0030.jpg' relativePathOutputFolder='output/2001.16.0030' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example10')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2001.16.0030.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2001.16.0030)
</p>
</details>

## T1993-293A_01.jpg

<div id="example11">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/T1993-293A_01.jpg' relativePathOutputFolder='output/T1993-293A_01' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example11')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/T1993-293A_01.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/T1993-293A_01)
</p>
</details>

## 36313.jpg

<div id="example12">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/36313.jpg' relativePathOutputFolder='output/36313' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example12')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/36313.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/36313)
</p>
</details>

## 16525R.jpg

<div id="example13">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/16525R.jpg' relativePathOutputFolder='output/16525R' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example13')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/16525R.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/16525R)
</p>
</details>

## MG4202.jpg

<div id="example14">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/MG4202.jpg' relativePathOutputFolder='output/MG4202' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example14')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/MG4202.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/MG4202)
</p>
</details>

## MG811.jpg

<div id="example15">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/MG811.jpg' relativePathOutputFolder='output/MG811' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example15')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/MG811.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/MG811)
</p>
</details>

## 30235.jpg

<div id="example16">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/30235.jpg' relativePathOutputFolder='output/30235' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example16')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/30235.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/30235)
</p>
</details>

## 17229R.jpg

<div id="example17">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/17229R.jpg' relativePathOutputFolder='output/17229R' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example17')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/17229R.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/17229R)
</p>
</details>

## 1997.16.0021.jpg

<div id="example18">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/1997.16.0021.jpg' relativePathOutputFolder='output/1997.16.0021' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example18')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/1997.16.0021.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/1997.16.0021)
</p>
</details>

## 52838.jpg

<div id="example19">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/52838.jpg' relativePathOutputFolder='output/52838' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example19')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/52838.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/52838)
</p>
</details>

## 2005.16.0006.jpg

<div id="example20">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0006.jpg' relativePathOutputFolder='output/2005.16.0006' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example20')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0006.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0006)
</p>
</details>



### Voting

<div class="strawpoll-embed" id="strawpoll_kjn18vwq0yQ" style="height: 600px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;">
<iframe title="StrawPoll Embed" id="strawpoll_iframe_kjn18vwq0yQ" src="https://strawpoll.com/embed/polls/kjn18vwq0yQ" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe>
<!-- <script async src="https://cdn.strawpoll.com/dist/widgets.js" charset="utf-8"></script> -->
</div>
<br/>
