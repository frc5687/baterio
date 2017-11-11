import Vue from 'vue'
import VueRouter from 'vue-router'
import { store } from './store.js'

Vue.use(VueRouter)

function load (component) {
    // '@' is aliased to src/components
    return () => import(`@/${component}.vue`)
}

const router = new VueRouter({
    /*
     * NOTE! VueRouter "history" mode DOESN'T works for Cordova builds,
     * it is only to be used only for websites.
     *
     * If you decide to go with "history" mode, please also open /config/index.js
     * and set "build.publicPath" to something other than an empty string.
     * Example: '/' instead of current ''
     *
     * If switching back to default "hash" mode, don't forget to set the
     * build publicPath back to '' so Cordova builds work again.
     */

    routes: [
        { path: '/', redirect: '/hejmo' },
        { path: '/agordojn', component: load('Agordojn') },
        { path: '/hejmo', component: load('Hello') },
        { path: '/ensaluti', component: load('Ensaluti') },
        { path: '/baterioj', component: load('Baterioj/Baterioj') },
        { path: '/baterioj/baterio/:baterioId', component: load('Baterioj/Battery/Battery') },
        { path: '/novaOkazajxo', component: load('NovaOkazajxo') },
        { path: '/servilo', component: load('Servilo/Servilo') },
        { path: '*', component: load('Error404') },
    ],
})

router.beforeEach((al, de, poste) => {
    if (al.path.substring(0, 9) === '/ensaluti') {
        poste()
    }
    else {
        store.getters.neEkspiritaKunsido ? poste() : poste('/ensaluti')
    }
})

export default router
