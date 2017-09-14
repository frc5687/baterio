import Vue from 'vue'
import Vuex from 'vuex'
import {LocalStorage} from 'quasar'

Vue.use(Vuex)

let blankState = {
    lingvo: 'eo',
    kunsido: {
        kunsidoId: null,
        validaĜis: null
    }
}

let vuexState = Object.assign(blankState, (LocalStorage.get.item('vuexState') || {}))

export const store = new Vuex.Store({
    state: vuexState,
    getters: {
        neEkspiritaKunsido: state => {
            return state.kunsido.validaĜis !== null && new Date(state.kunsido.validaĜis) > new Date()
        }
    },
    mutations: {
        agordiLingvon (state, lingvo) {
            state.lingvo = lingvo
        }
    },
    actions: {
        agordiLingvon ({ commit }, lingvo) {
            commit('agordiLingvon', lingvo)
            skribuVuexStateAlLokaStokado()
        }
    }
})

export function skribuVuexStateAlLokaStokado () {
    console.info('%cstore.js: %cskribante vuex state al loka stokado', 'color: blue', 'color: green')
    let stateToWrite = JSON.parse(JSON.stringify(store.state))
    LocalStorage.set('vuexState', stateToWrite)
}
