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

            <cta/>
        </q-toolbar>

        <korpo slot="left"/>

        <div class="layout-padding">
            <aldonu-modal ref="aldonuModal"/>

            <q-fixed-position corner="bottom-right" :offset="[18, 18]">
                <q-btn round icon="add" color="primary" @click="$refs.aldonuModal.openModal()"></q-btn>
            </q-fixed-position>
            <q-search v-model="query"/>
            <q-list>
                <baterio-vico :baterioId="baterioId" v-for="baterioId in Object.keys($store.state.baterioj)" :key="baterioId"/>
            </q-list>
        </div>
    </q-layout>
</template>

<script>
    import Korpo from '../Kesto/Korpo.vue'
    import AldonuModal from './AldonuModal.vue'
    import BaterioVico from './BaterioVico.vue'
    import Cta from '../Cta.vue'
    import { store } from '../../store.js'

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
        QSearch,
        QFixedPosition,
        QPopover,
    } from 'quasar'

    export default {
        store,
        components: {
            Cta,
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
            QSearch,
            QFixedPosition,
            AldonuModal,
            QPopover,
            BaterioVico,
        },
        mounted () {
            this.$store.dispatch('akiriBaterioj')
        },
        data () {
            return {
                query: '',
            }
        },
    }
</script>
