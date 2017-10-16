<template>
    <q-layout ref="layout">
        <q-toolbar slot="header">
            <q-btn flat @click="$refs.layout.toggleLeft()">
                <q-icon name="menu" />
            </q-btn>

            <q-toolbar-title>
                baterio
            </q-toolbar-title>
        </q-toolbar>

        <korpo slot="left"/>

        <div class="layout-padding">
            <lingvo-elektilo/>
            <div class="row items-center justify-center content-center" style="height: 60vh;">
                <div>
                    <p class="text-center">{{ $t('bonvoluEnsaluti') }}</p>
                    <br>
                    <div class="row justify-around">
                        <img src="~assets/btn_google_signin_light_normal_web.png" @click="signIn()"/>
                    </div>
                </div>
            </div>
        </div>
    </q-layout>
</template>

<script>
    import Vue from 'vue'
    import { store, skribuVuexStateAlLokaStokado } from '../store'
    import { mapState, mapActions } from 'vuex'
    import Korpo from './Kesto/Korpo.vue'
    import LingvoElektilo from './LingvoElektilo.vue'
    import { client } from '../main.js'
    import gql from 'graphql-tag'

    import {
        QLayout,
        QToolbar,
        QToolbarTitle,
        QBtn,
        QIcon,
        Toast
    } from 'quasar'

    export default {
        store,
        components: {
            LingvoElektilo,
            Korpo,
            QLayout,
            QToolbar,
            QToolbarTitle,
            QBtn,
            QIcon
        },
        computed: mapState({
            session: state => state.session
        }),
        methods: {
            ...mapActions([]),
            signIn () {
                Vue.googleAuth().directAccess()
                Vue.googleAuth().signIn(this.onSignInSuccess, this.onSignInError)
            },
            onSignInSuccess (googleUser) {
                console.log('Google User: %o', googleUser)
                let aliroToken = googleUser.Zi.access_token
                console.log('Aliro Token: %o', aliroToken)

                let mem = this

                client.mutate({
                    mutation: gql`
                        mutation ($aliroToken: ID!) {
                            kreiKunsidonKunGoogle (aliroToken: $aliroToken) {
                                kunsidon {
                                    kunsidonId
                                    validaGxis
                                }
                            }
                        }
                    `,
                    variables: {
                        aliroToken: aliroToken
                    }
                }).then(respondo => {
                    console.log(respondo)
                    mem.$store.commit('starigisNovanKunsidon', respondo.data.kreiKunsidonKunGoogle.kunsidon)
                    skribuVuexStateAlLokaStokado()
                    mem.$router.push('/')
                })
            },
            onSignInError (error) {
                console.log('Error while Signing In', error)
                Toast.create.negative({
                    html: this.$t('mesagxoj.eraroDumSubskribo')
                })
            }
        },
        data () {
            return {}
        }
    }
</script>
