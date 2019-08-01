from flask import Flask, json, g, request
from flask_cors import CORS, cross_origin
import random
from Board import Board
from Algorithms import Algorithms

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/random-board", methods=["GET"])
@cross_origin(origin='http://localhost:3000')
def get_random_board():
    random_numbers = random.sample(range(0, 9), 9)

    return json_response({"board": random_numbers})


@app.route("/solve-board", methods=["POST"])
@cross_origin(origin='http://localhost:3000')
def solve_board():
    algorithms = Algorithms(request.get_json()['state'])
    done = False
    try:
        done = algorithms.a_star_search(request.get_json()['heuristic'])

    except Exception as e:
        print(e)
    if done:
        return json_response(algorithms.solution_json())
    else:
        return json_response("failed")


def json_response(payload, status=200):
    return json.dumps(payload), status, {'content-type': 'application/json'}


if __name__ == "__main__":
    app.run(debug=True)
    logging.getLogger('flask_cors').level = logging.DEBUG