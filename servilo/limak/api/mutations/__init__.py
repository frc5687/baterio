import graphene
from limak.api.mutations.uzanto import KreiKunsidonKunGoogle, KreiKontoKunRetposxto, KreiKunsidonKunRetposxto


class Mutation(graphene.ObjectType):
	motd = graphene.NonNull(graphene.String)
	krei_kunsidon_kun_google = KreiKunsidonKunGoogle.Field()
	krei_kunsidon_kun_retposxto = KreiKunsidonKunRetposxto.Field()
	krei_konto_kun_retposxto = KreiKontoKunRetposxto.Field()

	def resolve_motd(self, args, context, info):
		return 'Saluton'
