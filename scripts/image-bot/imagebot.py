import discord
import requests
import random
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

client = discord.Client()

# Replace this with your API key and search engine ID
API_KEY = "YOUR_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"

@client.event
async def on_message(message):
    if message.content == "!capybara":
        service = build("customsearch", "v1", credentials=Credentials.from_authorized_user_info(info=None, scopes=["https://www.googleapis.com/auth/cse"]))
        result = service.cse().list(q="capybara", cx=SEARCH_ENGINE_ID, searchType="image", imgSize="large", num=10, key=API_KEY).execute()
        images = [item["link"] for item in result["items"]]
        image_url = random.choice(images)
        response = requests.get(image_url, stream=True)
        await message.channel.send(file=discord.File(response.raw, "capybara.jpg"))

client.run("YOUR_BOT_TOKEN_HERE")
