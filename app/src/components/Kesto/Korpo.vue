<template>
    <div>
        <q-list no-border link inset-delimiter>
            <q-list-header>{{ $t('kesto.korpo.navigi') }}</q-list-header>
            <q-side-link item to="/">
                <q-item-side icon="home" />
                <q-item-main :label="$t('kesto.korpo.hejmo')"/>
            </q-side-link>
            <q-side-link item to="/agordojn">
                <q-item-side icon="settings" />
                <q-item-main :label="$t('kesto.korpo.agordojn')"/>
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
