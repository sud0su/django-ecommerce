<template>
    <div class="column is-7 is-offset-1">
        <h1 class="login-heading">Welcome to the Site</h1>
        <p class="login-subheading">{{ msg }}</p>

        <form @submit.prevent="login">
            <div class="field">
            <p class="control has-icons-left has-icons-right">
                <input class="input is-medium" type="text" placeholder="username" v-model="credentials.username" :class="{ 'is-danger': $v.credentials.username.$error }">
                <span class="icon is-medium is-left">
                <i class="fa fa-envelope"></i>
                </span>
                <span class="icon is-small is-right">
                <i class="fa fa-check"></i>
                </span>
            </p>
            </div>
            <div class="field">
            <p class="control has-icons-left has-icons-right">
                <input class="input is-medium" type="password" placeholder="Password" v-model="credentials.password" :class="{ 'is-danger': $v.credentials.username.$error }">
                <span class="icon is-medium is-left">
                <i class="fa fa-lock"></i>
                </span>
                <span class="icon is-small is-right">
                <i class="fa fa-eye"></i>
                </span>
            </p>
            </div>
            <div class="field is-grouped is-grouped-centered login-btn-group">
            <p class="control">
                <button class="button is-primary is-rounded" :disabled="!valid">Login</button>
            </p>
            <p class="control">
                <a class="forgot-link" ><router-link to="/password_reset">Reset Password</router-link></a>
            </p>
            </div>
        </form>
    </div>
</template>

<script>
import { required, minLength, between } from 'vuelidate/lib/validators'

export default {
    name: 'Auth',
    data: () => ({
        credentials: {
            username: '',
            password: ''
        },
        msg: 'Fill out thisto access super awesome imaginary control panel',
        valid:true,
        loading:false
    }),
    validations: {
        credentials: {
            username: { required, min: minLength(3) },
            password: { required }
        }
    },
    methods: {
        login() {
            var me = this;
            me.$v.credentials.$touch();
            if(me.$v.credentials.$error) return me.loading = false
            me.loading = true;
            me.$store.dispatch('auth/login', me.credentials)
                .then(() => me.$store.getters['auth/isAuthenticated'] ? me.$router.push('/') : me.msg = 'Wrong username or password')
        }
    }

}
</script>
