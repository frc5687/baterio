import graphene
import google.oauth2.credentials
from google.auth.transport.requests import AuthorizedSession
from limak.api.types import Kunsidon
from limak.db import funkcioj as db_funkcioj
from limak.api import esceptoj


class KreiKunsidon(graphene.Mutation):
	class Input:
		aliro_token = graphene.NonNull(graphene.ID)

	kunsidon = graphene.Field(Kunsidon)

	@staticmethod
	def mutate(root, args, context, info):
		kreditoj = google.oauth2.credentials.Credentials(args.get('aliro_token'))
		rajtigita_kunsido = AuthorizedSession(kreditoj)
		respondo = rajtigita_kunsido.get('https://www.googleapis.com/userinfo/v2/me')
		respondo = respondo.json()

		google_id = respondo.get('id')
		try:
			uzanto_id = db_funkcioj.akiri_uzanton_id(google_id)
		except esceptoj.GoogleIdNeTrovita:
			uzanto_id = db_funkcioj.krei_konton(respondo.get('email'),
												google_id,
												respondo.get('given_name'),
												respondo.get('family_name'),
												respondo.get('name'),
												respondo.get('picture'),
												respondo.get('hd', 'gmail.com')
												)

		valida_gxis, kunsidon_id = db_funkcioj.krei_kunsidon(uzanto_id)

		kunsidon = Kunsidon(kunsidon_id=kunsidon_id, valida_gxis=valida_gxis)

		return KreiKunsidon(kunsidon=kunsidon)
