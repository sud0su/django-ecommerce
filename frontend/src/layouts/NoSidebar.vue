<script>
import NavBar from '@/components/Navbar'
import FooterBar from '@/components/Footer'

export default {
    components: {
        NavBar,
        FooterBar
    }
}
</script>

<template>
    <div>
        <nav-bar />
        <div class="container">
            <slot />
        </div>

        <footer-bar />
    </div>
</template>
