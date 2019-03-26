<template>
  <div>
    <section class="hero carouselbg">
      <carousel-bar />
    </section>
  </div>
</template>

<script>
import CarouselBar from '@/components/Carousel'

export default {
  name: 'home',
  components:{
    CarouselBar,
  }
}
</script>

<style>
/* .carouselbg {
  background-color: azure;
} */
</style>
