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
    baterioj: [],
    baterioOkazajxoj: [],
    lokoj: [
        {
            label: 'Battle Of the Bay',
            value: '2017nhbb'
        },
        {
            label: 'Granite State',
            value: '2018nhgrs'
        },
        {
            label: 'New England District Championship',
            value: '2018necmp'
        }
    ],
    defauxltaLoko: '2017nhbb'
}

let vuexState = Object.assign(blankState, (LocalStorage.get.item('vuexState') || {}))

export const store = new Vuex.Store({
    state: vuexState,
    getters: {
        neEkspiritaKunsido: state => {
            return state.kunsido.validaGxis !== null && new Date(state.kunsido.validaGxis) > new Date()
        },
        defauxltaLoko: state => {
            return state.lokoj.filter((loko, index, arr) => {
                return loko.value === state.defauxltaLoko
            })[0] || null
        },
        bateriojPorSelect: state => {
            return state.baterioj.map(baterio => {
                return {
                    label: baterio.baterioNomo,
                    value: baterio.baterioId
                }
            })
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
        },
        aldoniBaterio (state, payload) {
            state.baterioj = [...state.baterioj, payload]
        },
        aldoniBaterioOkazajxo (state, payload) {
            state.baterioOkazajxo = [...state.baterioOkazajxo, payload]
        },
        redaktiBaterio (state, payload) {
            state.baterioj = state.baterioj.map(baterio => {
                if (baterio.baterioId === payload.baterioId) {
                    return Object.assign({}, baterio, payload)
                }
                else {
                    return baterio
                }
            })
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
        },
        aldoniBaterio ({ commit, state }, payload) {
            /*
            client.mutate({
                mutation: gql`
                    mutation ($kunsidonId: ID!, $baterioNomo: String!, $modelo: String!) {
                        baterio(kunsidonId: $kunsidonId) {
                            registriBaterio(baterioNomo: $baterioNomo, modelo: $modelo) {
                                baterio {
                                    baterioId
                                    baterioNomo
                                    modelo
                                }
                            }
                        }
                    }
                `,
                variables: {
                    kunsidonId: state.kunsido.kunsidonId,
                    baterioNomo: payload.baterioNomo,
                    modelo: payload.modelo
                }
            }).then(respondo => {
                commit('aldoniBaterio', {
                    baterioId: respondo.data.baterio.registriBaterio.baterio.baterioId,
                    baterioNomo: respondo.data.baterio.registriBaterio.baterio.baterioNomo
                })
            })
            */
            commit('aldoniBaterio', {
                baterioId: uuid4Gen(),
                baterioNomo: payload.baterioNomo,
                modelo: payload.modelo
            })
            skribuVuexStateAlLokaStokado()
        },
        aldoniBaterioOkazajxo ({ commit }, payload) {
            commit('aldoniBaterioOkazajxo', Object.assign({}, payload, {
                baterioOkazajxoIdL: uuid4Gen()
            }))
            skribuVuexStateAlLokaStokado()
        },
        redaktiBaterio ({ commit }, payload) {
            commit('redaktiBaterio', payload)
            skribuVuexStateAlLokaStokado()
        }
    }
})

export function skribuVuexStateAlLokaStokado () {
    console.info('%cstore.js: %cskribante vuex state al loka stokado', 'color: blue', 'color: green')
    let stateToWrite = JSON.parse(JSON.stringify(store.state))
    LocalStorage.set('vuexState', stateToWrite)
}

export function uuid4Gen () {
    let uuid = '', ii
    for (ii = 0; ii < 32; ii += 1) {
        switch (ii) {
        case 8:
        case 20:
            uuid += '-'
            uuid += (Math.random() * 16 | 0).toString(16)
            break
        case 12:
            uuid += '-'
            uuid += '4'
            break
        case 16:
            uuid += '-'
            uuid += (Math.random() * 4 | 8).toString(16)
            break
        default:
            uuid += (Math.random() * 16 | 0).toString(16)
        }
    }
    return uuid
}
