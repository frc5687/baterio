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
            <q-list>
                <lingvo-elektilo/>
                <q-item-separator/>
                <q-list-header>{{ $t('mesagxoj.provoViaAuxdado') }}</q-list-header>
                <q-item>
                    <div class="row justify-around" style="width: 100%">
                        <q-btn @click="ĉagreniAliajn(40)">40hz</q-btn>
                        <q-btn @click="ĉagreniAliajn(400)">400hz</q-btn>
                        <q-btn @click="ĉagreniAliajn(15000)">15khz</q-btn>
                        <q-btn @click="ĉagreniAliajn(17000)">17khz</q-btn>
                        <q-btn @click="ĉagreniAliajn(19000)">19khz</q-btn>
                    </div>
                </q-item>
                <q-item>
                    <div class="row justify-around" style="width: 100%">
                        <q-btn @click="haltuTono()" color="secondary">{{ $t('mesagxoj.haltuTono') }}</q-btn>
                    </div>
                </q-item>
                <q-item-separator/>
                <q-item>
                    <div class="row justify-around" style="width: 100%">
                        <q-btn @click="elsaluti()" color="negative">{{ $t('mesagxoj.elsaluti') }}</q-btn>
                    </div>
                </q-item>
            </q-list>
        </div>
    </q-layout>
</template>

<script>
    import { store } from '../store'
    import Korpo from './Kesto/Korpo.vue'
    import LingvoElektilo from './LingvoElektilo.vue'

    import {
        QLayout,
        QToolbar,
        QToolbarTitle,
        QBtn,
        QIcon,
        QList,
        QListHeader,
        QField,
        QItem,
        QItemMain,
        QSelect,
        QItemSeparator
    } from 'quasar'

    export default {
        store,
        components: {
            Korpo,
            LingvoElektilo,
            QLayout,
            QToolbar,
            QToolbarTitle,
            QBtn,
            QIcon,
            QList,
            QListHeader,
            QField,
            QItem,
            QItemMain,
            QSelect,
            QItemSeparator
        },
        mounted () {
            this.audioContext = new AudioContext()
            this.osc = this.audioContext.createOscillator()
            this.osc.frequency.value = 0
            this.osc.connect(this.audioContext.destination)
        },
        data () {
            return {
                audioContext: null,
                osc: null,
                ludas: false
            }
        },
        methods: {
            haltuTono () {
                if (this.ludas) {
                    this.osc.stop()
                    this.ludas = false
                }
            },
            ĉagreniAliajn (ofteco) {
                this.osc.frequency.value = ofteco
                if (!this.ludas) {
                    this.osc.start()
                }
                this.ludas = true
            },
            elsaluti () {
                this.$store.dispatch('klaraKunsido')
                this.$router.push('/')
            }
        }
    }
</script>
