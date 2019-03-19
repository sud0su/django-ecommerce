<template>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            Primary title
          </h1>
          <h2 class="subtitle">
            Primary subtitle
          </h2>
        </div>
      </div>
    </section>
  <!-- <div id="app"> -->
    <!-- {{ msg }}
    <form @submit.prevent="submitCarrier">
      <label>Name</label>
      <input type="text" v-model="formData.name">
      <label>Price</label>
      <input type="text" v-model="formData.price">
      <label>Delivery Text</label>
      <input type="text" v-model="formData.delivery_text">
      <div v-if="!formData.logo">
        <label>Select an image</label>
        <input type="file" @change="onFileChange">
      </div>
      <div v-else>
        <img :src="formData.logo" />
        <button @click="removeImage">Remove image</button>
      </div>
      <br>
      <button type="submit">Submit</button>
    </form> -->
  <!-- </div> -->
</template>

<script>
import api from '@/api/carriers'

export default {
  name: 'app',
  data () {
    return {
      msg: 'Carriers Form',
      formData: {
        name: '',
        price: '',
        delivery_text: '',
        logo: ''
      }
    }
  },
  methods: {
    submitCarrier(){
      api.fetchCarriers('post', null, this.formData).then( res => {
        this.msg = 'Saved'
      }).catch((e)=>{
        this.msg = e.response
      })
    },
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      this.createImage(files[0]);
    },
    createImage(file) {
      var logo = new Image();
      var reader = new FileReader();
      var getlogo = this.formData;

      reader.onload = (e) => {
        getlogo.logo = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    removeImage: function (e) {
      this.formData.logo = '';
    }
  },
}
</script>
