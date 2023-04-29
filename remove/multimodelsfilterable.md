---
title: Multi Models
description: Visual Comparison of Multiple Models
layout: doc
outline: [2, 4]
---

<script setup lang="ts">
import ImageSliderGithub from './components/imageslidergithubfilterable.vue' // the vue image slider example comparison component

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

This page contains the full examples of images that have been upscaled with multiple different models for you to visually compare the outputs of these models against each other. If you would like to see a smaller selection, head on over to my [favorites page](./favorites.md).

Here I demonstrate how I was comparing different model outputs with each other, it features my oldest example which included only around 20 universal upscaling models. The examples on this page are newer and now contain some 300+ outputs in comparison.

<iframe width="100%" height="315" src="https://www.youtube.com/embed/0TYRDmQ5LZk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Examples

These examples feature 300+ model ouputs and display all of my generated output from the respective github folder. Bear in mind that some of these models serve a different purpose than upscaling, like for example some 1x denoising models. You find the links to the input image and all the generated outputs in the 'Details' Section beneath each example, in case you wanted to do your own upscaling comparison.

> Example Controls: Left mouse button to drag the image or to move the slider, mouse wheel to zoom in, right mouse button to toggle left model on/off, releasing middle mouse button will activate a short flicker test for the left side of the slider. Do not work on mobile.

### Photo

<br/>

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

#### Painting

<div id="paintingExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/photos/painting.jpg'  relativePathOutputFolder='output/lossless/photos/painting'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('paintingExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 427x320 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/photos/painting.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/photos/painting)

  </p>
</details>

#### PC Build

<div id="pcbuildExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/photos/pcbuild.jpg'  relativePathOutputFolder='output/lossless/photos/pcbuild'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('pcbuildExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 427x320 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/photos/pcbuild.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/photos/pcbuild)

  </p>
</details>

#### Snowboard

<div id="snowboardExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/photos/snowboard.jpg'  relativePathOutputFolder='output/lossless/photos/snowboard'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('snowboardExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 427x320 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/photos/snowboard.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/photos/snowboard)

  </p>
</details>

### Anime

<br/>

#### Fate

<div id="fateExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/anime/FateStayNightUnlimitedBladeWorksOpening.jpg'  relativePathOutputFolder='output/lossless/anime/fate'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('fateExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 640x360 pixels (360p)

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/anime/FateStayNightUnlimitedBladeWorksOpening.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/anime/fate)

  </p>
</details>

#### KonoSuba

<div id="konosubaExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/anime/KonoSuba.jpg'  relativePathOutputFolder='output/lossless/anime/konosuba'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('konosubaExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 640x360 pixels (360p)

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/anime/KonoSuba.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/anime/konosuba)

  </p>
</details>

#### Overlord

<div id="overlordExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/anime/Overlord.jpg'  relativePathOutputFolder='output/lossless/anime/overlord'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('overlordExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 640x360 pixels (360p)

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/anime/Overlord.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/anime/overlord)

  </p>
</details>

#### Sword Art Online

<div id="sao1Example">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/anime/SwordArtOnline.jpg'  relativePathOutputFolder='output/lossless/anime/sao1'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('sao1Example')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 640x360 pixels (360p)

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/anime/SwordArtOnline.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/anime/sao1)

  </p>
</details>

### AI Generated

<br>

#### ColorJacket

<div id="colorjacketExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/colorJacket.png'  relativePathOutputFolder='output/lossless/generated/colorjacket'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('colorjacketExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 360x360 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/ai_generated/colorJacket.png)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/generated/colorjacket)

  </p>
</details>

#### Astronaut

<div id="astronautExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/astronaut.png'  relativePathOutputFolder='output/lossless/generated/astronaut'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('astronautExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 360x360 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/ai_generated/astronaut.png)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/generated/astronaut)

  </p>
</details>

#### Planet

<div id="planetExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/planet.png'  relativePathOutputFolder='output/lossless/generated/planet'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('planetExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 360x360 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/ai_generated/planet.png)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/generated/planet)

  </p>
</details>

#### Life

<div id="lifeExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/life.png'  relativePathOutputFolder='output/lossless/generated/life'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('lifeExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 360x360 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/ai_generated/life.png)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/generated/life)

  </p>
</details>

#### ColorScape

<div id="colorScapeExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/colorScape.png'  relativePathOutputFolder='output/lossless/generated/colorscape'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('colorScapeExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 360x360 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/ai_generated/colorScape.png)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/generated/colorscape)

  </p>
</details>

#### Door

<div id="doorExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/door.png'  relativePathOutputFolder='output/lossless/generated/door'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('doorExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 360x360 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/ai_generated/door.png)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/generated/door)

  </p>
</details>

#### CyberpunkRebel

<div id="cyberpunkrebelExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/cyberpunkRebel.png'  relativePathOutputFolder='output/lossless/generated/cyberpunkrebel'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('cyberpunkrebelExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 360x360 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/ai_generated/cyberpunkRebel.png)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/generated/cyberpunkrebel)

  </p>
</details>

#### UnderwaterPiano


<div id="underwaterpianoExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/underwaterPiano.png'  relativePathOutputFolder='output/lossless/generated/underwaterpiano'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('underwaterpianoExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 360x360 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/ai_generated/underwaterPiano.png)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/generated/underwaterpiano)

  </p>
</details>


#### YellowRoom

<div id="yellowroomExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/yellowRoom.png'  relativePathOutputFolder='output/lossless/generated/yellowroom'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('yellowroomExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 360x360 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/ai_generated/yellowRoom.png)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/generated/yellowroom)

  </p>
</details>

#### Livingroom

<div id="livingroomExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/livingroom.jpg'  relativePathOutputFolder='output/lossless/generated/livingroom'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('livingroomExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 320x320 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/blob/main/sources/input/ai_generated/livingroom.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/generated/livingroom)

  </p>
</details>

## Lossy

The output images beneath this point had been stored in the lossy jpg format (for faster example loads) and are, therefore, lossy. Everything above this point had been redone in lossless png. You can still use all the following examples. Since this is a visual comparison site, I just wanted to mark the compression happening after this point.

### Anime

<br/>

#### Sword Art Online 2

<div id="sao2Example">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/anime/SwordArtOnline2.jpg'  relativePathOutputFolder='multimodel/current/anime/sao2'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('sao2Example')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 640x360 pixels (360p)

