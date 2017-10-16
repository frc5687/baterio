<template>
    <div class="layout-padding">
        <q-list>
            <q-list-header>{{ $t('aldonu.baterioDetaloj') }}</q-list-header>
            <q-item>
                <q-item-main>
                    <q-field
                        :error="baterioNomoModifita && validaBaterioNomo"
                        :error-label="$t('aldonu.baterioNomoTroMallonga')"
                        :helper="$t('aldonu.laNomoDeLaBaterio')"
                    >
                        <q-input
                            v-model="baterioNomo"
                            :float-label="$t('aldonu.baterioNomo')"
                            @change="baterioNomoModifita = true"
                        />
                    </q-field>
                </q-item-main>
            </q-item>
            <q-item>
                <q-item-main>
                    <q-field
                        :error="baterioModeloModifita && validaBaterioModelo"
                        :error-label="$t('aldonu.baterioModeloTroMallonga')"
                        :helper="$t('aldonu.laModeloDeLaBaterio')"
                    >
                        <q-input
                            v-model="baterioModelo"
                            :float-label="$t('aldonu.baterioModelo')"
                            @change="baterioModeloModifita = true"
                        />
                    </q-field>
                </q-item-main>
            </q-item>
            <q-item>
                <q-item-main>
                    <q-field>
                        <q-btn
                            :disabled="!baterioNomo || !baterioModelo"
                            color="primary"
                        >
                            {{ $t('aldonu.sendu') }}
                        </q-btn>
                    </q-field>
                </q-item-main>
            </q-item>
            <q-item-separator/>
            <q-list-header>
                *{{ $t('aldonu.bateriojNurPovasEstiAldonitajDumInterrete') }}
            </q-list-header>
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
        QItemMain,
        QBtn
    } from 'quasar'

    export default {
        components: {
            QList,
            QListHeader,
            QItemSeparator,
            QField,
            QItem,
            QInput,
            QItemMain,
            QBtn
        },
        computed: {
            validaBaterioNomo () {
                return this.baterioNomo.length === 0
            },
            validaBaterioModelo () {
                return this.baterioModelo.length === 0
            }
        },
        data () {
            return {
                baterioNomoModifita: false,
                baterioModeloModifita: false,
                baterioNomo: '',
                baterioModelo: ''
            }
        }
    }
</script>
