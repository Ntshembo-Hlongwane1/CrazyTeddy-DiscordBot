import discord
import os
from dotenv import load_dotenv
from mongoengine import *
load_dotenv(verbose=True)

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

mongo = connect(db='Users', host=os.getenv('mongoURI'))

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_member_join(member):
    print(member)

@client.event
async def on_member_remove(member):
    print()
    


client.run(os.getenv('TOKEN'))
