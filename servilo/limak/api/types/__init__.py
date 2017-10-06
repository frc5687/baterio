from graphene.types.datetime import DateTime
import graphene


class Kunsidon(graphene.ObjectType):
	valida_gxis = graphene.NonNull(graphene.types.datetime.DateTime)
	kunsidon_id = graphene.NonNull(graphene.ID)