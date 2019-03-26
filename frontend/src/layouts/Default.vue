<script>
import { mapGetters } from 'vuex';
import Navbar from '@/layouts/components/Navbar'
import FooterBar from '@/layouts/components/Footer'
import SideBar from '@/layouts/components/Sidebar'

export default {
    components: {
        Navbar,
        FooterBar,
        SideBar
    },
    computed: mapGetters('auth', ['isAuthenticated',]),
}
</script>

<template>
    <div>
        <navbar></navbar>
        <div class="container section">
            <div class="columns">
                <div class="column is-8">
                    <slot />
                </div>

                <div class="column is-4">
                    <side-bar />
                </div>
            </div>
        </div>

        <footer-bar />
    </div>
</template>
