from flask import Flask, render_template, request, jsonify
import json, random

app = Flask(__name__)

with open("anime_data.json") as f:
    anime_data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    name = request.form.get("name", "").lower()
    results = [a for a in anime_data if name in a["name"].lower()]
    return jsonify(results)

@app.route("/random")
def random_anime():
    return jsonify([random.choice(anime_data)])

@app.route("/filter_genre", methods=["POST"])
def filter_genre():
    genre = request.form.get("genre", "")
    results = [a for a in anime_data if genre in a["genres"]]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
