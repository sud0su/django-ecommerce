import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router/index'
import VueSession from 'vue-session'
import Vuelidate from 'vuelidate'

// import store from './store/index'
// layout
import Default from './layouts/Default.vue'
import NoSidebar from './layouts/NoSidebar.vue'
import Login from './layouts/Login.vue'

Vue.use(VueSession)
Vue.use(Vuelidate)
Vue.component('default-layout', Default)
Vue.component('no-sidebar-layout', NoSidebar)
Vue.component('login-layout', Login)

Vue.config.productionTip = false

require("./assets/main.scss")

new Vue({
  el: '#app',
  beforeCreate () {
    Vue.prototype.$http = axios
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    axios.defaults.xsrfCookieName = 'csrftoken'
  },
  router,
  // store,
  render: h => h(App)
})
