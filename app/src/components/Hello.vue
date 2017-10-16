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
            <p>{{ $t('saluton') }}</p>
        </div>
    </q-layout>
</template>

<script>
    import Korpo from './Kesto/Korpo.vue'

    import {
        QLayout,
        QToolbar,
        QToolbarTitle,
        QBtn,
        QIcon,
        QList,
        QListHeader
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
            QListHeader
        }
    }
</script>
