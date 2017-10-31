<template>
    <div>
        <q-list no-border link inset-delimiter>
            <q-list-header>{{ $t('kesto_navigi') }}</q-list-header>
            <q-side-link item to="/">
                <q-item-side icon="home"/>
                <q-item-main :label="$t('kesto_hejmo')"/>
            </q-side-link>
            <q-side-link item to="/baterioj">
                <q-item-side icon="battery_full"/>
                <q-item-main :label="$t('baterioj')"/>
            </q-side-link>
            <q-side-link item to="/agordojn">
                <q-item-side icon="settings"/>
                <q-item-main :label="$t('kesto_agordojn')"/>
            </q-side-link>
        </q-list>
    </div>
</template>

<script>
    import {
        QItemMain,
        QItemSide,
        QList,
        QListHeader,
        QSideLink
    } from 'quasar'

    export default {
        components: {
            QItemMain,
            QItemSide,
            QList,
            QListHeader,
            QSideLink
        },
        data () {
            return {}
        }
    }
</script>

<style>
</style>
