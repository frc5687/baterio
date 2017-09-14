from uuid import uuid4
import datetime
from typing import Tuple
from limak.db import DBKunsido, KunsidoV1, UzantoV1
from limak.api import esceptoj


def havas_konton(google_id: str) -> bool:
	db_kunsido = DBKunsido()
	row = db_kunsido.query(UzantoV1).filter(UzantoV1.google_id == google_id).first()
	db_kunsido.close()
	return row is not None


def akiri_uzanton_vico(google_id: str) -> UzantoV1:
	db_kunsido = DBKunsido()
	vico = db_kunsido.query(UzantoV1).filter(UzantoV1.google_id == google_id).first()
	db_kunsido.close()
	if vico is None:
		raise esceptoj.GoogleIdNeTrovita('Google ID Ne Trovita')
	return vico


def akiri_uzanton_id(google_id: str) -> str:
	db_kunsido = DBKunsido()
	vico = db_kunsido.query(UzantoV1).filter(UzantoV1.google_id == google_id).first()  # type: UzantoV1
	db_kunsido.close()
	if vico is None:
		raise esceptoj.GoogleIdNeTrovita('Google ID Ne Trovita')
	return vico.uzanto_id


def krei_konton(retpoŝto: str,
				google_id: str,
				unua_nomo: str,
				familiar_nomo: str,
				plena_nomo: str,
				bildo: str,
				hd: str,
				estos_administra=False,
				uzanto_id=None) -> str:
	if uzanto_id is None:
		uzanto_id = str(uuid4())

	db_kunsido = DBKunsido()
	db_kunsido.add(UzantoV1(
		uzanto_id=uzanto_id,
		estos_administra=estos_administra,
		retpoŝto=retpoŝto,
		google_id=google_id,
		unua_nomo=unua_nomo,
		familiar_nomo=familiar_nomo,
		plena_nomo=plena_nomo,
		bildo=bildo,
		hd=hd
	))
	db_kunsido.commit()

	return uzanto_id


def krei_kunsidon(uzanton_id: str) -> Tuple[datetime.datetime, str]:
	kunsidon_id = str(uuid4())
	valida_ĝis = datetime.datetime.utcnow() + datetime.timedelta(days=90)
	db_kunsido = DBKunsido()
	db_kunsido.add(KunsidoV1(
		uzanton_id=uzanton_id,
		kunsidon_id=kunsidon_id,
		valida_ĝis=valida_ĝis
	))
	db_kunsido.commit()
	db_kunsido.close()
	return valida_ĝis, kunsidon_id
