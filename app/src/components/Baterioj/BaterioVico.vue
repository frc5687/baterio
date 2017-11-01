<template>
    <q-item link>
        <q-item-main :label="baterio.baterioNomo"/>
        <q-item-side right icon="more_vert">
            <q-popover ref="popover">
                <q-list item-separator link>
                    <q-item @click="$refs.popover.close()">
                        <q-item-main label="Edit Name"/>
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
        QPopover
    } from 'quasar'

    export default {
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
            QPopover
        }
    }
</script>
