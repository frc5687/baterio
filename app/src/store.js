import Vue from 'vue'
import Vuex from 'vuex'
import {LocalStorage} from 'quasar'
import { client } from './main.js'
import gql from 'graphql-tag'

Vue.use(Vuex)

let blankState = {
    lingvo: 'eo',
    kunsido: {
        kunsidonId: null,
        validaGxis: null
    },
    baterioj: []
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
        },
        starigisBaterioj (state, payload) {
            state.baterioj = payload
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
        },
        akiriBaterioj ({ commit, state }) {
            client.query({
                query: gql`
                    query ($kunsidonId: ID!) {
                        baterio (kunsidonId: $kunsidonId) {
                            baterioj {
                                baterioNomo
                                baterioId
                                modelo
                            }
                        }
                    }
                `,
                variables: {
                    kunsidonId: state.kunsido.kunsidonId
                }
            }).then(respondo => {
                commit('starigisBaterioj', respondo.data.baterio.baterioj)
            })
        }
    }
})

export function skribuVuexStateAlLokaStokado () {
    console.info('%cstore.js: %cskribante vuex state al loka stokado', 'color: blue', 'color: green')
    let stateToWrite = JSON.parse(JSON.stringify(store.state))
    LocalStorage.set('vuexState', stateToWrite)
}
