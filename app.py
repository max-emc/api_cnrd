from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-enigma/")
def get_enigma():
    enigma = Enigma()

    enigma_data = {
        "crypted_words": enigma.crypted_words,
        "crypted_text": enigma.crypted_text,
        "rotors": [list(r) for r in enigma.rotors],
        "true_position": enigma.true_position
    }

    return jsonify(enigma_data)

@app.route("/decode-enigma/", methods=["POST"])
def decode_enigma():
    data = request.json

    enigma = Enigma(
        data["true_position"],
        data["rotors"]
    )

    decoded_words, decoded_text = enigma.decode(data["position"])

    return jsonify({"decoded_words": decoded_words, "decoded_text": decoded_text})

@app.route("/forest-generator/", methods=["POST"])
def create_forest():
    data = request.json
    forest_generator = ForestGenerator(**data)
    return forest_generator.create_forest()

@app.route("/board-game/", methods=["POST"])
def board_game():
    data = request.json
    player = data["player"]

    position_1 = orthogonal_move(data["agent_1"], player)
    position_2 = octogonal_move(data["agent_2"], player)

    return jsonify({
        "agent_1": position_1,
        "agent_2": position_2,
        "player_win":  player[0] == board_size - 1,
        "player_lose": position_1 == player or position_2 == player
    })


if __name__ == "__main__":
    app.run(debug=True)
