from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["flashdb"]
collection = db["submissions"]


# JSON API
@app.route("/api/data", methods=["GET"])
def get_data():
    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    data = {
        "name": name,
        "email": email,
        "message": message
    }

    collection.insert_one(data)

    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)