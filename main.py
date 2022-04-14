from pathlib import Path
import discord
import json
import nltk
import random

API_KEYS = Path(__file__).parent / "keys.json"
SUS = discord.File("sussy.gif")

with open(API_KEYS, "r") as f:
  keys = json.load(f)


bot = discord.Client()

@bot.event
async def on_message(message):
  tokens = nltk.word_tokenize(message.content)
  for index in range(len(tokens)-1,-1,-1):
    if "VB" in tokens[index][1]:
      if random.randint(0,4) == 0:
        await message.channel.send(tokens[index][0].upper() + " THIS", file=SUS)
      return

bot.run(keys["BOT"])