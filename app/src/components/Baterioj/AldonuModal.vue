<template>
    <q-modal ref="modal" maximized :content-css="{minWidth: '80vw', minHeight: '80vh'}">
        <q-modal-layout>
            <q-toolbar slot="header">
                <q-btn flat @click="closeModal()">
                    <q-icon name="keyboard_arrow_left" />
                </q-btn>
                <q-toolbar-title>
                    {{ $t('novaBaterio') }}
                </q-toolbar-title>
            </q-toolbar>

            <div class="layout-padding">
                <q-list>
                    <q-list-header>{{ $t('baterioDetaloj') }}</q-list-header>
                    <q-item>
                        <q-item-main>
                            <q-field
                                :error="baterioNomoModifita && validaBaterioNomo"
                                :error-label="$t('baterioNomoTroMallonga')"
                                :helper="$t('laNomoDeLaBaterio')"
                            >
                                <q-input
                                    v-model="baterioNomo"
                                    :float-label="$t('baterioNomo')"
                                    @change="baterioNomoModifita = true"
                                />
                            </q-field>
                        </q-item-main>
                    </q-item>
                    <q-item>
                        <q-item-main>
                            <q-field
                                :error="baterioModeloModifita && validaBaterioModelo"
                                :error-label="$t('baterioModeloTroMallonga')"
                                :helper="$t('laModeloDeLaBaterio')"
                            >
                                <q-input
                                    v-model="baterioModelo"
                                    :float-label="$t('baterioModelo')"
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
                                    @click="submit()"
                                >
                                    {{ $t('sendu') }}
                                </q-btn>
                            </q-field>
                        </q-item-main>
                    </q-item>
                    <q-item-separator/>
                    <q-list-header>
                        *{{ $t('frazo_bateriojNurPovasEstiAldonitajDumInterrete') }}
                    </q-list-header>
                </q-list>
            </div>
        </q-modal-layout>
    </q-modal>
</template>

<script>
    import {
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
        Toast
    } from 'quasar'
    import { store } from '../../store.js'

    export default {
        store,
        components: {
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
            QBtn
        },
        methods: {
            openModal () {
                this.$refs.modal.open()
            },
            closeModal () {
                this.$refs.modal.close()
            },
            submit () {
                this.$store.dispatch('aldoniBaterio', {
                    baterioNomo: this.baterioNomo,
                    modelo: this.baterioModelo
                })
                this.closeModal()
                Toast.create.positive('Successfully Added New Battery')
                this.baterioNomoModifita = false
                this.baterioModeloModifita = false
                this.baterioNomo = ''
                this.baterioModelo = ''
            }
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
