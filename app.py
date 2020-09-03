from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    scrape = mongo.db.scrape.find_one()
    return render_template("index.html", scrape=scrape)

@app.route("/scrape")
def scraper():
    scrape = mongo.db.scrape
    scrape_data = scrape_mars.scrape()
    scrape.update({}, scrape_data, upsert=True)
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)
