"""
MinerGuard starter bot (ACM AI @ S&T)

Comes online in Discord and answers when someone @mentions it,
using the same LangChain agent + tools we built in weeks 1 and 2.

Setup:
    pip install discord.py python-dotenv langchain langchain-ollama
    Make a file called .env in this folder with one line:
        DISCORD_TOKEN=paste-your-bot-token-here
    (NEVER push .env to GitHub. It's in .gitignore.)

Run:
    python bot.py
"""

import asyncio
import json
import os
import urllib.parse
import urllib.request
from datetime import date

import discord                              # the Discord library
from dotenv import load_dotenv              # reads secrets from the .env file
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()                               # load DISCORD_TOKEN from .env
TOKEN = os.getenv("DISCORD_TOKEN")
MODEL = "gpt-oss:20b-cloud"


# ---------- Tools: plain Python functions the agent can call ----------

def get_json(url):
    """Helper: download a URL and turn the JSON into a Python dict."""
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read())


@tool
def get_weather(city: str) -> dict:
    """Get the current weather for a city, like 'Rolla'.
    Use this for any question about weather or what to wear outside."""
    geo = get_json("https://geocoding-api.open-meteo.com/v1/search?count=1&name="
                   + urllib.parse.quote(city))
    if not geo.get("results"):
        return {"error": f"Couldn't find {city}"}
    place = geo["results"][0]
    now = get_json(
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={place['latitude']}&longitude={place['longitude']}"
        "&current=temperature_2m,apparent_temperature,precipitation,wind_speed_10m"
        "&temperature_unit=fahrenheit&wind_speed_unit=mph"
    )["current"]
    return {"city": place["name"], "temp_f": now["temperature_2m"],
            "feels_like_f": now["apparent_temperature"],
            "precip_in": now["precipitation"], "wind_mph": now["wind_speed_10m"]}


TOOLS = [get_weather]   # members add their tools to this list


# ---------- The agent ----------

agent = create_agent(
    model=ChatOllama(model=MODEL, temperature=0),
    tools=TOOLS,
    system_prompt=(
        "You are MinerGuard, the ACM Discord bot at Missouri S&T in Rolla, MO. "
        f"Today is {date.today().isoformat()}. "
        "Use your tools when they help. Keep answers short, this is Discord."
    ),
    checkpointer=InMemorySaver(),   # remembers each person's conversation while running
)


def ask_agent(question, user_id):
    """Run the agent. Each Discord user gets their own conversation (thread_id)."""
    config = {"configurable": {"thread_id": str(user_id)}}
    result = agent.invoke({"messages": [{"role": "user", "content": question}]}, config)
    return result["messages"][-1].content


# ---------- Discord ----------

intents = discord.Intents.default()
intents.message_content = True     # needed to read message text
intents.members = True             # needed later for the server guard (join events)
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"MinerGuard is online as {client.user}")


@client.event
async def on_message(message):
    if message.author.bot:                       # ignore other bots (and itself)
        return
    if client.user not in message.mentions:      # only answer when @mentioned
        return

    # Remove the @MinerGuard part so the agent just sees the question
    question = message.content.replace(f"<@{client.user.id}>", "").strip()
    if not question:
        await message.reply("Hey! Ask me something.")
        return

    async with message.channel.typing():         # shows "MinerGuard is typing..."
        # The agent is slow and not async, so run it in a background thread
        answer = await asyncio.to_thread(ask_agent, question, message.author.id)

    await message.reply(answer[:2000])           # Discord max message length is 2000


client.run(TOKEN)
