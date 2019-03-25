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
  name: 'app',
  mounted() {
    this.checkLoggedIn();
  },
  components:{
    CarouselBar,
  },
  methods: {
    checkLoggedIn(){
      this.$session.start();
      if(!this.$session.has('token')){
        this.$router.push('/login');
      }      
    }
  },
}
</script>

<style>
/* .carouselbg {
  background-color: azure;
} */
</style>
