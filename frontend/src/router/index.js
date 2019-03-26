import Vue from 'vue';
import Router from 'vue-router';
// Public Pages
import Home from '@/pages/Home';
import About from '@/pages/About';
import NotFound from '@/pages/404';
// Authentification
import Login from '@/pages/authentification/Login';
import Register from '@/pages/authentification/Signup';
import PasswordReset from '@/pages/authentification/PasswordReset';
import PasswordResetConfirm from '@/pages/authentification/PasswordResetConfirm';
import VerifyEmail from '@/pages/authentification/VerifyEmail';

import store from '@/store';

const requireAuthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (!store.getters['auth/isAuthenticated']) {
        next('/login');
      } else {
        next();
      }
    });
};

const requireUnauthenticated = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      if (store.getters['auth/isAuthenticated']) {
        next('/home');
      } else {
        next();
      }
    });
};

const AuthenticatedYesOrNot = (to, from, next) => {
  store.dispatch('auth/initialize')
    .then(() => {
      console.log(store.getters['auth/isAuthenticated']);
    })
    .then(() => next());
};

const redirectLogout = (to, from, next) => {
  store.dispatch('auth/logout')
    .then(() => next('/login'));
};

Vue.use(Router);

export default new Router({
  saveScrollPosition: true,
  routes: [
    {
      path: '/',
      redirect: '/home',
    },
    {
      path: '/about',
      component: About,
      beforeEnter: AuthenticatedYesOrNot,
    },
    {
      path: '/home',
      meta: {layout: "no-sidebar"},
      component: Home,
      beforeEnter: AuthenticatedYesOrNot,
    },
    {
      path: '/password_reset',
      component: PasswordReset,
    },
    {
      path: '/password_reset/:uid/:token',
      component: PasswordResetConfirm,
    },
    {
      path: '/register',
      component: Register,
    },
    {
      path: '/register/:key',
      component: VerifyEmail,
    },
    {
      path: '/login',
      component: Login,
      meta: {layout: "login"},
      beforeEnter: requireUnauthenticated,
    },
    {
      path: '/logout',
      beforeEnter: redirectLogout,
    },
    {
      path: '*',
      component: NotFound,
    },
  ],
});
