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

        <div class="layout-padding">
            <p>Hello</p>
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
        QListHeader
    } from 'quasar'

    export default {
        components: {
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
