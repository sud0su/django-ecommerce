import Vue from 'vue'
import Router from 'vue-router'

// Pages
import Login from '@/pages/Login'
import Carriers from '@/pages/Carriers'

Vue.use(Router)
export default new Router({
    made: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            meta: {layout: "no-sidebar"},
            component: require("@/pages/Home.vue").default
        },{
            path: '/login',
            name: 'login',
            meta: {layout: "login"},
            component: Login
        },{
            path: '/carriers',
            name: 'carriers',
            component: Carriers
        }
    ]
})