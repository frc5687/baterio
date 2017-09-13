import graphene


class Mutation(graphene.ObjectType):
	motd = graphene.NonNull(graphene.String)

	def resolve_motd(self, args, context, info):
		return 'Saluton'
