import graphene
from limak.api.mutations import uzanto, baterio
from limak.db import funkcioj
from limak.api import esceptoj


class Mutation(graphene.ObjectType):
	motd = graphene.NonNull(graphene.String)
	krei_kunsidon_kun_google = uzanto.KreiKunsidonKunGoogle.Field()
	krei_kunsidon_kun_retposxto = uzanto.KreiKunsidonKunRetposxto.Field()
	krei_konto_kun_retposxto = uzanto.KreiKontoKunRetposxto.Field()
	baterio = graphene.Field(baterio.MutateBaterio, kunsidon_id=graphene.NonNull(graphene.ID))

	def resolve_motd(self, args, context, info):
		return 'Saluton'

	def resolve_baterio(self, args, context, info):
		if funkcioj.estas_valida_kunsido_id(args.get('kunsidon_id')):
			return baterio.MutateBaterio()
		else:
			raise esceptoj.GeneraEraro('Nevalida kunsido id')
