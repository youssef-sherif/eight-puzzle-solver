from flask import Flask, json, g, request
import random
from Board import Board


app = Flask(__name__)


@app.route("/board", methods=["GET"])
def get_random_board():
    random_numbers = random.sample(range(0, 9), 9)
    i = 0
    dictionary = {}
    for number in random_numbers:
        dictionary[i] = number
        i += 1

    board = Board.from_dictionary(dictionary)

    return json_response(board.to_json())


@app.route("/board", methods=["POST"])
def solve_board(board: Board):
    return json_response("solved")


def json_response(payload, status=200):
    return json.dumps(payload), status, {'content-type': 'application/json'}

if __name__ == "__main__":
    app.run(debug=True)