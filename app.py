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


@app.route("/api/data", methods=["GET"])
def get_data():
    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submittodoitem", methods=["POST"])
def submittodoitem():
    item_name = request.form["item_name"]
    item_description = request.form["item_description"]

    todo_item = {
        "ItemName": item_name,
        "ItemDescription": item_description
    }

    collection.insert_one(todo_item)

    return jsonify({
        "message": "To-Do item submitted successfully",
        "ItemName": item_name,
        "ItemDescription": item_description
    })


if __name__ == "__main__":
    app.run(debug=True)