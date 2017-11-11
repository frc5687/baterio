<template>
    <q-item highlight>
        <q-item-main>
            <q-item-tile label>{{ baterioOkazaĵo.loko }}</q-item-tile>
            <q-item-tile sublabel>{{ baterioOkazaĵo.tempo }}</q-item-tile>
        </q-item-main>
        <q-item-side right icon="more_vert">
            <q-popover ref="popover">
                <q-list item-separator link>
                    <q-item @click="$refs.popover.close()">
                        <q-item-side icon="delete"/>
                        <q-item-main :label="$t('Forigi')" @click="deleteBatteryEvent()"/>
                    </q-item>
                </q-list>
            </q-popover>
        </q-item-side>
    </q-item>
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
    } from 'quasar'
    import { mapState } from 'vuex'

    export default {
        props: ['batteryEventId'],
        components: {
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
        },
        computed: mapState({
            baterioOkazaĵo (state) {
                return Object.assign({
                    loko: null,
                    tempo: 0,
                    baterioId: null,
                    ellasilon: null,
                    zorge: null,
                    tensioCxe0: null,
                    tensioCxe18: null,
                    rezisto: null,
                    notoj: null,
                }, state.baterioOkazajxoj[this.batteryEventId])
            },
        }),
        methods: {
            deleteBatteryEvent () {
                let self = this
                Dialog.create({
                    title: self.$t('Ĉu vi certas?'),
                    buttons: [
                        'Cancel',
                        {
                            label: self.$t('Konfirmi'),
                            handler () {
                                Toast.create.positive(self.$t('Baterio Okazaĵo Forigita'))
                                self.$store.dispatch('deleteBatteryEvent', self.batteryEventId)
                            },
                        },
                    ],
                })
            },
        },
    }
</script>
