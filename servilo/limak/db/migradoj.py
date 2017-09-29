from limak.db import DBKunsido, UzantoV1, UzantoV2


def migri_uzantov1_al_uzantov2():
	db_kunsido = DBKunsido()
	for uzanto in db_kunsido.query(UzantoV1).filter(~UzantoV1.uzanto_id.in_(db_kunsido.query(UzantoV2.uzanto_id))).all():  # type: UzantoV1
		db_kunsido.add(UzantoV2(
			uzanto_id=uzanto.uzanto_id,
			estas_administranto=uzanto.estas_administranto,
			retpoŝto=uzanto.retpoŝto,
			unua_nomo=uzanto.unua_nomo,
			familia_nomo=uzanto.familia_nomo,
			pasvorto='',
			google_id=uzanto.google_id,
			google_ekstra={
				'plena_nomo': uzanto.plena_nomo,
				'bildo': uzanto.bildo,
				'hd': uzanto.hd
			}
		))
		db_kunsido.commit()
	db_kunsido.close()


if __name__ == '__main__':
	migri_uzantov1_al_uzantov2()