<template>
  <hooper :settings="hooperSettings">
    <slide>
      <img src="http://placehold.it/630x250">
    </slide>
    <slide>
      <img src="http://placehold.it/630x250">
    </slide>
    <slide>
      <img src="http://placehold.it/630x250">
    </slide>
    <slide>
      <img src="http://placehold.it/630x250">
    </slide>
    <slide>
      <img src="http://placehold.it/630x250">
    </slide>
    <slide>
      <img src="http://placehold.it/630x250">
    </slide>
    <hooper-navigation slot="hooper-addons"></hooper-navigation>
    <hooper-pagination slot="hooper-addons"></hooper-pagination>
  </hooper>
</template>

<script>
import {
  Hooper,
  Slide,
  Navigation as HooperNavigation,
  Pagination as HooperPagination 
  } from 'hooper';
import 'hooper/dist/hooper.css';

export default {
    name: 'Carousel',
    components: {
        Hooper,
        Slide,
        HooperNavigation,
        HooperPagination
    },
    data () {
      return {
        hooperSettings: {
          itemsToShow: 3,
          centerMode: true
        }
      }
    }
}
</script>

<style>
.hooper{
    height: 100%;
    padding: 0px 0px 20px;
}
.hooper-indicator{
    height: 7px;
}
.hooper-indicator.is-active, .hooper-indicator:hover {
    width: 20px;
}
.hooper-pagination {
    bottom: 5px;
}
.hooper-navigation {
    position: relative;
    margin: 10px 40% 0px;
}
</style>
