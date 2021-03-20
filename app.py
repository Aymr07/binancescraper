from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import time
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "https://www.binance.com/en/support/announcement/c-48?navId=48")
soup = BeautifulSoup(page.content, 'html.parser')
title = ""
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/822918524619718726/iofuXEasO545MjY8PoSvQbf_TF0C_dqbOy-jl8av7mLDP06TNsgTkkoqNR-LlvQkks9a')



while True:
    first_headline = soup.find("a", {"class": "css-1ej4hfo"}).text
    time.sleep(3)
    if title == first_headline:
        print("Title is the same")
        embed = DiscordEmbed(
            title="New Binance Update!",
            description=first_headline,
            color='ffff00',
        )
        webhook.add_embed(embed)
        webhook.execute()
        webhook.embeds.pop()
        title = first_headline

    else:
        embed = DiscordEmbed(
            title="New Binance Update!",
            description=first_headline,
            color='ffff00',
        )
        webhook.add_embed(embed)
        webhook.execute()
        webhook.embeds.pop()
        title = first_headline







