<template>
    <q-layout ref="layout">
        <q-toolbar slot="header">
            <q-btn flat @click="$refs.layout.toggleLeft()">
                <q-icon name="menu" />
            </q-btn>

            <q-toolbar-title>
                {{ $t('baterioj') }}
                <span slot="subtitle">baterio</span>
            </q-toolbar-title>
        </q-toolbar>

        <korpo slot="left"/>

        <div class="layout-padding">
            <q-search v-model="query"/>
            <q-list>
                <q-item link>
                    <q-item-main label="Butterfingers"/>
                </q-item>
                <q-item link>
                    <q-item-main label="Rick looks like Duffy"/>
                </q-item>
            </q-list>
        </div>
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
        QRouteTab,
        QItem,
        QItemMain,
        QItemSide,
        QSearch
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
            QRouteTab,
            QItem,
            QItemMain,
            QItemSide,
            QSearch
        },
        data () {
            return {
                query: ''
            }
        }
    }
</script>
