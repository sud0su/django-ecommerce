import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'

import router from './router'

import Default from './layouts/Default.vue'
import NoSidebar from './layouts/NoSidebar.vue'

Vue.component('default-layout', Default)
Vue.component('no-sidebar-layout', NoSidebar)

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
  render: h => h(App)
})
