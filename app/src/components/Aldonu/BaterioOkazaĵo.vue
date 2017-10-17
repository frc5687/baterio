<template>
    <div class="layout-padding">
        <q-list>
            <q-list-header>{{ $t('baterioOkazajxoDetaloj') }}</q-list-header>
            <q-item>
                <q-item-main>
                    <q-field>
                        <q-select
                            :options="baterioElektuEblojn"
                            :v-model="elektitaBaterioId"
                        />
                    </q-field>
                </q-item-main>
            </q-item>
        </q-list>
    </div>
</template>

<script>
    import {
        QList,
        QListHeader,
        QItemSeparator,
        QField,
        QItem,
        QInput,
        QSelect,
        QItemMain,
        QBtn
    } from 'quasar'
    import { store } from '../../store'

    export default {
        store,
        components: {
            QList,
            QListHeader,
            QItemSeparator,
            QField,
            QItem,
            QInput,
            QSelect,
            QItemMain,
            QBtn
        },
        computed: {
            baterioElektuEblojn () {
                return this.$store.state.baterioj.map(function (baterio) {
                    return { label: baterio.baterioNomo, value: baterio.baterioId }
                })
            }
        },
        data () {
            return {
                elektitaBaterioId: { label: null, value: null }
            }
        },
        mounted () {
            this.$store.dispatch('akiriBaterioj')
        }
    }
</script>
