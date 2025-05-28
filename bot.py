
import discord
import random
import string
import os

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

TOKEN = os.getenv("MTM3NzAwMTcyMDQ2NjY0MTAzNw.GCK91a.f4hTmqqed0XwWlWTeBX6A96P5zlskrTvC9U7CQ")

bot = discord.Client(intents=intents)

def generate_key():
    return "-".join("".join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(3))

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!gethwid"):
        key = generate_key()
        with open("used_keys.txt", "a") as f:
            f.write(key + "\n")

        try:
            await message.author.send(f"🔐 Your one-time HWID key: **{key}**\nUse it in the loader.")
            await message.channel.send("📬 HWID sent in DMs.")
        except:
            await message.channel.send("❌ Can't send DM. Enable messages from server members.")

bot.run(TOKEN)
