<template>
    <q-btn flat>
        <q-icon name="add"/>
        <q-popover ref="popover">
            <q-list>
                <q-item link @click="$router.push('/novaOkazajxo')">
                    <q-item-side icon="photo_camera"/>
                    <q-item-main>
                        <q-item-tile label>{{ $t('Skani QR Kodo') }}</q-item-tile>
                    </q-item-main>
                </q-item>
                <q-item link @click="$router.push('/novaOkazajxo')">
                    <q-item-side icon="list"/>
                    <q-item-main>
                        <q-item-tile label>{{ $t('Nova Baterio Okazajxo') }}</q-item-tile>
                    </q-item-main>
                </q-item>
            </q-list>
        </q-popover>
    </q-btn>
</template>

<script>
    import {
        QBtn,
        QIcon,
        QPopover,
        QList,
        QItem,
        QItemMain,
        QItemSide,
        QItemTile,
    } from 'quasar'

    export default {
        components: {
            QBtn,
            QIcon,
            QPopover,
            QList,
            QItem,
            QItemMain,
            QItemSide,
            QItemTile,
        },
    }
</script>
