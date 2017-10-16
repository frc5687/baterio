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


class ForigiBaterio(graphene.Mutation):
	class Input:
		baterio_id = graphene.NonNull(graphene.String)

	estis_sukcesa = graphene.NonNull(graphene.Boolean)

	@staticmethod
	def mutate(root, args, context, info):
		db_funkcioj.forigi_baterio(args.get('baterio_id'))
		return ForigiBaterio(estis_sukcesa=True)


class GxisdatigoBaterioNomo(graphene.Mutation):
	class Input:
		baterio_id = graphene.NonNull(graphene.ID)
		nova_baterio_nomo = graphene.NonNull(graphene.String)

	baterio = graphene.Field(types.Baterio)

	@staticmethod
	def mutate(root, args, context, info):
		baterio = db_funkcioj.ĝisdatigo_baterio_nomo(
			args.get('baterio_id'),
			args.get('nova_baterio_nomo')
		)
		return GxisdatigoBaterioNomo(baterio=baterio)


class GxisdatigoBaterioModelo(graphene.Mutation):
	class Input:
		baterio_id = graphene.NonNull(graphene.ID)
		nova_baterio_modelo = graphene.NonNull(graphene.String)

	baterio = graphene.Field(types.Baterio)

	@staticmethod
	def mutate(root, args, context, info):
		baterio = db_funkcioj.ĝisdatigo_baterio_modelo(
			args.get('baterio_id'),
			args.get('nova_baterio_modelo')
		)
		return GxisdatigoBaterioModelo(baterio=baterio)


class MutateBaterio(graphene.ObjectType):
	registri_baterio = RegistriBaterio.Field()
	forigi_baterio = ForigiBaterio.Field()
	gxisdatigo_baterio_nomo = GxisdatigoBaterioNomo.Field()
	gxisdatigo_baterio_modelo = GxisdatigoBaterioModelo.Field()
