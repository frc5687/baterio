import Vue from 'vue'
import Vuex from 'vuex'
import {LocalStorage} from 'quasar'

Vue.use(Vuex)

let blankState = {
    lingvo: 'eo',
    kunsido: {
        kunsidonId: null,
        validaGxis: null
    }
}

let vuexState = Object.assign(blankState, (LocalStorage.get.item('vuexState') || {}))

export const store = new Vuex.Store({
    state: vuexState,
    getters: {
        neEkspiritaKunsido: state => {
            return state.kunsido.validaGxis !== null && new Date(state.kunsido.validaGxis) > new Date()
        }
    },
    mutations: {
        agordiLingvon (state, lingvo) {
            state.lingvo = lingvo
        },
        starigisNovanKunsidon (state, payload) {
            state.kunsido.kunsidonId = payload.kunsidonId
            state.kunsido.validaGxis = payload.validaGxis
        }
    },
    actions: {
        agordiLingvon ({ commit }, lingvo) {
            commit('agordiLingvon', lingvo)
            skribuVuexStateAlLokaStokado()
        },
        klaraKunsido ({ commit }) {
            commit('starigisNovanKunsidon', {
                kunsidonId: null,
                validaGxis: null
            })
        }
    }
})

export function skribuVuexStateAlLokaStokado () {
    console.info('%cstore.js: %cskribante vuex state al loka stokado', 'color: blue', 'color: green')
    let stateToWrite = JSON.parse(JSON.stringify(store.state))
    LocalStorage.set('vuexState', stateToWrite)
}
