import graphene
from limak.api import types, esceptoj
from limak.db import funkcioj as db_funkcioj


class QueryBaterio(graphene.ObjectType):
	baterioj = graphene.List(types.Baterio)

	def resolve_baterioj(self, args, context, info):
		baterioj = db_funkcioj.akiri_baterioj()
		return baterioj
