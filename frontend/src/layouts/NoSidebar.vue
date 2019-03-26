<script>
import { mapGetters } from 'vuex';
import Navbar from '@/layouts/components/Navbar'
import FooterBar from '@/layouts/components/Footer'

export default {
    components: {
        Navbar,
        FooterBar
    },
    computed: mapGetters('auth', ['isAuthenticated',]),
}
</script>

<template>
    <div>
        <navbar></navbar>
            <slot />
        <footer-bar />
    </div>
</template>
