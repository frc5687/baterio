from graphene.types.datetime import DateTime
from graphene.types.json import JSONString
import graphene


class Kunsidon(graphene.ObjectType):
	valida_gxis = graphene.NonNull(graphene.types.datetime.DateTime)
	kunsidon_id = graphene.NonNull(graphene.ID)


class Baterio(graphene.ObjectType):
	baterio_id = graphene.NonNull(graphene.ID)
	baterio_nomo = graphene.NonNull(graphene.String)
	modelo = graphene.NonNull(graphene.String)


class BaterioOkazajxo(graphene.ObjectType):
	okazajxo_id = graphene.NonNull(graphene.ID)
	baterio_id = graphene.NonNull(graphene.ID)
	data = graphene.NonNull(graphene.types.json.JSONString)
