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
                <q-item>
                    <q-item-main>
                        <q-field icon="language" :helper="$t('agordojn.elektuVianPreferatanLingvonPorMontriPagxojn')">
                            <q-select v-model="elektitaLingvo" :options="lingvoj" @change="agordiLingvon()" :float-label="$t('agordojn.lingvo')"/>
                        </q-field>
                    </q-item-main>
                </q-item>
            </q-list>
        </div>
    </q-layout>
</template>

<script>
    import { store } from '../store'
    import { mapState } from 'vuex'
    import Korpo from './Kesto/Korpo.vue'

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
        QSelect
    } from 'quasar'

    export default {
        store,
        components: {
            Korpo,
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
            QSelect
        },
        computed: mapState({
            lingvo: state => state.lingvo
        }),
        mounted () {
            this.elektitaLingvo = this.lingvo
        },
        data () {
            return {
                elektitaLingvo: '',
                lingvoj: [
                    {
                        label: 'English',
                        value: 'en'
                    },
                    {
                        label: 'Esperanto',
                        value: 'eo'
                    }
                ]
            }
        },
        methods: {
            agordiLingvon () {
                store.dispatch('agordiLingvon', this.elektitaLingvo)
                // i18n.locale = this.elektitaLingvo
            }
        }
    }
</script>