Input Image: [Image](https://github.com/Phhofm/upscale/tree/sources/input/anime/SwordArtOnline2.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/sources/multimodel/current/anime/sao2)

  </p>
</details>

#### That Time I Got Reincarnated As A Slime

<div id="slimeExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/anime/ThatTimeIGotReincarnatedAsASlime.jpg'  relativePathOutputFolder='multimodel/current/anime/slime'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('slimeExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 640x360 pixels (360p)

Input Image: [Image](https://github.com/Phhofm/upscale/tree/sources/input/anime/ThatTimeIGotReincarnatedAsASlime.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/sources/multimodel/current/anime/slime)

</p>
</details>

### AI Generated

<br/>

#### Child

<div id="childExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/child.jpg'  relativePathOutputFolder='multimodel/current/ai_generated/child'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('childExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 320x320 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/tree/sources/input/ai_generated/child.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/sources/multimodel/current/ai_generated/child)

</p>
</details>

#### Landscape

<div id="landscapeExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/landscape.jpg'  relativePathOutputFolder='multimodel/current/ai_generated/landscape'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('landscapeExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 320x320 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/tree/sources/input/ai_generated/landscape.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/sources/multimodel/current/ai_generated/landscape)

</p>
</details>

#### Lightning

<div id="lightningExample">
<ImageSliderGithub :key="componentKey" inputImageURL='https://raw.githubusercontent.com/Phhofm/upscale/main/sources/input/ai_generated/lightning.jpg'  relativePathOutputFolder='multimodel/current/ai_generated/lightning'/>
</div>
<button v-if="fullscreenEnabled" @click="enterFullscreen('lightningExample')" style="color:mediumseagreen;"><strong>FULLSCREEN (Exit with ESC)</strong></button><br/>
<button v-if="fullscreenEnabled" @click="forceRerender()" style="color:mediumseagreen;"><strong>Reset examples</strong></button>  
<br/>

<details>
  <summary>Details</summary>
  <p>

Input Image: 320x320 pixels

Input Image: [Image](https://github.com/Phhofm/upscale/tree/sources/input/ai_generated/lightning.jpg)

Output Images: [Github Folder](https://github.com/Phhofm/upscale/tree/sources/multimodel/current/ai_generated/lightning)

</p>
</details>

## Sets

Older set-based approach. These examples had been created in imgsli before the existence of this website. Since created with imgsli, these examples are 'static', meaning they do not change. All created examples belonged to a Set, which is a specific list of upscaling models which all examples of that Set follow. They are ordered from newest (Set 5) to oldest (Set 1, my very first comparison I did, also featured in the youtube video at the top of this page). The progression can be seen from the first Set using 22 upscaling models (the universal ones) to 315 in Set 5.

For the examples above this point I used a vue component where I had added selectors which inputs are from a json file (since static page) which is created in the build step, which gets triggered with each commit on the main branch thorugh github actions. This means they are 'dynamic'. Instead of drag and dropping hundreds of images through the imgsli web interface to create a new examples, the images above are simply build from the github folder, and update themselves automatically if I add or remove an image file, which makes it simpler for me to add new models.

### Set 5

Creation Date Of Upscale Set: 01. Dec 2022

Added some new models like  
Real_HAT_GAN_SRx4 as released on the 24. Nov 2022 (last week as of me creating this entry)  
Swin2SR models released one month ago at the end of oct 2022  
FeMaSR which had been released in the second half of 2022.  
I try to list updates I make on the [changelog page](changelog.md)  
Added a voting feature where the community could vote on the best results for each example. My idea at that time had been to create a community page and feature the top 5 voted for models there.

<br/>

#### Buddy

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTM3MDAy/0/1" style="width: 100%; border: 0px none; height: 56vmin; min-height: 300px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>

<a href="https://imgsli.com/MTM3MDAy/0/1" target="_blank">Open in external tab</a>

##### Example Details

Name: Buddy
Creation Date: 01. Dec 2022  
 Input Image: 480x320 pixels  
 Scaling Factor: 4  
 Output Image: 1920x1280 pixels  
 Models used: 315  
 Input Source File: [Link](https://github.com/Phhofm/upscale/public/sources/input/photos)  
 Output Source Files: [Link](https://github.com/Phhofm/upscale/public/sources/multimodel/current/photos)

  <details>
    <summary>Models List</summary>

    001_classicalSR_DF2K_s64w8_SwinIR-M_x4
    001_classicalSR_DIV2K_s48w8_SwinIR-M_x4
    002_lightweightSR_DIV2K_s64w8_SwinIR-S_x4
    003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN
    003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN
    4x_1ch-Alpha-Lite_212000_G
    4x_AmericanDad2
    4x_Archerpolation_NXbrz
    4x_b_melozard_2_latest_G
    4x_BigFace_v3_Blend
    4x_BigFace_v3_Clear
    4x_BigFace_v3
    4x_BigFArt_Bang1
    4x_BigFArt_Base
    4x_BigFArt_Blend
    4x_BigFArt_Detail_300000_G
    4x_BigFArt_Fine
    4x_BMS_85000_G
    4x_BMS_jpg60_20000_G
    4x_BooruGan_600k
    4x_BooruGan_650k
    4x_BS_DevianceMIP_82000_G
    4x_BS_DevianceV2
    4x_BS_Mystery
    4x_BS_SbeveHarvey_62000_G
    4x_BS_Screenbooster_SPSR_88000G
    4x_BSRGAN_old_arch
    4x_BSRGAN
    4x_cat_patch_325000_G
    4x_comic_dataset_115k
    4x_Compact_Pretrain_traiNNer
    4x_Compact_Pretrain
    4x_CountryRoads_377000_G
    4x_DBMangaStand_255k GOOD
    4x_DeBLRFS
    4x_deindeo_x4_130000_G
    4x_Deviance_60000G
    4x_Deviance
    4x_DevianceSPSR_152000_G
    4x_DF2K_JPEG
    4x_DigitalFake_2.1_100000_G
    4x_DigitalFake-2.1_100000_G
    4x_eula_digimanga_bw_v1_860k
    4x_eula_digimanga_bw_v2_nc1_307k
    4x_face_focus_275k
    4x_Faces_04_N_180000_G
    4x_FArtDIV3_Base
    4x_FArtDIV3_Blend
    4x_FArtDIV3_Fine
    4x_FArtDIV3_UltraMix4
    4x_FArtFace
    4x_FArtSuperBlend
    4x_fatal_Anime_160k
    4x_fatal_Anime_190k
    4x_fatal_Anime_200k
    4x_fatal_Anime_260k
    4x_fatal_Anime_360k
    4x_Fatal_Anime_435k
    4x_fatal_Anime_500000_G
    4x_fatal_Faces_FS_MKI
    4x_Fatal_twerpilation
    4x_Fatality_01_375000_G
    4x_Fatality_Comix_260000_G
    4x_Fatality_Faces_310000_G
    4x_Fatality_MKII_90000_G
    4x_FatalPhotos_Beta
    4x_FatalPixels_340000_G
    4x_FireAlpha
    4x_foolhardy_Remacri_ExtraSmoother
    4x_foolhardy_Remacri
    4x_FS_Dedither_new
    4x_FuzzyBox
    4x_GameAI_1.0
    4x_GameAI_2.0
    4x_GameboyCamera
    4x_HDCube_110k
    4x_HellInACel
    4X_KCJPUNK_1.0_233089_
    4x_Loyaldk-Kororo_652500_V1.0
    4x_Loyaldk-LitePony_500000_V2.0
    4x_Loyaldk-MediumPony_500000_V2.0
    4x_Loyaldk-SuperPony_500000_V2.0
    4x_mdeblur
    4x_MeguUp_105000
    4x_Minecraft_256hr_55000_G
    4x_Minecraft_256hr_spsr_40000_G
    4x_Minepack
    4x_Morrowind_2.0_205K
    4x_MW_ESRGAN_130K
    4x_Nickelback_70000G
    4x_NickelbackFS_72000_G
    4x_NickelbackFS
    4x_NMKD_SuperYandere_175k
    4x_NMKD-PatchySharp_100K
    4x_NMKD-PatchySharp_135K
    4x_NMKD-PatchySharp_240K
    4x_NMKD-Siax_200k
    4x_NMKD-Superscale-SP_178000_G
    4x_NMKD-UltraYandere_300k
    4x_NMKD-UltraYandere-Lite_280k
    4x_NMKD-UpgifLiteV2_210k
    4x_NMKD-Yandere2_255000_G
    4x_NMKD-Yandere4_120000_G
    4x_NMKD-YandereNeoXL_200k
    4x_NMKDfaces_downsized
    4x_NMKDSuperscale-Artisoftject
    4x_NMKDSuperscale
    4x_OLDIES_290000_G_FINAL_interp_03
    4x_OLDIES_ALTERNATIVE_FINAL
    4x_OLDIES_ALTERNATIVE_FINAL.PTH
    4x_Pixelity_Faces
    4x_PixelPerfectV4_137000_G
    4x_PixelScale_MKII_Beta
    4x_PocketMonsters-Alpha_115000_G
    4x_realistic_misc_alsa
    4x_reks_effeks_photoanime_v2_150k
    4x_RRDB-G_ResNet-D_latest_G
    4x_scalenx_90k
    4x_ScreenBoosterV2_44000_G
    4x_SmolFace_200k
    4x_SmolFace_clean
    4x_Soladad
    4x_Sourcetex-v2_136000_G
    4x_Sourcetex-v2-DXTJPG-Smooth_132000_G
    4x_Sourcetex-v2-DXTJPG-Smoother_134000_G
    4x_Sourcetex-v2-Smooth_120000_G
    4x_Sourcetex-v2-Smoother_120000_G
    4x_Sourcetex-v2-Smoothest_100000_G
    4x_SpongeBob_235000_G
    4x_Spongebob_v6_190000_G
    4x_Spongebob_v6_DDDQ_90000_G
    4x_Spongebob_v6_Deblur_65000_G
    4x_SpongeBob-Reloaded_153000_G
    4x_SpongeBob-Reloaded-SWAG_153000_swaG
    4x_SpongePSNR_85k
    4x_Struzan_300000
    4x_test_clay_v2
    4x_test_Fatality_MK3
    4x_test_redither
    4x_Training4Melozard_Anime_144000_G
    4x_Training4Xeller_latest_G
    4x_Training4Xeller_v2_latest_G
    4x_trixie
    4x_Unholy_FArt
    4x_UniversalUpscalerV2-Neutral_115000_swaG
    4x_UniversalUpscalerV2-Sharp_101000_G
    4x_UniversalUpscalerV2-Sharper_103000_G
    4x_Valar_v1
    4x_xbrz_90k
    4x_xbrz+dd_260k
    4x-AnimeSharp-lite
    4x-AnimeSharp
    4x-DeCompress EXTREME(avoid unless necessary)
    4x-DeCompress-Strong
    4x-DeCompress
    4x-Fabric-Alt
    4x-Fabric
    4x-FatePlus-lite
    4x-SkyrimTexV2_Fabric
    4x-SkyrimTexV2.1
    4x-TextSharpV1
    4x-UltraMix_Balanced
    4x-UltraMix_Restore
    4x-UltraMix_Smooth
    4x-UltraSharp
    4x-UniScale_Restore
    4x-UniScale-Balanced [72000g]
    4x-UniScale-Interp
    4x-UniScale-Strong [42400g]
    4x-UniScaleNR-Balanced [34400g]
    4x-UniScaleNR-Strong [62400g]
    4x-UniScaleV2_Moderate
    4x-UniScaleV2_Sharp
    4x-UniScaleV2_Soft
    4x-VolArt
    4x-VolArtNR
    4xBox
    4xBS_DevianceV3
    4xCatPatch
    4xCharSprite
    4xContextualSpongebob_70000_G
    4xDetoon
    4xDigiPaint35k
    4xdragoon
    4xEdges2Faces_V2Test
    4xEdges2Faces_V3Test
    4xEdges2Faces
    4xESRGAN
    4xFaceB
    4xFaceriZor_V1Test
    4xFaithful64
    4xFalcoon
    4xFalloutWeaponsV2
    4xFart
    4xFatalCats
    4xFatalCoon
    4xFatalFacesV1
    4xFatalFacesV2
    4xFatalimiX_MKII_beta
    4xFatalimiX_MKIII
    4xFatalimiX
    4xFatalityV1
    4xFatalityV2
    4xFatalPixels
    4xFireAlpha
    4xForest
    4xFS_DF2K_jpeg_SDSR
    4xFS_DF2K_jpeg_TDSR
    4xFSDedither_Manga
    4xFSDedither_Riven_Smooth
    4xFSDedither_Riven
    4xFSDedither
    4xFSMangaV2
    4xFuzzyBox
    4xGround
    4xGuilty
    4xJaypeg90
    4xLADDIER1_282500_G
    4xLady0101
    4xlollypop
    4xManga109
    4xMCWashed
    4xMeguUp130k
    4xMinecraftAlpha
    4xMinecraftSPSR_60000_G
    4xMinepack
    4xMisc
    4xNickelback
    4xNickelfront
    4xPackCraft_v4_40000_G
    4xPackCraft_v4
    4xPaper
    4xpicsy
    4xPixelScale
    4xPixelScaleClay
    4xportrait
    4xPSNR
    4xQuaker
    4xRealSR_DF2K_JPEG
    4xRealSR_DF2K
    4xRealSR_DPED
    4xreboutfs
    4xreboutpg
    4xRender
    4xScreenBooster
    4xSGI_103000_G
    4xSGI
    4xShiteMountainV3
    4xSkyrim_Weapons_And_Armor
    4xSmoothRealism
    4xsnesal
    4xSourcetexV2_DXTJPG_Smooth
    4xSourcetexV2_DXTJPG_Smoother
    4xSourcetexV2_Smooth
    4xSourcetexV2_Smoother
    4xSourcetexV2
    4xSpongeBob
    4xSpongeBobTweak
    4xSteveHarvey
    4xSW1997_TEST
    4xSW1997
    4xSW1997Attempt2
    4xSW1997Attempt3
    4xSW1997V2
    4xSW1997V3
    4xsynla
    4xTest_cout
    4xTest_FSBox
    4xTest_FSLinear
    4xTest_pixy
    4xTest_scalegenx
    4xXplode
    4xyammy
    4xZZines
    8x_glasshopper_ArzenalV1.1_175000_downsized
    8x_glasshopper_MS-Unpainter_195000_G_downsized
    8x_glasshopper_MS-Unpainter_De-Dither_195000_G_downsized
    8x_HugePeeps_v1_downsized
    American.Dad.2.HD.150ki.5e-PHOENiX
    ArbSR
    BSRGAN
    deviantPixelHD_250000
    DF2K_JPEG
    DigiPaint35000
    ESRGAN_GroundTextures_NonTiled_RGB_UpscalingAlgorithm_128HR_32LR_305000Iterations
    ESRGAN_Skyrim_NonTiled_Alpha_NN_128_32_105000
    FeMaSR
    HAT_SRx4_ImageNet-pretrain
    HAT_SRx4
    HAT-L_SRx4_ImageNet-pretrain
    HCFlow
    LADDIER1_282500_G
    Lady0101_208000
    LBNet-X4
    LDSR
    lollypop
    nESRGANplus
    Real_HAT_GAN_SRx4
    realesr-general-wdn-x4v3
    realesr-general-x4v3
    RealESRGAN_x4plus_anime_6B
    RealESRGAN_x4plus
    realesrgan-x4minus
    RealESRGANv2-animevideo-xsx4
    reboutblend
    reboutcx
    RRDB_ESRGAN_x4_old_arch
    RRDB_PSNR_x4_old_arch
    ruDALL-E-SR
    SpongeBob.CEL.2.HD.125ki.499e-PHOENiX
    spsr
    SRResCGAN
    Swin2SR_ClassicalSR_X4_64
    Swin2SR_CompressedSR_X4_48
    Swin2SR_RealworldSR_X4_64_BSRGAN_PSNR

  </details>

##### Voting

"4x BSRGAN" and "4x BSRGAN_old_arch" -> "BSRGAN"

<div class="strawpoll-embed" id="strawpoll_QrgeVNGxOZp" style="height: 600px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;">
<iframe title="StrawPoll Embed" id="strawpoll_iframe_QrgeVNGxOZp" src="https://strawpoll.com/embed/polls/QrgeVNGxOZp" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe>
<!-- <script async src="https://cdn.strawpoll.com/dist/widgets.js" charset="utf-8"></script> -->
</div>
<br/>
<!-- Google Forms alternative, but I like the username entry of strawpoll since there are names/tags we know from the upscale community
<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSfwm-x0ZBB3fgcHzYUouXGkaA5EGndIFgpZCfF90oyN8VtXKg/viewform?embedded=true" width="640" height="474" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe> -->

#### Grosser Mythen

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTM3MDgy/0/1" style="width: 100%; border: 0px none; height: 62vmin; min-height: 300px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>

<a href="https://imgsli.com/MTM3MDgy/0/1" target="_blank">Open in external tab</a>

##### Example Details

Name: Grosser Mythen  
Creation Date: 01. Dec 2022  
 Input Image: 427x320 pixels  
 Scaling Factor: 4  
 Output Image: 1708x1280 pixels  
 Input Source File: [Link](https://github.com/Phhofm/upscale/public/sources/input/photos)  
 Output Source Files: [Link](https://github.com/Phhofm/upscale/public/sources/multimodel/current/photos)  
 (Output Source Files are mozjpg compressed

##### Voting

<div class="strawpoll-embed" id="strawpoll_PKglzr9zEyp" style="height: 600px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;">
<iframe title="StrawPoll Embed" id="strawpoll_iframe_PKglzr9zEyp" src="https://strawpoll.com/embed/polls/PKglzr9zEyp" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe>
<!-- <script async src="https://cdn.strawpoll.com/dist/widgets.js" charset="utf-8"></script> -->
</div>
<br/>

#### Painting

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTM3MTI2/0/1" style="width: 100%; border: 0px none; height: 62vmin; min-height: 300px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>

<a href="https://imgsli.com/MTM3MTI2/0/1" target="_blank">Open in external tab</a>

##### Example Details

Name: Painting
Creation Date: 01. Dec 2022  
 Input Image: 427x320 pixels  
 Scaling Factor: 4  
 Output Image: 1708x1280 pixels  
 Input Source File: [Link](https://github.com/Phhofm/upscale/public/sources/input/photos)  
 Output Source Files: [Link](https://github.com/Phhofm/upscale/public/sources/multimodel/current/photos)  
 (Output Source Files are mozjpg compressed

##### Voting

<div class="strawpoll-embed" id="strawpoll_QrgeVNMkbZp" style="height: 600px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;">
<iframe title="StrawPoll Embed" id="strawpoll_iframe_QrgeVNMkbZp" src="https://strawpoll.com/embed/polls/QrgeVNMkbZp" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe>
<!-- <script async src="https://cdn.strawpoll.com/dist/widgets.js" charset="utf-8"></script> -->
</div>
<br/>

#### PC Build

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTM3MTMw/0/1" style="width: 100%; border: 0px none; height: 62vmin; min-height: 300px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>

<a href="https://imgsli.com/MTM3MTMw/0/1" target="_blank">Open in external tab</a>

##### Example Details

Name: PC Build
Creation Date: 01. Dec 2022  
 Input Image: 427x320 pixels  
 Scaling Factor: 4  
 Output Image: 1708x1280 pixels  
 Input Source File: [Link](https://github.com/Phhofm/upscale/public/sources/input/photos)  
 Output Source Files: [Link](https://github.com/Phhofm/upscale/public/sources/multimodel/current/photos)  
 (Output Source Files are mozjpg compressed

##### Voting

<div class="strawpoll-embed" id="strawpoll_eJnv7bdNEgv" style="height: 600px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;">
<iframe title="StrawPoll Embed" id="strawpoll_iframe_eJnv7bdNEgv" src="https://strawpoll.com/embed/polls/eJnv7bdNEgv" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe>
<!-- <script async src="https://cdn.strawpoll.com/dist/widgets.js" charset="utf-8"></script> -->
</div>
<br/>

#### Snowboard

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTM3MTM4/0/1" style="width: 100%; border: 0px none; height: 62vmin; min-height: 300px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>

<a href="https://imgsli.com/MTM3MTM4/0/1" target="_blank">Open in external tab</a>

##### Example Details

Name: Snowboard
Creation Date: 01. Dec 2022  
 Input Image: 427x320 pixels  
 Scaling Factor: 4  
 Output Image: 1708x1280 pixels  
 Input Source File: [Link](https://github.com/Phhofm/upscale/public/sources/input/photos)  
 Output Source Files: [Link](https://github.com/Phhofm/upscale/public/sources/multimodel/current/photos)  
 (Output Source Files are mozjpg compressed

##### Voting

<div class="strawpoll-embed" id="strawpoll_B2ZB3MbxjyJ" style="height: 600px; width: 100%; margin: 0 auto; display: flex; flex-direction: column;">
<iframe title="StrawPoll Embed" id="strawpoll_iframe_B2ZB3MbxjyJ" src="https://strawpoll.com/embed/polls/B2ZB3MbxjyJ" style="position: static; visibility: visible; display: block; width: 100%; flex-grow: 1;" frameborder="0" allowfullscreen allowtransparency>Loading...</iframe>
<!-- <script async src="https://cdn.strawpoll.com/dist/widgets.js" charset="utf-8"></script> -->
</div>
<br/>

### Set 4

Creation Date Of Upscale Set: 04. Nov 2022  
 Models used: ~300  
 Models Category: Basically every applicable x4 model I currently had at my disposal

  <details>
    <summary>Models List</summary>

    001_classicalSR_DF2K_s64w8_SwinIR-M_x4
    001_classicalSR_DIV2K_s48w8_SwinIR-M_x4
    002_lightweightSR_DIV2K_s64w8_SwinIR-S_x4
    003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN
    003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN
    4x-AnimeSharp-lite
    4x-AnimeSharp
    4x-DeCompress
    4x-DeCompress-Strong
    4x-DeCompress
    4x-Fabric-Alt
    4x-Fabric
    4x-FatePlus-lite
    4x-SkyrimTexV2.1
    4x-SkyrimTexV2_Fabric
    4x-TextSharpV1
    4x-UltraMix_Balanced
    4x-UltraMix_Restore
    4x-UltraMix_Smooth
    4x-UltraSharp
    4x-UniScale-Balanced
    4x-UniScale-Interp
    4x-UniScale-Strong
    4x-UniScaleNR-Balanced
    4x-UniScaleNR-Strong
    4x-UniScaleV2_Moderate
    4x-UniScaleV2_Sharp
    4x-UniScaleV2_Soft
    4x-UniScale_Restore
    4x-VolArt
    4x-VolArtNR
    4xBox
    4xBS_DevianceV3
    4xCatPatch
    4xCharSprite
    4xContextualSpongebob_70000_G
    4xDetoon
    4xDigiPaint35k
    4xdragoon
    4xESRGAN
    4xFaceB
    4xFaithful64
    4xFalcoon
    4xFalloutWeaponsV2
    4xFart
    4xFatalCats
    4xFatalCoon
    4xFatalFacesV1
    4xFatalFacesV2
    4xFatalimiX
    4xFatalimiX_MKIII
    4xFatalimiX_MKII_beta
    4xFatalityV1
    4xFatalityV2
    4xFatalPixels
    4xFireAlpha
    4xForest
    4xFSDedither
    4xFSDedither_Manga
    4xFSDedither_Riven
    4xFSDedither_Riven_Smooth
    4xFSMangaV2
    4xFS_DF2K_jpeg_SDSR
    4xFS_DF2K_jpeg_TDSR
    4xFuzzyBox
    4xGround
    4xGuilty
    4xJaypeg90
    4xLADDIER1_282500_G
    4xLady0101
    4xlollypop
    4xManga109
    4xMCWashed
    4xMeguUp130k
    4xMinecraftAlpha
    4xMinecraftSPSR_60000_G
    4xMinepack
    4xMisc
    4xNickelback
    4xNickelfront
    4xPackCraft_v4
    4xPackCraft_v4_40000_G
    4xPaper
    4xpicsy
    4xPixelScale
    4xPixelScaleClay
    4xportrait
    4xPSNR
    4xQuaker
    4xRealSR_DF2K
    4xRealSR_DF2K_JPEG
    4xRealSR_DPED
    4xreboutfs
    4xreboutpg
    4xRender
    4xScreenBooster
    4xSGI
    4xSGI_103000_G
    4xShiteMountainV3
    4xSkyrim_Weapons_And_Armor
    4xSmoothRealism
    4xsnesal
    4xSourcetexV2
    4xSourcetexV2_DXTJPG_Smooth
    4xSourcetexV2_DXTJPG_Smoother
    4xSourcetexV2_Smooth
    4xSourcetexV2_Smoother
    4xSpongeBob
    4xSpongeBobTweak
    4xSteveHarvey
    4xSW1997
    4xSW1997Attempt2
    4xSW1997Attempt3
    4xSW1997V2
    4xSW1997V3
    4xSW1997_TEST
    4xsynla
    4xTest_FSBox
    4xTest_FSLinear
    4xTest_pixy
    4xTest_scalegenx
    4xXplode
    4xyammy
    4xZZines
    4x_AmericanDad2
    4x_Archerpolation_NXbrz
    4x_BigFace_v3
    4x_BigFace_v3_Blend
    4x_BigFace_v3_Clear
    4x_BigFArt_Bang1
    4x_BigFArt_Base
    4x_BigFArt_Blend
    4x_BigFArt_Detail_300000_G
    4x_BigFArt_Fine
    4x_BMS_85000_G
    4x_BMS_jpg60_20000_G
    4x_BooruGan_600k
    4x_BooruGan_650k
    4x_BSRGAN
    4x_BSRGAN_old_arch
    4x_BS_DevianceMIP_82000_G
    4x_BS_DevianceV2
    4x_BS_Mystery
    4x_BS_SbeveHarvey_62000_G
    4x_BS_Screenbooster_SPSR_88000G
    4x_b_melozard_2_latest_G
    4x_cat_patch_325000_G
    4x_comic_dataset_115k
    4x_Compact_Pretrain
    4x_Compact_Pretrain_traiNNer
    4x_CountryRoads_377000_G
    4x_DBMangaStand_255k
    4x_DeBLRFS
    4x_deindeo_x4_130000_G
    4x_Deviance
    4x_DevianceSPSR_152000_G
    4x_Deviance_60000G
    4x_DF2K_JPEG
    4x_DigitalFake-2.1_100000_G
    4x_DigitalFake_2.1_100000_G
    4x_Faces_04_N_180000_G
    4x_face_focus_275k
    4x_FArtDIV3_Base
    4x_FArtDIV3_Blend
    4x_FArtDIV3_Fine
    4x_FArtDIV3_UltraMix4
    4x_FArtFace
    4x_FArtSuperBlend
    4x_Fatality_01_375000_G
    4x_Fatality_Comix_260000_G
    4x_Fatality_Faces_310000_G
    4x_Fatality_MKII_90000_G
    4x_FatalPhotos_Beta
    4x_FatalPixels_340000_G
    4x_fatal_Anime_160k
    4x_fatal_Anime_190k
    4x_fatal_Anime_200k
    4x_fatal_Anime_260k
    4x_fatal_Anime_360k
    4x_Fatal_Anime_435k
    4x_fatal_Anime_500000_G
    4x_fatal_Faces_FS_MKI
    4x_Fatal_twerpilation
    4x_FireAlpha
    4x_foolhardy_Remacri
    4x_foolhardy_Remacri_ExtraSmoother
    4x_FS_Dedither_new
    4x_FuzzyBox
    4x_GameAI_1.0
    4x_GameAI_2.0
    4x_HDCube_110k
    4x_HellInACel
    4X_KCJPUNK_1.0_233089_
    4x_Loyaldk-Kororo_652500_V1.0
    4x_Loyaldk-LitePony_500000_V2.0
    4x_Loyaldk-MediumPony_500000_V2.0
    4x_Loyaldk-SuperPony_500000_V2.0
    4x_MeguUp_105000
    4x_Minecraft_256hr_55000_G
    4x_Minecraft_256hr_spsr_40000_G
    4x_Minepack
    4x_Morrowind_2.0_205K
    4x_MW_ESRGAN_130K
    4x_NickelbackFS
    4x_NickelbackFS_72000_G
    4x_Nickelback_70000G
    4x_NMKD-PatchySharp_100K
    4x_NMKD-PatchySharp_135K
    4x_NMKD-PatchySharp_240K
    4x_NMKD-Siax_200k
    4x_NMKD-Superscale-SP_178000_G
    4x_NMKD-UltraYandere-Lite_280k
    4x_NMKD-UltraYandere_300k
    4x_NMKD-UpgifLiteV2_210k
    4x_NMKD-Yandere2_255000_G
    4x_NMKD-Yandere4_120000_G
    4x_NMKD-YandereNeoXL_200k
    4x_NMKDSuperscale-Artisoftject
    4x_NMKDSuperscale
    4x_NMKD_SuperYandere_175k
    4x_OLDIES_290000_G_FINAL_interp_03
    4x_OLDIES_ALTERNATIVE_FINAL
    4x_OLDIES_ALTERNATIVE_FINAL.PTH
    4x_PixelPerfectV4_137000_G
    4x_PixelScale_MKII_Beta
    4x_PocketMonsters-Alpha_115000_G
    4x_realistic_misc_alsa
    4x_reks_effeks_photoanime_v2_150k
    4x_RRDB-G_ResNet-D_latest_G
    4x_scalenx_90k
    4x_ScreenBoosterV2_44000_G
    4x_SmolFace_200k
    4x_SmolFace_clean
    4x_Soladad
    4x_Sourcetex-v2-DXTJPG-Smoother_134000_G
    4x_Sourcetex-v2-DXTJPG-Smooth_132000_G
    4x_Sourcetex-v2-Smoother_120000_G
    4x_Sourcetex-v2-Smooth_120000_G
    4x_Sourcetex-v2_136000_G
    4x_SpongeBob-Reloaded-SWAG_153000_swaG
    4x_SpongeBob-Reloaded_153000_G
    4x_SpongeBob_235000_G
    4x_Spongebob_v6_190000_G
    4x_Spongebob_v6_DDDQ_90000_G
    4x_Spongebob_v6_Deblur_65000_G
    4x_SpongePSNR_85k
    4x_Struzan_300000
    4x_test_clay_v2
    4x_test_Fatality_MK3
    4x_test_redither
    4x_Training4Melozard_Anime_144000_G
    4x_Training4Xeller_latest_G
    4x_Training4Xeller_v2_latest_G
    4x_trixie
    4x_Unholy_FArt
    4x_UniversalUpscalerV2-Neutral_115000_swaG
    4x_UniversalUpscalerV2-Sharper_103000_G
    4x_UniversalUpscalerV2-Sharp_101000_G
    4x_Valar_v1
    4x_xbrz+dd_260k
    4x_xbrz_90k
    American.Dad.2.HD.150ki.5e-PHOENiX
    arbsr
    BSRGAN
    deviantPixelHD_250000
    DF2K_JPEG
    DigiPaint35000
    esrgan
    ESRGAN_GroundTextures_NonTiled_RGB_UpscalingAlgorithm_128HR_32LR_305000Iterations
    hat
    hcflow-sr
    LADDIER1_282500_G
    Lady0101_208000
    lbnet-x4
    ldsr_100steps
    ldsr_200steps
    ldsr_500steps
    ldsr_50steps
    lollypop
    nESRGANplus
    real-esrgan
    realesr-general-wdn-x4v3
    realesr-general-x4v3
    realesrgan-x4minus
    RealESRGANv2-animevideo-xsx4
    RealESRGAN_x4plus
    RealESRGAN_x4plus_anime_6B
    reboutblend
    reboutcx
    RRDB_ESRGAN_x4_old_arch
    RRDB_PSNR_x4_old_arch
    rudalle-sr
    SpongeBob.CEL.2.HD.125ki.499e-PHOENiX
    spsr
    srrescgan
    swin2sr_classical_sr
    swin2sr_compressed_sr
    swin2sr_real_sr
    swinir-l
    swinir-m

  </details>

#### Beautiful Landscape

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTMyOTA0/0/1" style="width: 100%; border: 0px none; height: 78vmin; min-height: 410px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>

<a href="https://imgsli.com/MTMyOTA0/0/1" target="_blank">Open in external tab</a>

##### Example Details

Input Image: 256x256 pixels  
 Scaling Factor: 4  
 Output Image: 1280x1280 pixels  
 Type: AI Generated Image

### Set 3

Creation Date Of Upscale Set: 27. Oct 2022  
 Models used: 87  
 Models Category: Universal Upsaling Models (extended), Art/Pixel Art models, Official Models, Pretrained Models, Model Collections  
 Usage Type: Art Images

  <details>
    <summary>Models List</summary>

    001_classicalSR_DF2K_s64w8_SwinIR-M_x4
    001_classicalSR_DIV2K_s48w8_SwinIR-M_x4
    002_lightweightSR_DIV2K_s64w8_SwinIR-S_x4
    003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN
    003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN
    4x-UltraMix_Balanced
    4x-UltraMix_Restore
    4x-UltraMix_Smooth
    4x-UltraSharp
    4x-UniScale-Balanced
    4x-UniScale-Interp
    4x-UniScale-Strong
    4x-UniScaleNR-Balanced
    4x-UniScaleNR-Strong
    4x-UniScaleV2_Moderate
    4x-UniScaleV2_Sharp
    4x-UniScaleV2_Soft
    4x-UniScale_Restore
    4xESRGAN
    4xPSNR
    4xSmoothRealism
    4x_Archerpolation_NXbrz
    4x_BigFArt_Bang1
    4x_BigFArt_Base
    4x_BigFArt_Blend
    4x_BigFArt_Detail_300000_G
    4x_BigFArt_Fine
    4x_BS_DevianceMIP_82000_G
    4x_Compact_Pretrain
    4x_Compact_Pretrain_traiNNer
    4x_CountryRoads_377000_G
    4x_Deviance_60000G
    4x_ESRGAN
    4x_FArtDIV3_Base
    4x_FArtDIV3_Blend
    4x_FArtDIV3_Fine
    4x_FArtDIV3_UltraMix4
    4x_FArtSuperBlend
    4x_Fatality_01_375000_G
    4x_Fatality_MKII_90000_G
    4x_FatalPixels_340000_G
    4x_foolhardy_Remacri
    4x_FuzzyBox
    4x_hcflow-sr_general
    4x_Lanzcos
    4x_LDSR
    4x_LDSR_100steps
    4x_LDSR_200steps
    4x_LDSR_500steps
    4x_LDSR_50steps
    4x_NMKD-Siax_200k
    4x_PixelPerfectV4_137000_G
    4x_realistic_misc_alsa
    4x_rudalle-sr
    4x_scalenx_90k
    4x_ScuNET
    4x_srrescgan
    4x_Struzan_300000
    4x_SwinIR
    4x_Unholy_FArt
    4x_UniversalUpscalerV2-Neutral_115000_swaG
    4x_UniversalUpscalerV2-Sharper_103000_G
    4x_UniversalUpscalerV2-Sharp_101000_G
    4x_xbrz+dd_260k
    4x_xbrz_90k
    8x_glasshopper_ArzenalV1.1_175000__downsized
    8x_glasshopper_MS-Unpainter_195000_G__downsized
    8x_glasshopper_MS-Unpainter_De-Dither_195000_G__downsized
    8x_HugePeeps_v1__downsized
    BSRGAN
    deviantPixelHD_250000
    DF2K_JPEG
    Lady0101_208000
    lollypop
    nESRGANplus
    realesr-general-wdn-x4v3
    realesr-general-x4v3
    realesrgan-x4minus
    RealESRGANv2-animevideo-xsx4
    RealESRGAN_x4plus
    RealESRGAN_x4plus_anime_6B
    reboutblend
    reboutcx
    RRDB_ESRGAN_x4_old_arch
    RRDB_PSNR_x4_old_arch
    ScuNET_PSNR
    spsr

  </details>

#### Wuffy

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTMxODgy/0/1" style="width: 100%; border: 0px none; height: 78vmin; min-height: 410px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>

<a href="https://imgsli.com/MTMxODgy/0/30" target="_blank">Open in external tab</a>

##### Example Details

Input Image: 480x480 pixels  
 Scaling Factor: 4  
 Output Image: 1920x1920 pixels  
 Type: AI Generated Image

#### Planet

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTMyMDEz/0/1" style="width: 100%; border: 0px none; height: 78vmin; min-height: 410px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>

<a href="https://imgsli.com/MTMyMDEz/0/1" target="_blank">Open in external tab</a>

##### Example Details

Input Image: 480x480 pixels  
 Scaling Factor: 4  
 Output Image: 1920x1920 pixels  
 Type: AI Generated Image

#### Landscape

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTMyMDE4/0/1" style="width: 100%; border: 0px none; height: 78vmin; min-height: 410px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>

<a href="https://imgsli.com/MTMyMDE4/0/1" target="_blank">Open in external tab</a>

##### Example Details

Input Image: 480x480 pixels  
 Scaling Factor: 4  
 Output Image: 1920x1920 pixels  
 Type: AI Generated Image

### Set 2

Creation Date Of Upscale Set: 22. Oct 2022  
 Models used: 71  
 Models Category: Universal Upsaling Models (extended), Realistic Photos models, Faces models, Official Models, Pretrained Models, Model Collections  
 Usage Type: Photos with people/faces in it

  <details>
    <summary>Models List</summary>

    001_classicalSR_DF2K_s64w8_SwinIR-M_x4
    001_classicalSR_DIV2K_s48w8_SwinIR-M_x4
    002_lightweightSR_DIV2K_s64w8_SwinIR-S_x4
    003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN
    003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN
    4x-UltraMix_Balanced
    4x-UltraMix_Restore
    4x-UltraMix_Smooth
    4x-UltraSharp
    4x-UniScale-Balanced
    4x-UniScale-Interp
    4x-UniScale-Strong
    4x-UniScaleNR-Balanced
    4x-UniScaleNR-Strong
    4x-UniScaleV2_Moderate
    4x-UniScaleV2_Sharp
    4x-UniScaleV2_Soft
    4x-UniScale_Restore
    4xBox
    4xESRGAN
    4xPSNR
    4x_BigFace_v3
    4x_BigFace_v3_Blend
    4x_BigFace_v3_Clear
    4x_BS_SbeveHarvey_62000_G
    4x_Compact_Pretrain
    4x_Compact_Pretrain_traiNNer
    4x_CountryRoads_377000_G
    4x_Faces_04_N_180000_G
    4x_face_focus_275k
    4x_FArtFace
    4x_Fatality_Faces_310000_G
    4x_foolhardy_Remacri
    4x_FuzzyBox
    4x_NickelbackFS_72000_G
    4x_Nickelback_70000G
    4x_NMKD-Siax_200k
    4x_NMKD-Superscale-SP_178000_G
    4x_realistic_misc_alsa
    4x_SmolFace_200k
    4x_SmolFace_clean
    4x_UniversalUpscalerV2-Neutral_115000_swaG
    4x_UniversalUpscalerV2-Sharper_103000_G
    4x_UniversalUpscalerV2-Sharp_101000_G
    4x_Valar_v1
    arbsr
    BSRGAN
    BSRGAN4x
    codeformer4x_enhanceall_fidelity1
    DF2K_JPEG
    hat
    hcflow-sr
    Lanczos4x
    LDSR4x_100steps
    LDSR4x_200steps
    LDSR4x_500steps
    LDSR4x_50steps
    lollypop
    nESRGANplus
    real-esrgan-faceenhance
    realesr-general-wdn-x4v3
    realesr-general-x4v3
    realesrgan-x4minus
    RealESRGAN_x4plus
    RRDB_ESRGAN_x4_old_arch
    RRDB_PSNR_x4_old_arch
    rudalle-sr
    ScuNETGAN
    ScuNETPSNR
    spsr
    srrescgan

  </details>

#### Buddy

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTMyNTYx/0/1" style="width: 100%; border: 0px none; height: 55vmin; min-height: 320px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>

<a href="https://imgsli.com/MTMyNTYx/0/1" target="_blank">Open in external tab</a>

##### Example Details

Input Image: 480x320 pixels  
 Scaling Factor: 4  
 Output Image: 1920x1330 pixels (without caption it would have been 1920x1280)  
 Type: Photo

### Set 1

Creation Date Of Upscale Set: 2nd Oct. 2022  
 Models used: 22  
 Models Category: Universal Upsaling Models  
 Usage Type: Universal

  <details>
    <summary>Models List</summary>

    CountryRoads
    Remacri
    UltraSharp
    UltraMix-Balanced
    UltraMix-Restore
    UltraMix-Smooth
    UniScale-Restore
    UniScale-Balanced
    UniScale-Interp
    UniScaleNR-Balanced
    UniScaleNR-Strong
    UniScale-Restore
    UniScaleV2-Soft
    UniScaleV2-Moderate
    UniScaleV2-Sharp
    realsrgan-minus
    Misc
    FuzzyBox
    Lollypop
    UniversalUpscalerV2-Neutral
    UniversalUpscalerV2-Sharp
    UniversalUpscalerV2-Sharper
    NMKD Siax

  </details>

#### Buddy

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4NDE3/0/1" style="width: 100%; border: 0px none; height: 55vmin; min-height: 310px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### Hike

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4NjY3/0/1" style="width: 100%; border: 0px none; height: 60vmin; min-height: 320px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### Grat

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4NjY5/0/1" style="width: 100%; border: 0px none; height: 100vmin; min-height: 500px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### View

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4Njc1/0/1" style="width: 100%; border: 0px none; height: 48vmin; min-height: 280px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### PC Build

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4Njcx/0/1" style="width: 100%; border: 0px none; height: 60vmin; min-height: 320px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### 200Fr PC Build

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4Njcz/0/1" style="width: 100%; border: 0px none; height: 60vmin; min-height: 320px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### Painting

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4NjY4/0/1" style="width: 100%; border: 0px none; height: 60vmin; min-height: 320px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### Charade1963 Screenshot

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4NDIy/0/1" style="width: 100%; border: 0px none; height: 48vmin; min-height: 270px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### Wuffy

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4NDE5/0/1" style="width: 100%; border: 0px none; height: 78vmin; min-height: 410px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### Child

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4NjI4/0/1" style="width: 100%; border: 0px none; height: 78vmin; min-height: 410px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### Sir Foxy

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4Njc0/0/1" style="width: 100%; border: 0px none; height: 78vmin; min-height: 410px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### Freedoom Texture

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4NDEz/0/1" style="width: 100%; border: 0px none; height: 35vmin; min-height: 320px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### Freedoom Sprite

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4NDE1/0/1" style="width: 100%; border: 0px none; height: 35vmin; min-height: 320px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>
<br/>

#### Freedoom Titlepic

<div style="border: 0px solid rgb(201, 0, 1); overflow: hidden; margin: 15px auto; max-width: 100%;">
  <iframe allowfullscreen scrolling="no" src="https://imgsli.com/MTI4Njcw/0/1" style="width: 100%; border: 0px none; height: 52vmin; min-height: 300px; margin-top: -75px; margin-bottom:-30px;">
  </iframe>
</div>