from pathlib import Path
from nltk.stem.wordnet import WordNetLemmatizer
import discord
import json
import nltk

import random

API_KEYS = Path(__file__).parent / "keys.json"
SUSSY = Path(__file__).parent / "sussy.gif"

with open(API_KEYS, "r") as f:
  keys = json.load(f)

bot = discord.Client()

@bot.event
async def on_message(message):
  temp = nltk.word_tokenize(message.content)
  tokens = nltk.pos_tag(temp)
  for index in range(len(tokens)-1,-1,-1):
    if "VB" in tokens[index][1]:
      if random.randint(0,99) == 0:
        with open(SUSSY, "rb") as f:
          base_word = WordNetLemmatizer().lemmatize(tokens[index][0],'v')
          await message.channel.send(base_word.upper() + " THIS", file=discord.File(f))
      return

bot.run(keys["BOT"])