from flask import Flask, jsonify, request
import csv

all_movies = []

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles  = []
unliked_articles  = []
did_not_articles  = []

app = Flask(__name__)

@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

@app.route("/liked-articles", methods=["POST"])
def liked_articles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-articles", methods=["POST"])
def unliked_articles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    unliked_articles.append(articles)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-articles", methods=["POST"])
def did_not_articles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    did_not_articles.append(articles)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()