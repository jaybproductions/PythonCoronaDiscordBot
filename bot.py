import requests
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ.get("token")

# bot command prefix
bot = commands.Bot(command_prefix='!')

# headers for Covid-19 API calls
headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "69e32e90cemshf5f029273e5dabcp147c44jsn65211f976d36"
}


headersinspire = {
    'x-rapidapi-host': "quotes15.p.rapidapi.com",
    'x-rapidapi-key': "69e32e90cemshf5f029273e5dabcp147c44jsn65211f976d36"
}


headersflip = {
    'x-rapidapi-host': "coin-flip1.p.rapidapi.com",
    'x-rapidapi-key': "69e32e90cemshf5f029273e5dabcp147c44jsn65211f976d36"
}

# When turning bot online / running python script
@bot.event
async def on_ready():
    print('We have logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')


#!totals command
@bot.command()
async def totals(ctx, a: str):

    # API call for specific country
    querystringcountry = {"format": "json", "name": a}
    urlcountry = "https://covid-19-data.p.rapidapi.com/country"
    responsecountry = requests.request(
        "GET", urlcountry, headers=headers, params=querystringcountry)
    x = responsecountry.json()

   # grabbing each key from JSON data and removing brackets
    confirmedcases = str([db_item["confirmed"] for db_item in x])[1:-1]
    recoveredcases = str([db_item["recovered"] for db_item in x])[1:-1]
    criticalcases = str([db_item["critical"] for db_item in x])[1:-1]
    deaths = str([db_item["deaths"] for db_item in x])[1:-1]

    # embedding information into discord channel
    embed = discord.Embed(
        title="CoronaBOT", description="CoronaVirus Case Numbers in: " + a.upper(), color=0xeee657)
    embed.add_field(name="Confirmed", value=confirmedcases, inline=False)
    embed.add_field(name="Recovered", value=recoveredcases, inline=False)
    embed.add_field(name="Critical", value=criticalcases, inline=False)
    embed.add_field(name="Deaths", value=deaths, inline=False)
    # sending embedded data
    await ctx.send(embed=embed)

# total worldwide command
@bot.command()
async def total(ctx):

    # API call for worldwide
    querystringtotals = {"format": "json"}
    urltotals = "https://covid-19-data.p.rapidapi.com/totals"
    responsetotals = requests.request(
        "GET", urltotals, headers=headers, params=querystringtotals)
    x = responsetotals.json()

   # grabbing each key from JSON data and removing brackets
    confirmedcases = str([db_item["confirmed"] for db_item in x])[1:-1]
    recoveredcases = str([db_item["recovered"] for db_item in x])[1:-1]
    criticalcases = str([db_item["critical"] for db_item in x])[1:-1]
    deaths = str([db_item["deaths"] for db_item in x])[1:-1]

    # embedding information into discord channel
    embed = discord.Embed(
        title="CoronaBOT", description="CoronaVirus Case Numbers in: World ", color=0xeee657)
    embed.add_field(name="Confirmed", value=confirmedcases, inline=False)
    embed.add_field(name="Recovered", value=recoveredcases, inline=False)
    embed.add_field(name="Critical", value=criticalcases, inline=False)
    embed.add_field(name="Deaths", value=deaths, inline=False)
    # sending embedded data
    await ctx.send(embed=embed)

'''
@bot.command()
async def meme(ctx):

    #API call for inspirationalquotes
    urlmeme = "https://meme-api.herokuapp.com/gimme/dankmemes/1"
    responsememe = requests.request("GET", urlmeme)
    x = responsememe.json()
    print(x['memes'][0]['url'])
    await ctx.send(x)
'''

# Flipping a Coin Command
@bot.command()
async def flip(ctx):

    # API call for coinflip
    urlflip = "https://coin-flip1.p.rapidapi.com/headstails"
    responseflip = requests.request("GET", urlflip, headers=headersflip)
    x = responseflip.json()
    #outcome = str( [db_item["outcome"] for db_item in x] )[1:-1]
    print(x['outcome'])
    await ctx.send(x['outcome'])

# removing default help command
bot.remove_command('help')

# help Command
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="CoronaBOT", description="Get Updated CoronaVirus Case Numbers", color=0xeee657)

    embed.add_field(
        name="!total", value="Gets the Total Number of cases Worldwide", inline=False)
    embed.add_field(name="!totals 'countryname'",
                    value="Gets the total number of cases per country entered", inline=False)
    embed.add_field(
        name="!inspire", value="Gives a random inspirational quote....coming soon. ", inline=False)
    embed.add_field(name="!flip", value="Flips a Coin", inline=False)
    embed.add_field(name="!help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)


# Bot TOKEN
bot.run(token)
