/*
Vue i18n havas problemojn kun unikodaj klavoj.
Pro tio ni uzas la x-notacion.
 */

export const messages = {
    eo: {
        kesto_hejmo: 'Hejmo',
        kesto_navigi: 'Navigi',
        kesto_agordojn: 'Agordojn',
        kesto_aldonu: 'Aldonu',
        baterio: 'Baterio',
        baterioOkazajxo: 'Baterio Okazaĵo',
        baterioNomo: 'Baterio Nomo',
        baterioModelo: 'Baterio Modelo',
        laNomoDeLaBaterio: 'La Nomo de la Baterio',
        laModeloDeLaBaterio: 'La Modelo de la Baterio',
        frazo_bateriojNurPovasEstiAldonitajDumInterrete: 'Baterioj nur povas esti aldonitaj dum interrete',
        sendu: 'Sendu',
        baterioModeloTroMallonga: 'Baterio Modelo Tro Mallonga',
        baterioNomoTroMallonga: 'Baterio Nomo Tro Mallonga',
        baterioDetaloj: 'Baterio Detaloj',
        saluton: 'Saluton',
        bonvoluEnsaluti: 'Bonvolu Ensaluti',
        eraroDumSubskribo: 'Eraro dum subskribo',
        provoViaAuxdado: 'Provo via auxdado',
        elsaluti: 'Elsaluti',
        haltuTono: 'Haultu tono',
        lingvo: 'Lingvo',
        frazo_elektuVianPreferatanLingvonPorMontriPagxojn: 'Elektu vian preferatan lingvon por montri paĝojn',
        baterioOkazajxoDetaloj: 'Baterio Okazaĵo Detaloj'
    }
}

messages.en = Object.assign({}, messages.eo, {
    kesto_hejmo: 'Home',
    kesto_navigi: 'Navigate',
    kesto_agordojn: 'Settings',
    kesto_aldonu: 'Add',
    baterio: 'Battery',
    baterioOkazajxo: 'Battery Event',
    baterioNomo: 'Battery Name',
    baterioModelo: 'Battery Model',
    laNomoDeLaBaterio: 'The Battery\'s Name',
    laModeloDeLaBaterio: 'The Battery\'s Model',
    frazo_bateriojNurPovasEstiAldonitajDumInterrete: 'Batteries can only be added while online',
    sendu: 'Submit',
    baterioModeloTroMallonga: 'Battery Model Too Short',
    baterioNomoTroMallonga: 'Battery Name Too Short',
    baterioDetaloj: 'Battery Details',
    saluton: 'Hello',
    bonvoluEnsaluti: 'Please sign in',
    eraroDumSubskribo: 'Error while signing in',
    provoViaAuxdado: 'Test your hearing',
    elsaluti: 'Sign out',
    haltuTono: 'Stop Tone',
    lingvo: 'Language',
    frazo_elektuVianPreferatanLingvonPorMontriPagxojn: 'Choose your preferred language to display pages',
    baterioOkazajxoDetaloj: 'Battery Event Details'
})

messages.es = Object.assign({}, messages.eo, {
    kesto_hejmo: 'Inicio',
    kesto_navigi: 'Navegar',
    kesto_agordojn: 'Opciones',
    kesto_aldonu: 'Agregar',
    baterio: 'Batería',
    baterioOkazajxo: 'Evento de Bateria',
    baterioNomo: 'Nombre de la Batería',
    baterioModelo: 'Modela de la Batería',
    laNomoDeLaBaterio: 'El Nombre de la Batería',
    laModeloDeLaBaterio: 'El Modelo de la Batería',
    frazo_bateriojNurPovasEstiAldonitajDumInterrete: 'Solo puedes agregar baterias mientras estás en línea.',
    sendu: 'Enviar',
    baterioModeloTroMallonga: 'Modelo de batería demasiado corto',
    baterioNomoTroMallonga: 'Nombre de batería demasiado corto',
    baterioDetaloj: 'Detalles de la Batería',
    saluton: 'Hola',
    bonvoluEnsaluti: 'Por favor entrar a tu cuenta',
    eraroDumSubskribo: 'Error cuando tratamos al entrar a tu cuenta',
    provoViaAuxdado: 'Prueba tu audición',
    elsaluti: 'Salga de su cuenta',
    haltuTono: 'Detener el tono',
    lingvo: 'Idioma',
    frazo_elektuVianPreferatanLingvonPorMontriPagxojn: 'Seleccione su idioma favorito para mostrar páginas'
})

messages.it = Object.assign({}, messages.eo, {
    kesto_agordojn: 'Opzioni',
    lingvo: 'Lingua',
    frazo_elektuVianPreferatanLingvonPorMontriPagxojn: 'Scegli la lingua preferita per visualizzare le pagine',
    hejmo: 'Anteriore'
})
