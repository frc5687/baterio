<template>
    <q-layout ref="layout">
        <q-toolbar slot="header">
            <q-btn flat @click="$refs.layout.toggleLeft()">
                <q-icon name="menu" />
            </q-btn>

            <q-toolbar-title>
                {{ `${$t('baterio')}: ${baterio.baterioNomo}` }}
                <span slot="subtitle">baterio</span>
            </q-toolbar-title>

            <cta/>
        </q-toolbar>

        <korpo slot="left"/>

        <div class="layout-padding">
            <q-list no-border>
                <q-list-header>{{ $t('baterioDetaloj') }}</q-list-header>
                <q-item>
                    <q-item-main>
                        <q-item-tile label>{{ $t('baterioNomo') }}</q-item-tile>
                        <q-item-tile sublabel>{{ baterio.baterioNomo }}</q-item-tile>
                    </q-item-main>
                    <q-item-side right>
                        <q-item-tile icon="edit" color="primary" @click="redaktiNomon()"/>
                    </q-item-side>
                </q-item>
                <q-item>
                    <q-item-main>
                        <q-item-tile label>{{ $t('baterioModelo') }}</q-item-tile>
                        <q-item-tile sublabel>{{ baterio.modelo}}</q-item-tile>
                    </q-item-main>
                    <q-item-side right>
                        <q-item-tile icon="edit" color="primary"/>
                    </q-item-side>
                </q-item>
                <q-item-separator/>
                <q-list-header>{{ $t('Baterio Okazaĵoj') }}</q-list-header>
                <battery-event-item v-for="batteryEvent in Object.values($store.state.baterioOkazajxoj).filter((batteryEvent) => { return batteryEvent.baterioId === baterioId })" :key="batteryEvent.baterioOkazajxoId" :batteryEventId="batteryEvent.baterioOkazajxoId"/>
            </q-list>
        </div>
    </q-layout>
</template>

<script>
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
        Dialog,
        QItemTile,
        Toast,
        QItemSeparator,
    } from 'quasar'
    import { mapState } from 'vuex'
    import Cta from '../../Cta.vue'
    import Korpo from '../../Kesto/Korpo.vue'
    import BatteryEventItem from './BatteryEventItem.vue'

    export default {
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
            QPopover,
            QItemTile,
            QItemSeparator,
            BatteryEventItem,
        },
        computed: mapState({
            baterio (state) {
                return Object.assign({
                    baterioId: '',
                    baterioNomo: '',
                    modelo: '',
                }, state.baterioj[this.baterioId])
            },
        }),
        data () {
            return {
                baterioId: this.$route.params.baterioId,
            }
        },
        methods: {
            deleteBattery () {
                let self = this
                Dialog.create({
                    title: self.$t('Ĉu vi certas?'),
                    message: `${self.$t('Ĉi tio forigos')} ${self.baterio.baterioNomo}!`,
                    buttons: [
                        'Cancel',
                        {
                            label: self.$t('Konfirmi'),
                            handler () {
                                Toast.create.positive(self.$t('Baterio forigita'))
                                self.$store.dispatch('deleteBattery', self.baterioId)
                            },
                        },
                    ],
                })
            },
            redaktiNomon () {
                let self = this
                Dialog.create({
                    title: self.$t('Redakti Nomon'),
                    form: {
                        nomo: {
                            type: 'text',
                            label: self.$t('baterioNomo'),
                            model: self.baterio.baterioNomo,
                        },
                    },
                    buttons: [
                        'Cancel',
                        {
                            label: self.$t('sendu'),
                            handler (data) {
                                console.log(data)
                                console.log(self)
                                self.$store.dispatch('redaktiBaterio', Object.assign({}, self.baterio, {
                                    baterioNomo: data.nomo,
                                }))
                            },
                        },
                    ],
                })
            },
            redaktiModelo () {
                let self = this
                Dialog.create({
                    title: self.$t('Redakti Modelo'),
                    form: {
                        modelo: {
                            type: 'text',
                            label: self.$t('baterioModelo'),
                            model: '',
                        },
                    },
                    buttons: [
                        'Cancel',
                        {
                            label: self.$t('sendu'),
                            handler (data) {
                                console.log(data)
                                console.log(self)
                                self.$store.dispatch('redaktiBaterio', Object.assign({}, self.baterio, {
                                    modelo: data.modelo,
                                }))
                            },
                        },
                    ],
                })
            },
        },
    }
</script>
