<template>
    <q-layout ref="layout">
        <q-toolbar slot="header">
            <q-btn flat @click="$refs.layout.toggleLeft()">
                <q-icon name="menu" />
            </q-btn>

            <q-toolbar-title>
                baterio
            </q-toolbar-title>

            <q-btn flat @click="$router.push('/novaOkazajxo')">
                <q-icon name="add"/>
            </q-btn>
        </q-toolbar>

        <korpo slot="left"/>

        <div class="layout-padding">
            <q-list>
                <lingvo-elektilo/>
                <q-item-separator/>
                <q-item>
                    <div class="row justify-around" style="width: 100%">
                        <q-btn @click="elsaluti()" color="negative">{{ $t('elsaluti') }}</q-btn>
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
        QItemSeparator,
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
            QItemSeparator,
        },
        methods: {
            elsaluti () {
                this.$store.dispatch('klaraKunsido')
                this.$router.push('/')
            },
        },
    }
</script>
