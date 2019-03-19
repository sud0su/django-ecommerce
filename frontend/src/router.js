import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    made: 'history',

    routes: [
        {
            path: '/',
            name: 'home',
            meta: {layout: "no-sidebar"},
            component: require("@/pages/Home.vue").default
        }
    ]
})