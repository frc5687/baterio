import graphene
from limak.api.queries import Query
from limak.api.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
