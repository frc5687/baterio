// === DEFAULT / CUSTOM STYLE ===
// WARNING! always comment out ONE of the two require() calls below.
// 1. use next line to activate CUSTOM STYLE (./src/themes)
require(`./themes/app.${__THEME}.styl`)
// 2. or, use next line to activate DEFAULT QUASAR STYLE
// require(`quasar/dist/quasar.${__THEME}.css`)
// ==============================

// Uncomment the following lines if you need IE11/Edge support
// require(`quasar/dist/quasar.ie`)
// require(`quasar/dist/quasar.ie.${__THEME}.css`)

import Vue from 'vue'
import Quasar, { AddressbarColor } from 'quasar'
import router from './router'
import VueI18n from 'vue-i18n'
import GoogleAuth from 'vue-google-oauth'
import ApolloClient, { createNetworkInterface } from 'apollo-client'
Vue.config.productionTip = false
Vue.use(Quasar) // Install Quasar Framework
AddressbarColor.set('#BE1E2D')
Vue.use(VueI18n)
Vue.use(GoogleAuth, {
    client_id: '525115740517-1u093g1gav6fl7a4scafie5la3cggdqg.apps.googleusercontent.com',
    scope: 'https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile',
})
Vue.googleAuth().load()

import { messages } from './i18n'
import { store } from './store'

export const i18n = new VueI18n({
    locale: store.state.lingvo,
    messages,
})

store.subscribe((mutation, state) => {
    if (mutation.type === 'agordiLingvon') {
        i18n.locale = state.lingvo
    }
})

if (__THEME === 'mat') {
    require('quasar-extras/roboto-font')
}
import 'quasar-extras/material-icons'
// import 'quasar-extras/ionicons'
// import 'quasar-extras/fontawesome'
// import 'quasar-extras/animate'

let uri = 'http://localhost:8000/graphql'

if (PROD) {
    uri = 'https://baterio.jcharante.com/graphql'
}

export const client = new ApolloClient({
    networkInterface: createNetworkInterface({ uri }),
})

Quasar.start(() => {
    /* eslint-disable no-new */
    new Vue({
        el: '#q-app',
        i18n,
        store,
        router,
        render: h => h(require('./App')),
    })
})
