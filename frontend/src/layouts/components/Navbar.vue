  <!-- <ul class="navbar" id="navbar">
    <li><router-link to="/logout">logout</router-link></li>
    <li><router-link to="/about">about</router-link></li>
  </ul> -->
<template>
  <div>
    <nav class="navbar primarynav is-white">
      <div class="container">
        <div class="navbar-brand">
          <a class="navbar-item" href="/">
            (Django + VueJS) E-Commerce
          </a>

          <a class="navbar-burger" @click="open = !open">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div class="navbar-menu" :class="{'is-active': open}">
          <div class="navbar-start search">
            <div class="navbar-item search">
              <div class="control has-icons-right">
                <input class="input" type="search" placeholder="Search...">
                <span class="icon is-small is-right">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
                  <path fill="#ddd" d="M23.822 20.88l-6.353-6.354c.93-1.465 1.467-3.2 1.467-5.059.001-5.219-4.247-9.467-9.468-9.467s-9.468 4.248-9.468 9.468c0 5.221 4.247 9.469 9.468 9.469 1.768 0 3.421-.487 4.839-1.333l6.396 6.396 3.119-3.12zm-20.294-11.412c0-3.273 2.665-5.938 5.939-5.938 3.275 0 5.94 2.664 5.94 5.938 0 3.275-2.665 5.939-5.94 5.939-3.274 0-5.939-2.664-5.939-5.939z"/></svg>    
                </span>
              </div>
            </div>
          </div>

          <div class="navbar-end">
            <div class="navbar-item">
              <router-link class="button is-white" to="/">
                <span class="icon">
                  <i class="fas fa-shopping-cart"></i>
                </span>
              </router-link>
            </div>

            <div v-if="!isAuthenticated" class="ifconditional">
              <div class="navbar-item">
                <router-link class="button is-success is-outlined" to="/login">
                  Login
                </router-link>
              </div>
              <div class="is-divider-vertical" data-content="OR"></div>
              <div class="navbar-item">
                <router-link class="button is-danger is-outlined" to="/register">
                  Register
                </router-link>
              </div>
            </div>
            <div v-else  class="ifconditional">
              <div class="navbar-item">
                <router-link class="button is-success" to="/logout">
                  Logout
                </router-link>
              </div>
            </div>
              
          </div>
        </div>
      </div>
    </nav>

    <nav class="navbar secondarynav is-white">
      <div class="container">
        <div class="navbar-menu" :class="{'is-active': open}">
          <div class="navbar-start">
            <div class="navbar-item">
              <a href="#"><i class="fas fa-mobile-alt"></i> Download App</a>
            </div>
          </div>

          <div class="navbar-end">
            <div class="navbar-item">
              <a href="#"><i class="fas fa-headset"></i> Support Center</a>
            </div>
            <div class="navbar-item">
              <a href="#"><i class="fas fa-language"></i> Language</a>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'member-navbar',
  data() {
    return {
      open: false
    };
  },
  computed: mapGetters('auth', ['isAuthenticated',]),
};
</script>

<style lang="scss">
$navbar-height: 1.5rem;
@import "~bulma/bulma";
@import '~bulma-divider';

.primarynav {
  border-bottom: solid 1px #f3f3f3
}
.secondarynav a {    
    color: #636363;
    font-size: 14px;
}
.navbar {
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
}

.search, .search > .control {
  width: 100%;
}
</style>