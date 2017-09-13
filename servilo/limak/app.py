from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
from flask_cors import CORS
import logging
from limak.api import schema

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
logging.getLogger('flask_cors').level = logging.DEBUG

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


@app.after_request
def foo(response):
	response.headers['Access-Control-Allow-Credentials'] = 'true'
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Headers'] = 'origin, content-type, accept'
	return response


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8000)
