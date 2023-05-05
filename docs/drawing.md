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

## europeana_fashion_t00000380_006

<div id="examplea">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_t00000380_006.jpg' relativePathOutputFolder='output/europeana_fashion_t00000380_006' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('examplea')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
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

<div id="exampleb">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_t00000014_003.jpg' relativePathOutputFolder='output/europeana_fashion_t00000014_003' />
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('exampleb')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
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

## europeana_fashion_83319_2.jpg

<div id="example1">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_83319_2.jpg' relativePathOutputFolder='output/europeana_fashion_83319_2' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example1')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_83319_2.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_83319_2)
</p>
</details>

## europeana_fashion_22218.jpg

<div id="example2">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_22218.jpg' relativePathOutputFolder='output/europeana_fashion_22218' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example2')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_22218.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_22218)
</p>
</details>

## 2048215_europeana_fashion_http___ceres_mcu_es_pages_Main_idt_165325_inventary_FD041300_table_FDOC_museum_MT.jpg

<div id="example3">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/2048215_europeana_fashion_http___ceres_mcu_es_pages_Main_idt_165325_inventary_FD041300_table_FDOC_museum_MT.jpg' relativePathOutputFolder='output/2048215_europeana_fashion_http___ceres_mcu_es_pages_Main_idt_165325_inventary_FD041300_table_FDOC_museum_MT' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example3')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/2048215_europeana_fashion_http___ceres_mcu_es_pages_Main_idt_165325_inventary_FD041300_table_FDOC_museum_MT.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/2048215_europeana_fashion_http___ceres_mcu_es_pages_Main_idt_165325_inventary_FD041300_table_FDOC_museum_MT)
</p>
</details>

## europeana_fashion_24551.jpg

<div id="example4">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_24551.jpg' relativePathOutputFolder='output/europeana_fashion_24551' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example4')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_24551.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_24551)
</p>
</details>

## europeana_fashion_24894_15.jpg

<div id="example5">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_24894_15.jpg' relativePathOutputFolder='output/europeana_fashion_24894_15' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example5')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_24894_15.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_24894_15)
</p>
</details>

## europeana_fashion_83319_26.jpg

<div id="example6">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_83319_26.jpg' relativePathOutputFolder='output/europeana_fashion_83319_26' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example6')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_83319_26.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_83319_26)
</p>
</details>

## europeana_fashion_NMA_0068953.jpg

<div id="example7">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_NMA_0068953.jpg' relativePathOutputFolder='output/europeana_fashion_NMA_0068953' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example7')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_NMA_0068953.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_NMA_0068953)
</p>
</details>

## europeana_fashion_t003997_000.jpg

<div id="example8">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_t003997_000.jpg' relativePathOutputFolder='output/europeana_fashion_t003997_000' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example8')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_t003997_000.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_t003997_000)
</p>
</details>

## europeana_fashion_334.jpg

<div id="example9">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_334.jpg' relativePathOutputFolder='output/europeana_fashion_334' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example9')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_334.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_334)
</p>
</details>

## europeana_fashion_83318_5.jpg

<div id="example10">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_83318_5.jpg' relativePathOutputFolder='output/europeana_fashion_83318_5' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example10')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_83318_5.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_83318_5)
</p>
</details>

## europeana_fashion_65965_28.jpg

<div id="example11">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_65965_28.jpg' relativePathOutputFolder='output/europeana_fashion_65965_28' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example11')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_65965_28.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_65965_28)
</p>
</details>

## europeana_fashion_83319_3.jpg

<div id="example12">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_83319_3.jpg' relativePathOutputFolder='output/europeana_fashion_83319_3' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example12')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_83319_3.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_83319_3)
</p>
</details>

## europeana_fashion_t00000014_003.jpg

<div id="example13">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_t00000014_003.jpg' relativePathOutputFolder='output/europeana_fashion_t00000014_003' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example13')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_t00000014_003.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_t00000014_003)
</p>
</details>

## europeana_fashion_t00000007_004.jpg

<div id="example14">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_t00000007_004.jpg' relativePathOutputFolder='output/europeana_fashion_t00000007_004' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example14')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_t00000007_004.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_t00000007_004)
</p>
</details>

## europeana_fashion_2009_14_0172.jpg

<div id="example15">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_2009_14_0172.jpg' relativePathOutputFolder='output/europeana_fashion_2009_14_0172' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example15')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_2009_14_0172.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_2009_14_0172)
</p>
</details>

## europeana_fashion_KD_1948_110_23.jpg

<div id="example16">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_KD_1948_110_23.jpg' relativePathOutputFolder='output/europeana_fashion_KD_1948_110_23' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example16')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_KD_1948_110_23.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_KD_1948_110_23)
</p>
</details>

## europeana_fashion_t00000380_006.jpg

<div id="example17">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_t00000380_006.jpg' relativePathOutputFolder='output/europeana_fashion_t00000380_006' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example17')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_t00000380_006.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_t00000380_006)
</p>
</details>

## europeana_fashion_65965_22.jpg

<div id="example18">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_65965_22.jpg' relativePathOutputFolder='output/europeana_fashion_65965_22' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example18')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_65965_22.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_65965_22)
</p>
</details>

## europeana_fashion_18131_002.jpg

<div id="example19">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_18131_002.jpg' relativePathOutputFolder='output/europeana_fashion_18131_002' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example19')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_18131_002.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_18131_002)
</p>
</details>

## europeana_fashion_20293_2_L.jpg

<div id="example20">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/ksismanis/upscale/main/sources/input/europeana_fashion_20293_2_L.jpg' relativePathOutputFolder='output/europeana_fashion_20293_2_L' />
</div>
 <button v-if="fullscreenEnabled" @click="enterFullscreen('example20')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/> 
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>
<br/>
<details>
<summary>Details</summary>
<p>

Input Image: [Image](https://github.com/ksismanis/upscale/blob/main/sources/input/europeana_fashion_20293_2_L.jpg)
Output Images: [Github Folder](https://github.com/ksismanis/upscale/tree/main/sources/output/europeana_fashion_20293_2_L)
</p>
</details>



### Voting

<div class="strawpoll-embed" id="strawpoll_GPgV6RX44ga" style="height: 600px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;">
<iframe title="StrawPoll Embed" id="strawpoll_iframe_QrgeVNGxOZp" src="https://strawpoll.com/embed/polls/GPgV6RX44ga" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe>
<!-- <script async src="https://cdn.strawpoll.com/dist/widgets.js" charset="utf-8"></script> -->
</div>
<br/>
