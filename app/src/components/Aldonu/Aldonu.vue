<template>
    <q-layout ref="layout">
        <q-toolbar slot="header">
            <q-btn flat @click="$refs.layout.toggleLeft()">
                <q-icon name="menu" />
            </q-btn>

            <q-toolbar-title>
                Aldonu
                <span slot="subtitle">baterio</span>
            </q-toolbar-title>
        </q-toolbar>

        <korpo slot="left"/>

        <q-tabs slot="navigation">
            <q-route-tab
                icon="event_note"
                to="/aldonu"
                exact
                slot="title"
            >
                {{ $t('baterioOkazajxo') }}
            </q-route-tab>
            <q-route-tab
                icon="battery_std"
                to="/aldonu/baterio"
                exact
                slot="title"
            >
                {{ $t('baterio') }}
            </q-route-tab>
        </q-tabs>

        <router-view/>
    </q-layout>
</template>

<script>
    import Korpo from '../Kesto/Korpo.vue'

    import {
        QLayout,
        QToolbar,
        QToolbarTitle,
        QBtn,
        QIcon,
        QList,
        QListHeader,
        QTabs,
        QRouteTab
    } from 'quasar'

    export default {
        components: {
            Korpo,
            QLayout,
            QToolbar,
            QToolbarTitle,
            QBtn,
            QIcon,
            QList,
            QListHeader,
            QTabs,
            QRouteTab
        }
    }
</script>
