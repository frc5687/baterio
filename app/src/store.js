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
        validaGxis: null,
    },
    baterioj: {},
    baterioOkazajxoj: {},
    lokoj: [
        {
            label: 'Battle Of the Bay',
            value: '2017nhbb',
        },
        {
            label: 'Granite State',
            value: '2018nhgrs',
        },
        {
            label: 'New England District Championship',
            value: '2018necmp',
        },
    ],
    defauxltaLoko: '2017nhbb',
}

let vuexState = Object.assign(blankState, (LocalStorage.get.item('baterioVuexState') || {}))

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
            return Object.values(state.baterioj).map(baterio => {
                return {
                    label: baterio.baterioNomo,
                    value: baterio.baterioId,
                }
            })
        },
    },
    mutations: {
        agordiLingvon (state, lingvo) {
            state.lingvo = lingvo
        },
        starigisNovanKunsidon (state, payload) {
            state.kunsido.kunsidonId = payload.kunsidonId
            state.kunsido.validaGxis = payload.validaGxis
        },
        aldoniBaterio (state, payload) {
            Vue.set(state.baterioj, payload.baterioId, payload)
        },
        aldoniBaterioOkazajxo_ (state, payload) {
            Vue.set(state.baterioOkazajxoj, payload.baterioOkazajxoId, payload)
        },
        redaktiBaterio (state, payload) {
            Vue.set(state.baterioj, payload.baterioId, payload)
        },
        deleteBattery_ (state, batteryId) {
            Vue.delete(state.baterioj, batteryId)
        },
        deleteBatteryEvent_ (state, batteryEventId) {
            Vue.delete(state.baterioOkazajxoj, batteryEventId)
        },
    },
    actions: {
        /**
         * Delete a battery event from the vuex store
         * @param commit
         * @param batteryEventId
         */
        deleteBatteryEvent ({ commit }, batteryEventId) {
            commit('deleteBatteryEvent_', batteryEventId)
            skribuVuexStateAlLokaStokado()
        },
        /**
         * Delete a battery (remote & local)
         * @param state
         * @param commit
         * @param batteryId
         */
        deleteBattery ({ state, commit }, batteryId) {
            client.mutate({
                mutation: gql`
                    mutation ($kunsidonId: ID!, $baterioId: String!) {
                        baterio(kunsidonId: $kunsidonId) {
                            forigiBaterio(baterioId: $baterioId) {
                                estisSukcesa
                            }
                        }
                    }
                `,
                variables: {
                    kunsidonId: state.kunsido.kunsidonId,
                    baterioId: batteryId,
                },
            }).then(respondo => {
                commit('deleteBattery_', batteryId)
                skribuVuexStateAlLokaStokado()
            })
        },
        /**
         * Sets the preferred langauge string for i18n
         * @param commit
         * @param {string} lingvo
         */
        agordiLingvon ({ commit }, lingvo) {
            commit('agordiLingvon', lingvo)
            skribuVuexStateAlLokaStokado()
        },
        /**
         * Locally nullifies the session info
         * @param commit
         */
        klaraKunsido ({ commit }) {
            commit('starigisNovanKunsidon', {
                kunsidonId: null,
                validaGxis: null,
            })
        },
        /**
         * Fetches and commits batteries from server
         * @param commit
         * @param state
         */
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
                    kunsidonId: state.kunsido.kunsidonId,
                },
            }).then(respondo => {
                respondo.data.baterio.baterioj.forEach((baterio) => commit('aldoniBaterio', baterio))
                skribuVuexStateAlLokaStokado()
            })
        },
        /**
         * Register a new battery (remote & local)
         * @param commit
         * @param state
         * @param {object} payload the battery object to add
         */
        aldoniBaterio ({ commit, state }, payload) {
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
                    modelo: payload.modelo,
                },
            }).then(respondo => {
                commit('aldoniBaterio', {
                    baterioId: respondo.data.baterio.registriBaterio.baterio.baterioId,
                    baterioNomo: respondo.data.baterio.registriBaterio.baterio.baterioNomo,
                    modelo: respondo.data.baterio.registriBaterio.baterio.modelo,
                })
                skribuVuexStateAlLokaStokado()
            })
        },
        /**
         * Adds battery event to vuex state
         * @param commit
         * @param {object} payload
         */
        aldoniBaterioOkazajxo ({ commit }, payload) {
            console.log(payload)
            let newPayload = { ...payload, baterioOkazajxoId: uuid4Gen() }
            console.log(newPayload)
            commit('aldoniBaterioOkazajxo_', newPayload)
            skribuVuexStateAlLokaStokado()
        },
        /**
         * Make changes to battery name & model (remote & local)
         * @param state
         * @param commit
         * @param payload
         */
        redaktiBaterio ({ state, commit }, payload) {
            client.mutate({
                mutation: gql`
                    mutation ($kunsidonId: ID!, $baterioId: ID!, $baterioNomo: String!, $modelo: String!) {
                        baterio(kunsidonId: $kunsidonId) {
                            gxisdatigoBaterioNomo(baterioId: $baterioId, novaBaterioNomo: $baterioNomo) {
                                baterio {
                                    baterioId
                                    baterioNomo
                                    modelo
                                }
                            }
                            gxisdatigoBaterioModelo(baterioId: $baterioId, novaBaterioModelo: $modelo) {
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
                    baterioId: payload.baterioId,
                    baterioNomo: payload.baterioNomo,
                    modelo: payload.modelo,
                },
            }).then(respondo => {
                commit('aldoniBaterio', {
                    baterioId: respondo.data.baterio.gxisdatigoBaterioModelo.baterio.baterioId,
                    baterioNomo: respondo.data.baterio.gxisdatigoBaterioModelo.baterio.baterioNomo,
                    modelo: respondo.data.baterio.gxisdatigoBaterioModelo.baterio.modelo,
                })
                skribuVuexStateAlLokaStokado()
            })
        },
    },
})

export function skribuVuexStateAlLokaStokado () {
    console.info('%cstore.js: %cskribante vuex state al loka stokado', 'color: blue', 'color: green')
    let stateToWrite = JSON.parse(JSON.stringify(store.state))
    LocalStorage.set('baterioVuexState', stateToWrite)
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
