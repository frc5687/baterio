import graphene
from limak.api import types, esceptoj
from limak.db import funkcioj as db_funkcioj


class RegistriBaterio(graphene.Mutation):
	"""
	Registri nova baterio. Neniu volos registri nova baterio ĉe konkurenco, do
	ĉi tio ne subteno senkonekta baterio id generacio.
	"""
	class Input:
		baterio_nomo = graphene.NonNull(graphene.String)
		modelo = graphene.NonNull(graphene.String)

	baterio = graphene.Field(types.Baterio)

	@staticmethod
	def mutate(root, args, context, info):
		baterio_id = db_funkcioj.krei_baterio(
			baterio_nomo=args.get('baterio_nomo'),
			modelo=args.get('modelo')
		)
		return RegistriBaterio(
			baterio=types.Baterio(
				baterio_id=baterio_id,
				baterio_nomo=args.get('baterio_nomo'),
				modelo=args.get('modelo')
			)
		)


class MutateBaterio(graphene.ObjectType):
	registri_baterio = RegistriBaterio.Field()
