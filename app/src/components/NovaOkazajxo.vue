<template>
    <q-layout>
        <q-toolbar slot="header">
            <q-btn flat @click="$router.go(-1)">
                <q-icon name="keyboard_arrow_left" />
            </q-btn>
            <q-toolbar-title>
                {{ $t('Nova Baterio Okazajxo') }}
            </q-toolbar-title>
        </q-toolbar>

        <div class="layout-padding">
            <q-list>
                <q-list-header>{{ $t('baterioOkazajxoDetaloj') }}</q-list-header>
                <q-item>
                    <q-item-main>
                        <q-field>
                            <q-select
                                v-model="loko"
                                :options="$store.state.lokoj"
                                :float-label="$t('La Loko de la Evento')"
                            />
                        </q-field>
                    </q-item-main>
                </q-item>
                <q-item>
                    <q-item-main>
                        <q-field
                            :error="!validaBaterioId"
                        >
                            <q-select
                                v-model="baterioId"
                                :options="$store.getters.bateriojPorSelect"
                                :float-label="$t('Baterio')"
                            />
                        </q-field>
                    </q-item-main>
                </q-item>
                <q-item>
                    <q-item-main>
                        <q-field
                            :error="false"
                        >
                            <q-select
                                v-model="ellasilon"
                                :options="ellasilonEbloj"
                                :float-label="$t('Ellasilon')"
                            />
                        </q-field>
                    </q-item-main>
                </q-item>
                <q-item>
                    <q-item-main>
                        <q-field
                            :error="tensioCxe0Modifita && !validaTensioCxe0"
                            :error-label="$t('Bonvolu Enmeti Valoron')"
                        >
                            <q-input
                                type="number"
                                v-model="tensioCxe0"
                                :float-label="$t('Tensio Cxe 0 Amps')"
                                @change="tensioCxe0Modifita = true"
                            />
                        </q-field>
                    </q-item-main>
                </q-item>
                <q-item>
                    <q-item-main>
                        <q-field
                            :error="tensioCxe18Modifita && !validaTensioCxe18"
                            :error-label="$t('Bonvolu Enmeti Valoron')"
                        >
                            <q-input
                                type="number"
                                v-model="tensioCxe18"
                                :float-label="$t('Tensio Cxe 18 Amps')"
                                @change="tensioCxe18Modifita = true"
                            />
                        </q-field>
                    </q-item-main>
                </q-item>
                <q-item>
                    <q-item-main>
                        <q-field
                            :error="rezistoModifita && !validaRezisto"
                            :error-label="$t('Bonvolu Enmeti Valoron')"
                        >
                            <q-input
                                type="number"
                                v-model="rezisto"
                                :float-label="$t('Rezisto (Ohms)')"
                                @change="rezistoModifita = true"
                            />
                        </q-field>
                    </q-item-main>
                </q-item>
                <q-item>
                    <q-item-main>
                        <q-field>
                            <q-input
                                type="textarea"
                                v-model="notoj"
                                :float-label="$t('Notoj')"
                            />
                        </q-field>
                    </q-item-main>
                </q-item>
                <q-item>
                    <q-item-main>
                        <q-field>
                            <q-btn
                                :disabled="!validaTensioCxe0 || !validaTensioCxe18 || !validaBaterioId || !validaRezisto"
                                color="primary"
                                @click="submit()"
                            >
                                {{ $t('sendu') }}
                            </q-btn>
                        </q-field>
                    </q-item-main>
                </q-item>
            </q-list>
        </div>
    </q-layout>
</template>

<script>
    import {
        QLayout,
        QModal,
        QModalLayout,
        QToolbar,
        QToolbarTitle,
        QIcon,
        QList,
        QListHeader,
        QItemSeparator,
        QField,
        QItem,
        QInput,
        QItemMain,
        QBtn,
        QSelect,
        Toast
    } from 'quasar'
    import { store } from '../store.js'

    export default {
        store,
        components: {
            QLayout,
            QModal,
            QModalLayout,
            QToolbar,
            QToolbarTitle,
            QIcon,
            QList,
            QListHeader,
            QItemSeparator,
            QField,
            QItem,
            QInput,
            QItemMain,
            QBtn,
            QSelect
        },
        methods: {
            submit () {
                Toast.create.positive(this.$t('Sukcese Aldonis Nova Baterio Okazajxo'))
                this.$router.go(-1)
            }
        },
        computed: {
            baterio () {
                return this.$store.state.baterioj.filter((baterio, index, arr) => {
                    return baterio.baterioId === this.baterioId
                })[0] || null
            },
            validaTensioCxe0 () {
                return typeof this.tensioCxe0 === typeof 1
            },
            validaTensioCxe18 () {
                return typeof this.tensioCxe18 === typeof 1
            },
            validaRezisto () {
                return typeof this.rezisto === typeof 1
            },
            validaBaterioId () {
                return this.baterioId !== ''
            }
        },
        data () {
            return {
                loko: this.$store.state.defauxltaLoko,
                tempo: new Date().getTime(),
                baterioId: '',
                okazajxoKey: '',
                okazajxoValue: '',
                tensioCxe0Modifita: false,
                tensioCxe0: null,
                tensioCxe18Modifita: false,
                tensioCxe18: null,
                rezistoModifita: false,
                rezisto: null,
                notoj: '',
                ellasilon: '',
                ellasilonEbloj: [
                    {
                        label: this.$t('Submetita al Matcxo'),
                        value: 'Submetita al Matcxo'
                    },
                    {
                        label: this.$t('Konektita al Cxarmo'),
                        value: 'Konektita al Cxarmo'
                    },
                    {
                        label: this.$t('Ricevis de Matcxo'),
                        value: 'Ricevis de Matcxo'
                    },
                    {
                        label: this.$t('Malkonektita de Cxarmo'),
                        value: 'Malkonektita de Cxarmo'
                    }
                ]
            }
        }
    }
</script>
