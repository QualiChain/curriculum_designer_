import logging

from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
# sys.path.append('../..')
from services import curriculum_recommendation


logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

'''Run flask by executing the command python -m flask run'''

app = Flask(__name__)
CORS(app)


@app.route('/curriculum_recommendation', methods=['POST'])
def recommend():
    try:
        response = curriculum_recommendation.recommend()
        return jsonify(response)
    except Exception as ex:
        log.error(ex)
        return ex, 400


@app.route('/curriculum_skill_coverage', methods=['POST'])
def get_coverage():
    try:
        response = {'curriculum_skill_coverage' : curriculum_recommendation.get_curriculum_coverage()}
        return jsonify(response)
    except Exception as ex:
        log.error(ex)
        return ex, 400
