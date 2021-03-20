from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import time
import json
from bs4 import BeautifulSoup

with open('data.json', 'r') as outfile:
    data = json.load(outfile)

# Make a request
page = requests.get(
    "https://www.binance.com/en/support/announcement/c-48?navId=48")
soup = BeautifulSoup(page.content, 'html.parser')
title = ""
webhook = DiscordWebhook(url=data["webhook"])


while True:
    first_a = soup.find("a", {"class": "css-1ej4hfo"})
    first_headline = first_a.text
    link = "https://binance.com" + str(first_a.get("href"))

    if title == first_headline:
        print("Title is the same")

    else:
        embed = DiscordEmbed(
            description=first_headline,
            color='ffff00',
        )
        embed.set_author(
            name="Binance New Update",
            url=str(link),
            icon_url="https://i.imgur.com/cjH2U9J.png"
        )
        webhook.add_embed(embed)
        webhook.execute()
        webhook.embeds.pop()
        title = first_headline

    time.sleep(300)