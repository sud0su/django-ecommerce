import Vue from 'vue';
import Vuelidate from 'vuelidate'

import App from './App';
import router from './router';
import store from './store';
// layout
import Default from './layouts/Default.vue'
import NoSidebar from './layouts/NoSidebar.vue'
import Login from './layouts/Login.vue'

Vue.use(Vuelidate)
Vue.config.productionTip = false;

Vue.component('default-layout', Default)
Vue.component('no-sidebar-layout', NoSidebar)
Vue.component('login-layout', Login)

require("./assets/main.scss")


// new Vue({
//   el: '#app',
//   router,
//   store,
//   render: h => h(App)
// })


export default new Vue({
  router,
  store,
  el: '#app',
  template: '<App/>',
  components: { App },
});