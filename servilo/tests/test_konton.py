import requests
import json
import uuid
import names


def test_konton(api_endpoint=None, verbose=False):
	api_endpoint = 'http://localhost:8000/graphql' if api_endpoint is None else api_endpoint

	payload = {
		'query': '''
		mutation TestKonton ($retposxto: String!, $unuaNomo: String!, $familiaNomo: String!, $pasvorto: String!) {
			kreiKontoKunRetposxto (retposxto: $retposxto, unuaNomo: $unuaNomo, familiaNomo: $familiaNomo, pasvorto: $pasvorto) { 
				kunsidon {
					kunsidonId
					validaGxis
				}
			} 
		}
		''',
		'variables': json.dumps({
			'retposxto': str(uuid.uuid4()) + '@theoutliers.org',
			'unuaNomo': names.get_first_name(),
			'familiaNomo': names.get_last_name(),
			'pasvorto': str(uuid.uuid4())
		})
	}

	r = requests.post(api_endpoint, data=payload)

	def test_passed():
		try:
			return len(r.json()['data']['kreiKontoKunRetposxto']['kunsidon']['kunsidonId']) == 36
		except:
			return False

	if verbose and test_passed() is False:
		print(json.dumps(r.json(), indent=4))

	assert test_passed()


if __name__ == '__main__':
	print(test_konton('http://localhost:8000/graphql', verbose=True))
