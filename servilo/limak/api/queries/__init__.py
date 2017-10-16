import graphene
from limak.api import esceptoj
from limak.api.queries import baterio
from limak.db import funkcioj


class Query(graphene.ObjectType):
	motd = graphene.NonNull(graphene.String)
	baterio = graphene.Field(baterio.QueryBaterio, kunsidon_id=graphene.NonNull(graphene.ID))

	def resolve_motd(self, args, context, info):
		return 'Saluton'

	def resolve_baterio(self, args, context, info):
		if funkcioj.estas_valida_kunsido_id(args.get('kunsidon_id')):
			return baterio.QueryBaterio()
		else:
			raise esceptoj.GeneraEraro('Nevalida Kunsidon ID')
