import graphene
from limak.api.mutations.uzanto import KreiKunsidon


class Mutation(graphene.ObjectType):
	motd = graphene.NonNull(graphene.String)
	krei_kunsidon = KreiKunsidon.Field()

	def resolve_motd(self, args, context, info):
		return 'Saluton'
