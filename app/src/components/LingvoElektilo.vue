<template>
    <q-item>
        <q-item-main>
            <q-field icon="language" :helper="$t('frazo_elektuVianPreferatanLingvonPorMontriPagxojn')">
                <q-select v-model="elektitaLingvo" :options="lingvoj" @change="agordiLingvon()" :float-label="$t('lingvo')"/>
            </q-field>
        </q-item-main>
    </q-item>
</template>

<script>
    import { store } from '../store'
    import { mapState } from 'vuex'

    import {
        QField,
        QItem,
        QItemMain,
        QSelect,
    } from 'quasar'

    export default {
        components: {
            QField,
            QItem,
            QItemMain,
            QSelect,
        },
        methods: {
            agordiLingvon () {
                store.dispatch('agordiLingvon', this.elektitaLingvo)
            },
        },
        computed: mapState({
            lingvo: state => state.lingvo,
        }),
        mounted () {
            this.elektitaLingvo = this.lingvo
        },
        data () {
            return {
                elektitaLingvo: '',
                lingvoj: [
                    {
                        label: 'English',
                        value: 'en',
                    },
                    {
                        label: 'Esperanto',
                        value: 'eo',
                    },
                    {
                        label: 'Español',
                        value: 'es',
                    },
                    {
                        label: 'Italiano',
                        value: 'it',
                    },
                ],
            }
        },
    }
</script>
