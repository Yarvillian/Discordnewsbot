# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
# Import the os module.
import os
#NEWSAPI needs requests
import requests
#Used for NewsAPI
from newsapi.newsapi_client import NewsApiClient
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
# Loads the .env file that resides on the same level as the script.
load_dotenv()
# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
NEWSAPI_TOKEN = os.getenv("NEWSAPI_TOKEN")
# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
#Initialize newsapi
newsapi = NewsApiClient(api_key=NEWSAPI_TOKEN)
# /v2/top-headlines
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("Message Recieved.")
	if message.content == "help":
		await message.channel.send("This bot currently can return breaking news headlines for a country and category with the '!headlines'.")
	if message.content == "!headlines": # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "!headlines".
		top_headlines = newsapi.get_top_headlines(q='Apple',
                                          sources='CNN',
                                          language='en',
                                          )
		print(f'headlines:{top_headlines}')
		await message.channel.send("Hey we got here.")
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)