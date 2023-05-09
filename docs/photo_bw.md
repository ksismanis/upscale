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

# BW Photos
  

## 2005.16.0140.jpg

<div id="example1">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0140.jpg' relativePathOutputFolder='output/2005.16.0140' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example1')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0140.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0140)
</p>
</details>

## 2005.16.0110.jpg

<div id="example2">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0110.jpg' relativePathOutputFolder='output/2005.16.0110' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example2')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0110.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0110)
</p>
</details>

## 2005.16.0084.jpg

<div id="example3">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0084.jpg' relativePathOutputFolder='output/2005.16.0084' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example3')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0084.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0084)
</p>
</details>

## 2005.16.0037.jpg

<div id="example4">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0037.jpg' relativePathOutputFolder='output/2005.16.0037' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example4')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0037.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0037)
</p>
</details>

## 2005.16.0022.jpg

<div id="example5">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0022.jpg' relativePathOutputFolder='output/2005.16.0022' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example5')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0022.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0022)
</p>
</details>

## 2005.16.0147.jpg

<div id="example6">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0147.jpg' relativePathOutputFolder='output/2005.16.0147' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example6')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0147.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0147)
</p>
</details>

## 2005.16.0105.jpg

<div id="example7">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0105.jpg' relativePathOutputFolder='output/2005.16.0105' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example7')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0105.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0105)
</p>
</details>

## 2005.16.0049.jpg

<div id="example8">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0049.jpg' relativePathOutputFolder='output/2005.16.0049' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example8')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0049.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0049)
</p>
</details>

## 2002.16.0009.jpg

<div id="example9">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2002.16.0009.jpg' relativePathOutputFolder='output/2002.16.0009' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example9')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2002.16.0009.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2002.16.0009)
</p>
</details>

## 2005.16.0123.jpg

<div id="example10">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0123.jpg' relativePathOutputFolder='output/2005.16.0123' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example10')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0123.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0123)
</p>
</details>

## 2005.16.0144.jpg

<div id="example11">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0144.jpg' relativePathOutputFolder='output/2005.16.0144' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example11')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0144.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0144)
</p>
</details>

## 2005.16.0129.jpg

<div id="example12">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0129.jpg' relativePathOutputFolder='output/2005.16.0129' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example12')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0129.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0129)
</p>
</details>

## 1994.16.0004.jpg

<div id="example13">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/1994.16.0004.jpg' relativePathOutputFolder='output/1994.16.0004' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example13')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/1994.16.0004.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/1994.16.0004)
</p>
</details>

## 2005.16.0042.jpg

<div id="example14">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0042.jpg' relativePathOutputFolder='output/2005.16.0042' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example14')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0042.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0042)
</p>
</details>

## 2005.16.0044.jpg

<div id="example15">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0044.jpg' relativePathOutputFolder='output/2005.16.0044' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example15')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0044.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0044)
</p>
</details>

## 2005.16.0035.jpg

<div id="example16">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0035.jpg' relativePathOutputFolder='output/2005.16.0035' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example16')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0035.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0035)
</p>
</details>

## 2005.16.0134.jpg

<div id="example17">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0134.jpg' relativePathOutputFolder='output/2005.16.0134' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example17')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0134.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0134)
</p>
</details>

## 2005.16.0083.jpg

<div id="example18">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0083.jpg' relativePathOutputFolder='output/2005.16.0083' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example18')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0083.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0083)
</p>
</details>

## 2005.16.0091.jpg

<div id="example19">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0091.jpg' relativePathOutputFolder='output/2005.16.0091' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example19')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0091.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0091)
</p>
</details>

## 2005.16.0191.jpg

<div id="example20">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0191.jpg' relativePathOutputFolder='output/2005.16.0191' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example20')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0191.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0191)
</p>
</details>

## 2005.16.0114.jpg

<div id="example21">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2005.16.0114.jpg' relativePathOutputFolder='output/2005.16.0114' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example21')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2005.16.0114.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2005.16.0114)
</p>
</details>

### Voting

<div class="strawpoll-embed" id="strawpoll_wAg3AEwRKy8" style="height: 600px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;">
<iframe title="StrawPoll Embed" id="strawpoll_iframe_wAg3AEwRKy8" src="https://strawpoll.com/embed/polls/wAg3AEwRKy8" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe>
<!-- <script async src="https://cdn.strawpoll.com/dist/widgets.js" charset="utf-8"></script> -->
</div>
<br/>
