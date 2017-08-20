from flask import render_template
import feedparser
from flask import Flask


app = Flask(__name__)

RSS_FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'msnbc' : 'http://www.msnbc.com/feeds/latest',
    'nytimes_tech' : "http://feeds.nytimes.com/nyt/rss/Technology"}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="nytimes_tech"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
