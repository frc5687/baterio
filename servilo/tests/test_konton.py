from limak.api import schema
import requests
import json
from uuid import uuid4
import names


def test_konton(verbose=False):
	query = '''
		mutation TestKonton ($retposxto: String!, $unuaNomo: String!, $familiaNomo: String!, $pasvorto: String!) {
			kreiKontoKunRetposxto (retposxto: $retposxto, unuaNomo: $unuaNomo, familiaNomo: $familiaNomo, pasvorto: $pasvorto) { 
				kunsidon {
					kunsidonId
					validaGxis
				}
			} 
		}
		'''
	variables = {
		'retposxto': str(uuid4()) + '@theoutliers.org',
		'unuaNomo': names.get_first_name(),
		'familiaNomo': names.get_last_name(),
		'pasvorto': str(uuid4())
	}

	r = schema.execute(query, variable_values=variables)

	def test_passed():
		try:
			return len(r.data['kreiKontoKunRetposxto']['kunsidon']['kunsidonId']) == 36
		except Exception as e:
			repr(e)
			return False

	if verbose and test_passed() is False:
		print(json.dumps(r.data, indent=4))

	assert test_passed()


if __name__ == '__main__':
	print(test_konton(verbose=True))
