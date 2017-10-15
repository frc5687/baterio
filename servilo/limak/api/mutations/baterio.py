import graphene
from limak.api.types import Kunsidon
from limak.db import funkcioj as db_funkcioj
from limak.api import esceptoj


class RegistriBaterio(graphene.Mutation):
	class Input:
		pass