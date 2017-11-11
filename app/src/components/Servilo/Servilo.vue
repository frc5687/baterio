<template>
    <q-layout ref="layout">
        <q-toolbar slot="header">
            <q-btn flat @click="$refs.layout.toggleLeft()">
                <q-icon name="menu" />
            </q-btn>

            <q-toolbar-title>
                {{ $t('Servilo') }}
                <span slot="subtitle">baterio</span>
            </q-toolbar-title>

            <cta/>
        </q-toolbar>

        <korpo slot="left"/>

        <div class="layout-padding">
            <p>
                Hi, the server is not quite ready to handle battery events, but do not worry, as your hard work
                recording battery events was not in vain!
            </p>
            <p>
                Click the below button to download your work, and email (or Slack) the file to John.
            </p>
            <p>
                The name of the file is "baterioStateSave-x.json", with x being a time stamp.
            </p>
            <q-btn @click="downloadState()">download</q-btn>
        </div>
    </q-layout>
</template>

<script>
    import { stateAsString } from '../../store.js'
    import Korpo from '../Kesto/Korpo.vue'
    import Cta from '../Cta.vue'
    import FileSaver from 'file-saver'

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
    } from 'quasar'

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
        },
        methods: {
            downloadState () {
                let blob = new Blob([stateAsString()], {type: 'text/json;charset=utf-8'})
                FileSaver.saveAs(blob, `baterioStateSave-${new Date().getTime()}.json`)
            },
        },
    }
</script>
