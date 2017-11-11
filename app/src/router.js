import Vue from 'vue'
import VueRouter from 'vue-router'
import { store } from './store.js'

import Servilo from '@/Servilo/Servilo.vue'
import Error404 from '@/Error404.vue'
import Agordojn from '@/Agordojn.vue'
import Hello from '@/Hello.vue'
import Ensaluti from '@/Ensaluti.vue'
import Baterioj from '@/Baterioj/Baterioj.vue'
import Battery from '@/Baterioj/Battery/Battery.vue'
import NovaOkazajxo from '@/NovaOkazajxo.vue'

Vue.use(VueRouter)

/*
 * Uncomment this section and use "load()" if you want
 * to lazy load routes.
function load (component) {
  // '@' is aliased to src/components
  return () => import(`@/${component}.vue`)
}
*/

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
        { path: '/agordojn', component: Agordojn },
        { path: '/hejmo', component: Hello },
        { path: '/ensaluti', component: Ensaluti },
        { path: '/baterioj', component: Baterioj },
        { path: '/baterioj/baterio/:baterioId', component: Battery },
        { path: '/novaOkazajxo', component: NovaOkazajxo },
        { path: '/servilo', component: Servilo },
        { path: '*', component: Error404 },
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
