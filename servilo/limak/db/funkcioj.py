from uuid import uuid4
import datetime
from limak.db import DBKunsido, KunsidoV1, UzantoV2
from limak import db
from limak.api import esceptoj, types
import bcrypt
from typing import Tuple, List


def krei_baterio(baterio_nomo: str, modelo: str, baterio_id=None) -> str:
	"""
	Krei la baterio kaj revenu la baterio_id
	:param baterio_nomo:
	:param modelo:
	:param baterio_id:
	:return:
	"""
	baterio_id = str(uuid4()) if baterio_id is None else baterio_id
	db_kunsido = DBKunsido()
	db_kunsido.add(db.BaterioV1(
		baterio_id=baterio_id,
		baterio_nomo=baterio_nomo,
		modelo=modelo
	))
	db_kunsido.commit()
	db_kunsido.close()
	return baterio_id


def krei_baterio_okazaĵo(baterio_id: str, data: dict, okazaĵo_id=None) -> str:
	"""
	Krei okazaĵo de baterio kaj revenue la kazaĵo_id
	:param baterio_id:
	:param data:
	:param okazaĵo_id:
	:return:
	"""
	okazaĵo_id = str(uuid4()) if okazaĵo_id is None else okazaĵo_id
	db_kunsido = DBKunsido()
	db_kunsido.add(db.BaterioOkazaĵoV1(
		okazaĵo_id=okazaĵo_id,
		baterio_id=baterio_id,
		data=data
	))
	db_kunsido.commit()
	db_kunsido.close()
	return okazaĵo_id


def forigi_baterio_okazaĵo(okazaĵo_id: str):
	"""
	Forigi baterio okazaĵoj kun la kazaĵo id
	:param okazaĵo_id:
	:return:
	"""
	db_kunsido = DBKunsido()
	db_kunsido \
		.query(db.BaterioOkazaĵoV1) \
		.filter(db.BaterioOkazaĵoV1.okazaĵo_id == okazaĵo_id) \
		.delete()
	db_kunsido.commit()
	db_kunsido.close()


def forigi_baterio(baterio_id: str):
	db_kunsido = DBKunsido()
	db_kunsido \
		.query(db.BaterioV1) \
		.filter(db.BaterioV1.baterio_id == baterio_id) \
		.delete()
	db_kunsido.commit()
	db_kunsido.close()


def ĝisdatigo_baterio_nomo(baterio_id: str, baterio_nomo: str) -> types.Baterio:
	db_kunsido = DBKunsido()
	vico = db_kunsido \
		.query(db.BaterioV1) \
		.filter(db.BaterioV1.baterio_id == baterio_id) \
		.first()  # type: db.BaterioV1
	if vico is None:
		raise esceptoj.GeneraEraro('Nevalida Baterio ID')
	vico.baterio_nomo = baterio_nomo
	baterio = types.Baterio(
		baterio_id=vico.baterio_id,
		baterio_nomo=vico.baterio_nomo,
		modelo=vico.modelo
	)
	db_kunsido.commit()
	db_kunsido.close()
	return baterio


def ĝisdatigo_baterio_modelo(baterio_id: str, modelo: str) -> types.Baterio:
	db_kunsido = DBKunsido()
	vico = db_kunsido \
		.query(db.BaterioV1) \
		.filter(db.BaterioV1.baterio_id == baterio_id) \
		.first()  # type: db.BaterioV1
	if vico is None:
		raise esceptoj.GeneraEraro('Nevalida Baterio ID')
	vico.modelo = modelo
	baterio = types.Baterio(
		baterio_id=vico.baterio_id,
		baterio_nomo=vico.baterio_nomo,
		modelo=vico.modelo
	)
	db_kunsido.commit()
	db_kunsido.close()
	return baterio


def ĝisdatigo_baterio_okazaĵo_data(okazaĵo_id: str, data: dict):
	db_kunsido = DBKunsido()
	db_kunsido \
		.query(db.BaterioOkazaĵoV1) \
		.filter(db.BaterioOkazaĵoV1.okazaĵo_id == okazaĵo_id) \
		.update({
		db.BaterioOkazaĵoV1.data: data
	})
	db_kunsido.commit()
	db_kunsido.close()


def akiri_baterio_okazaĵoj(baterio_id: str) -> List[types.BaterioOkazajxo]:
	db_kunsido = DBKunsido()
	listo = []
	for okazaĵo in db_kunsido.query(db.BaterioOkazaĵoV1).filter(db.BaterioOkazaĵoV1.baterio_id == baterio_id).all():  # type: db.BaterioOkazaĵoV1
		listo.append(
			types.BaterioOkazajxo(
				okazajxo_id=okazaĵo.okazaĵo_id,
				baterio_id=okazaĵo.baterio_id,
				data=okazaĵo.data
			)
		)
	db_kunsido.close()
	return listo


def akiri_baterioj() -> List[types.Baterio]:
	db_kunsido = DBKunsido()
	listo = []
	for baterio in db_kunsido.query(db.BaterioV1).all():
		listo.append(
			types.Baterio(
				baterio_id=baterio.baterio_id,
				baterio_nomo=baterio.baterio_nomo,
				modelo=baterio.modelo
			)
		)
	db_kunsido.close()
	return listo


def estas_korekta_pasvorton(retpoŝto: str, pasvorto: str) -> bool:
	"""
	Kontrolu se la pasvorto estas la korekta pasvorto por la uzanto
	:param retpoŝto: La retpoŝto de uzanto
	:param pasvorto: La pasvorto por kontrolu
	:return: Se la pasvorto estas korekta por la uzanto
	"""
	db_kunsido = DBKunsido()
	row = db_kunsido.query(UzantoV2).filter(UzantoV2.retpoŝto == retpoŝto).first()  # type: UzantoV2
	if row is None:
		esceptoj.NevalidaUzantoId('Nevalida Uzanto ID')
	db_kunsido.close()
	return bcrypt.checkpw(pasvorto.encode('utf-8'), row.pasvorto.encode('utf-8'))


