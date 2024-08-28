from flask import Flask
import os


app = Flask(__name__)
app.config["CACHE_TYPE"] = os.environ.get("CACHE_TYPE", "SimpleCache")



async def channel_to_rss(channel):
    pass