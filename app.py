from flask import Flask, request, render_template, jsonify, request, abort
from travel_recommender_api import suggest

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def make_prediction():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        data = request.json
        response = suggest(data)

        return jsonify(response)
    else:
        return render_template("layout.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
