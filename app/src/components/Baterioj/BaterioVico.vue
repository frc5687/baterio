<template>
    <q-item link>
        <q-item-main>
            <q-item-tile label>{{ baterio.baterioNomo }}</q-item-tile>
            <q-item-tile sublabel>{{ baterio.modelo }}</q-item-tile>
        </q-item-main>
        <q-item-side right icon="more_vert">
            <q-popover ref="popover">
                <q-list item-separator link>
                    <q-item @click="$refs.popover.close()">
                        <q-item-main :label="$t('Redakti Nomon')" @click="redaktiNomon()"/>
                    </q-item>
                    <q-item @click="$refs.popover.close()">
                        <q-item-main :label="$t('Redakti Modelo')" @click="redaktiModelo()"/>
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
        QItemTile
    } from 'quasar'
    import { store } from '../../store.js'

    export default {
        store,
        props: ['baterio'],
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
            QItemTile
        },
        methods: {
            redaktiNomon () {
                let self = this
                Dialog.create({
                    title: self.$t('Redakti Nomon'),
                    form: {
                        nomo: {
                            type: 'text',
                            label: self.$t('baterioNomo'),
                            model: ''
                        }
                    },
                    buttons: [
                        'Cancel',
                        {
                            label: self.$t('sendu'),
                            handler (data) {
                                console.log(data)
                                console.log(self)
                                self.$store.dispatch('redaktiBaterio', Object.assign({}, self.baterio, {
                                    baterioNomo: data.nomo
                                }))
                            }
                        }
                    ]
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
                            model: ''
                        }
                    },
                    buttons: [
                        'Cancel',
                        {
                            label: self.$t('sendu'),
                            handler (data) {
                                console.log(data)
                                console.log(self)
                                self.$store.dispatch('redaktiBaterio', Object.assign({}, self.baterio, {
                                    modelo: data.modelo
                                }))
                            }
                        }
                    ]
                })
            }
        }
    }
</script>
