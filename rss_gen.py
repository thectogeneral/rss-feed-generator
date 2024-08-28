from flask import Flask
import os
import httpx
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config["CACHE_TYPE"] = os.environ.get("CACHE_TYPE", "SimpleCache")

class ChannelNotFound(Exception):
    pass

async def get_doc_from_url(url):
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url)
            res.raise_for_status()
        return BeautifulSoup(res.content, "lxml")
    except httpx.HTTPStatusError as e:
        if "Redirect response" in str(e):
            raise ChannelNotFound()


async def channel_to_rss(channel):
    url = f"https://t.me/s/{channel}"
    doc = await get_doc_from_url(url)