def havas_konton(google_id=None, retpoŝto=None, uzanto_id=None):
	if google_id is not None:
		return havas_konton_kun_google(google_id)
	if retpoŝto is not None:
		return havas_konto_kun_retpoŝto(retpoŝto)
	if uzanto_id is not None:
		return havas_konto_kun_uzanto_id(uzanto_id)


def havas_konto_kun_uzanto_id(uzanto_id: str) -> bool:
	db_kunsido = DBKunsido()
	row = db_kunsido.query(UzantoV2).filter(UzantoV2.uzanto_id == uzanto_id).first()
	db_kunsido.close()
	return row is not None


def havas_konto_kun_retpoŝto(retpoŝto: str) -> bool:
	db_kunsido = DBKunsido()
	row = db_kunsido.query(UzantoV2).filter(UzantoV2.retpoŝto == retpoŝto).first()
	db_kunsido.close()
	return row is not None


def havas_konton_kun_google(google_id: str) -> bool:
	db_kunsido = DBKunsido()
	row = db_kunsido.query(UzantoV2).filter(UzantoV2.google_id == google_id).first()
	db_kunsido.close()
	return row is not None


def akiri_uzanton_vico(google_id: str) -> UzantoV2:
	db_kunsido = DBKunsido()
	vico = db_kunsido.query(UzantoV2).filter(UzantoV2.google_id == google_id).first()
	db_kunsido.close()
	if vico is None:
		raise esceptoj.GoogleIdNeTrovita('Google ID Ne Trovita')
	return vico


def akiri_uzanton_id(google_id=None, retpoŝto=None) -> str:
	if google_id is not None:
		return akiri_uzanton_id_kun_google_id(google_id)
	if retpoŝto is not None:
		return akiri_uzanton_id_kun_retpoŝto(retpoŝto)


def akiri_uzanton_id_kun_retpoŝto(retpoŝto: str) -> str:
	db_kunsido = DBKunsido()
	vico = db_kunsido.query(UzantoV2).filter(UzantoV2.retpoŝto == retpoŝto).first()  # type: UzantoV2
	db_kunsido.close()
	if vico is None:
		raise esceptoj.NevalidaRetpoŝto('Nevalida Retpoŝto')
	return vico.uzanto_id


def akiri_uzanton_id_kun_google_id(google_id: str) -> str:
	db_kunsido = DBKunsido()
	vico = db_kunsido.query(UzantoV2).filter(UzantoV2.google_id == google_id).first()  # type: UzantoV2
	db_kunsido.close()
	if vico is None:
		raise esceptoj.GoogleIdNeTrovita('Google ID Ne Trovita')
	return vico.uzanto_id


def krei_konton_kun_google(retpoŝto: str,
						   google_id: str,
						   unua_nomo: str,
						   familia_nomo: str,
						   plena_nomo: str,
						   bildo: str,
						   hd: str,
						   estos_administra=False,
						   uzanto_id=None):
	if uzanto_id is None:
		uzanto_id = str(uuid4())

	db_kunsido = DBKunsido()
	db_kunsido.add(UzantoV2(
		uzanto_id=uzanto_id,
		estas_administranto=estos_administra,
		retpoŝto=retpoŝto,
		unua_nomo=unua_nomo,
		familia_nomo=familia_nomo,
		pasvorto='',
		google_id=google_id,
		google_ekstra={
			'plena_nomo': plena_nomo,
			'bildo': bildo,
			'hd': hd
		}
	))
	db_kunsido.commit()

	return uzanto_id


def krei_konto_kun_pasvorto(retpoŝto: str,
							unua_nomo: str,
							familia_nomo: str,
							pasvorto: str,
							estos_administra=False,
							uzanto_id=None):
	if uzanto_id is None:
		uzanto_id = str(uuid4())

	hashed_pasvorto = bcrypt.hashpw(pasvorto.encode('utf-8'), bcrypt.gensalt())

	db_kunsido = DBKunsido()
	db_kunsido.add(UzantoV2(
		uzanto_id=uzanto_id,
		estas_administranto=estos_administra,
		retpoŝto=retpoŝto,
		unua_nomo=unua_nomo,
		familia_nomo=familia_nomo,
		pasvorto=hashed_pasvorto,
		google_id='',
		google_ekstra={}
	))
	db_kunsido.commit()
	db_kunsido.close()

	return uzanto_id


def krei_kunsidon(uzanto_id: str) -> Tuple[datetime.datetime, str]:
	kunsidon_id = str(uuid4())
	valida_ĝis = datetime.datetime.utcnow() + datetime.timedelta(days=90)
	db_kunsido = DBKunsido()
	db_kunsido.add(KunsidoV1(
		kunsidon_id=kunsidon_id,
		uzanto_id=uzanto_id,
		valida_ĝis=valida_ĝis
	))
	db_kunsido.commit()
	db_kunsido.close()
	return valida_ĝis, kunsidon_id


def estas_valida_kunsido_id(kunsido_id: str) -> bool:
	db_kunsido = DBKunsido()
	vico = db_kunsido.query(db.KunsidoV1).filter(db.KunsidoV1.kunsidon_id == kunsido_id).first()  # type: db.KunsidoV1
	if vico is not None:
		return vico.valida_ĝis > datetime.datetime.utcnow()
	return False
