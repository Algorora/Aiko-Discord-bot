import discord
from discord.ext import commands as command
import urllib.request as u
import xml.etree.ElementTree as et
import rule34
import random
import time
import asyncio
import functools
import itertools
import math
from async_timeout import timeout
import random
import datetime
import requests
from urllib import parse, request
import re
import discord
import youtube_dl
import asyncio
import os
import praw
import random
import requests
import aiohttp
from discord.ext.commands import has_permissions, MissingPermissions
ltime = time.asctime(time.localtime())
client = command.Bot(command_prefix='&')
Client = discord.Client()
client.remove_command('help')
r = rule34.Rule34


def xmlparse(str):
	root = et.parse(u.urlopen(str))
	for i in root.iter('post'):
		fileurl = i.attrib['file_url']
		return fileurl
def xmlcount(str):
	root = et.parse(u.urlopen(str))
	for i in root.iter('posts'):
		count = i.attrib['count']
		return count
def pidfix(str):
	ye = int(xmlcount(r.urlGen(tags=str,limit=1)))
	ye = ye - 1
	return ye
def rdl(str,int):
	print(f'[INFO {ltime}]: integer provided: {int}')

	if int > 2000:
		int = 2000
	if int == 0:
		int == 0
		print(f'[INFO {ltime}]: Integer is 0, accommodating for offset overflow bug. ')
	elif int != 0:
		int = random.randint(1,int)
	print(f'[INFO {ltime}]: integer after randomizing: {int}')
	xurl = r.urlGen(tags=str,limit=1,PID=int)
	print(xurl)
	wr = xmlparse(xurl)

	if 'webm' in wr:
		if 'sound' not in str:
			if 'webm' not in str:
				print(f'[INFO {ltime}]: We got a .webm, user didnt specify sound. Recursing. user tags: {str}')
				wr = rdl(str,pidfix(str))
		else:
			pass
	elif 'webm' not in wr:
		print(f'[INFO {ltime}]: Not a webm, dont recurse.')
	return wr
async def statuschange():
	while True:
		await client.change_presence(activity=discord.Game(name='with my pussy'))
		await asyncio.sleep(10)
		await client.change_presence(activity=discord.Game(name='&help'))
		await asyncio.sleep(10)
# Definitions of bot events starts here
# ================================================================================================================
@client.event
async def on_ready():
	print(f'[INFO {ltime}]: Logged in as {client.user.name}!')
	await statuschange()
# Definitions of bot commands starts here
# ================================================================================================================
@client.command()
async def yeet(ctx, user : discord.Member):
        embed=discord.Embed(title="", description=f"**{ctx.message.author.mention}yeeted{user.mention}**", color=0xff80ff)
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/803152602673184768/803158079847006218/YEET.gif')
        await ctx.send(embed = embed)

# ================================================================================================================
@client.command()
async def shutup(ctx, user : discord.Member):
        embed=discord.Embed(title="", description=f"**Shut up!!!{user.mention}**", color=0xff80ff)
        embed.set_image(url=f'https://cdn.kapwing.com/final_6011b5876dfaad00787b2687_253255.mp4')
        await ctx.send(embed = embed)

# ================================================================================================================
@client.command()
async def heal(ctx, user : discord.Member):
        embed=discord.Embed(title="", description=f"**{ctx.message.author.mention}HEALED{user.mention}**", color=0xff80ff)
        embed.set_image(url=f'https://media1.tenor.com/images/7a1bc74cf91eedfb0ea7027dacdc9e59/tenor.gif?itemid=20036165')
        await ctx.send(embed = embed)
# ================================================================================================================
@client.command()
async def info(ctx):
	embed=discord.Embed(title="Info about the bot", description=" ")
	embed=add_field(name="This bot is open source and BL4CK#9878 shall be credited for the making of this bot.")
	embed.set_footer(text='©BL4CK#9878')
	await ctx.send(embed = embed)
# ================================================================================================================
@client.command()
@command.has_permissions(ban_members=True)
async def ban(self, ctx, member: discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'**{user.mention} has banned**')
# ================================================================================================================
@client.command()
@command.has_permissions(administrator=True)
async def unban(self, ctx, * member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split("#")
	for ban_entry in banned_users:
		user = ban_entry.user
		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'**{user.mention} has been unbanned**')
			return
# ================================================================================================================
@client.command()
@command.has_permissions(kick_members=True)
async def kick(self, ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'**{user.mention} has been kicked**')
# ================================================================================================================

# ================================================================================================================

@client.command()
async def mention(ctx, user : discord.Member):
  await ctx.send(user.mention)
# ================================================================================================================

# ================================================================================================================
@client.command()

async def rr(ctx):
	
	bullet = random.randint(1,6)
	if bullet == 3:
		embed = discord.Embed(title=f'CRACK.')
		embed.set_author(name=f'{ctx.author.display_name} - Russian roulette',icon_url=f'{ctx.author.avatar_url}')
		embed.set_image(url=rdl('gore',random.randint(1,100)))
		embed.set_footer(text='')
		await ctx.send(embed=embed)
	if bullet == 6:
		embed = discord.Embed(title=f'CRACK.')
		embed.set_author(name=f'{ctx.author.display_name} - Russian roulette',icon_url=f'{ctx.author.avatar_url}')
		embed.set_image(url=rdl('gore',random.randint(1,100)))
		embed.set_footer(text='')
		await ctx.send(embed=embed)
	elif bullet != 3 or bullet != 6:
		await ctx.send('***Click...***')
# ================================================================================================================
@client.command()
async def rcoin(ctx):
	
	side = random.randint(1,100)
	if side == 50 or side > 50:
		embed = discord.Embed(title=f'NSFW Coinflip: Heads', color=ctx.author.color)
		embed.set_author(name=f'{ctx.author.display_name} - NSFW Coinflip',icon_url=f'{ctx.author.avatar_url}')
		embed.set_image(url=rdl('blowjob animated',random.randint(1,100)))
		embed.set_footer(text='')
		await ctx.send(embed=embed)
	elif side < 50:
		embed = discord.Embed(title=f'NSFW Coinflip: Tails', color=ctx.author.color)
		embed.set_author(name=f'{ctx.author.display_name} - NSFW Coinflip',icon_url=f'{ctx.author.avatar_url}')
		embed.set_image(url=rdl('big_ass animated',random.randint(1,100)))
		embed.set_footer(text='')
		await ctx.channel.send(embed=embed)
# ================================================================================================================
@client.command()


async def fcoin(ctx):
	side = random.randint(1,100)
	if side == 50 or side > 50:
		embed = discord.Embed(title=f'Furry Coinflip: Heads', color=ctx.author.color)
		embed.set_author(name=f'{ctx.author.display_name} - Furry Coinflip',icon_url=f'{ctx.author.avatar_url}')
		embed.set_image(url=rdl('furry blowjob animated',random.randint(1,100)))
		embed.set_footer(text='')
		await ctx.channel.send(embed=embed)
	elif side < 50:
		embed = discord.Embed(title=f'Furry Coinflip: Tails', color=ctx.author.color)
		embed.set_author(name=f'{ctx.author.display_name} - Furry Coinflip',icon_url=f'{ctx.author.avatar_url}')
		embed.set_image(url=rdl('furry tail animated',random.randint(1,100)))
		embed.set_footer(text='')
		await ctx.channel.send(embed=embed)

# ================================================================================================================
@client.command()
async def coin(ctx):
	side = random.randint(1,100)
	if side == 50 or side > 50:
		await ctx.channel.send('***The coin landed on heads***')
	if side < 50:
		await ctx.channel.send('***The coin landed on tails.***')
# ================================================================================================================
@client.command()
async def d6(ctx,arg=1):
	if arg == '':
		dside = str(random.randint(1,6))
		await ctx.channel.send(f'You rolled:' + ' ' + dside)
	else:
		try:
			aint = int(arg)
		except:
			print(f'Looks like the idiots a user and tried to provide string instead of int.')
			await ctx.channel.send('Hey idiot, send an integer, not text. Example: 6')
		mx = 6 * aint
		total = str(random.randint(1,mx))

		await ctx.channel.send(f'You rolled a total of:' + ' ' + total)
# ================================================================================================================
@client.command()
async def d8(ctx,arg=1):
	if arg == '':
		dside = str(random.randint(1,8))
		await ctx.channel.send(f'You rolled:' + ' ' + dside)
	else:
		try:
			aint = int(arg)
		except:
			print(f'Looks like the idiots a user and tried to provide string instead of int.')
			await ctx.channel.send('Hey idiot, send an integer, not text. Example: 6')
		mx = 8 * aint
		total = str(random.randint(1,mx))

		await ctx.channel.send(f'You rolled a total of:' + ' ' + total)
# ================================================================================================================
@client.command()
async def d10(ctx,arg=1):
	if arg == '':
		dside = str(random.randint(1,10))
		await ctx.channel.send(f'You rolled:' + ' ' + dside)
	else:
		try:
			aint = int(arg)
		except:
			print(f'Looks like the idiots a user and tried to provide string instead of int.')
			await ctx.channel.send('Hey idiot, send an integer, not text. Example: 6')
		mx = 10 * aint
		total = str(random.randint(1,mx))
		await ctx.send(f'You rolled a total of {total}')
# ================================================================================================================
@client.command()
async def d12(ctx,arg=1):
	if arg == '':
		dside = str(random.randint(1,12))
		await ctx.channel.send(f'You rolled:' + ' ' + dside)
	else:
		try:
			aint = int(arg)
		except:
			print(f'Looks like the idiots a user and tried to provide string instead of int.')
			await ctx.channel.send('Hey idiot, send an integer, not text. Example: 6')
		mx = 12 * aint
		total = str(random.randint(1,mx))
		await ctx.send(f'You rolled a total of {total}')
# ================================================================================================================
@client.command()
async def dc(ctx,arg1,arg2 = 1):

	a = str(arg1)
	if str(arg2) != '':
		b = str(arg2)

	print('a is equal to' + a)
	print('b is equal to' + b) # it is really this simple.
	if b == '':
		dside = str(random.randint(1,int(a)))
		await ctx.channel.send(f'You rolled:' + ' ' + dside)
	else:
		mx = int(a) * int(b)
		print('max is:' + str(mx))
		total = str(random.randint(1,mx))
	await ctx.channel.send(f'You rolled a total of:' + ' ' + total)
# ================================================================================================================
@client.command()
async def help(ctx):
	embed=discord.Embed(title="Aiko help", description="Prefix is &", color=0xff80ff)
	embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
	embed.add_field(name="`porn [tags]``", value="Polls rule34 for porn following your tags.", inline=False)
	embed.add_field(name="`d6 [dice]``", value="Rolls (a/multiple) 6 sided die. Change [dice] to add several.", inline=False)
	embed.add_field(name="`d8 [dice]``", value="Rolls (a/multiple) 8 sided die, change your [dice] argument to add several.", inline=False)
	embed.add_field(name="`d10 [dice]``", value="Rolls (a/multiple) 10 sided die, change your [dice] argument to add several.", inline=False)
	embed.add_field(name="`d12 [dice]``", value="Rolls (a/multiple) 12 sided die, change your [dice] argument to add several.", inline=False)
	embed.add_field(name="`dc <sides> [dice]``", value="Rolls a custom-sided die, change your <sides> argument to set sides, and your [dice] argument to add more dice.", inline=False)
	embed.add_field(name="`coin`", value="Flips a coin.", inline=False)
	embed.add_field(name="`rcoin`", value="Flips a coin and posts a nsfw image based on what you get.", inline=False)
	embed.add_field(name="`fcoin`", value="Flips a coin and posts a nsfw furry image based on what you get.", inline=False)
	embed.add_field(name="`rr`", value="Russian roulette. Posts gore images if gun goes off.", inline=False)
	embed.add_field(name="`shibe`", value="Posts an image of a Shiba inu.", inline=False)
	embed.add_field(name="`cat`", value="Posts an image of a cat.", inline=False)
	embed.add_field(name="`bird`", value="Posts an image of a bird.", inline=False)
	embed.add_field(name="`bird", value="Posts an image of a bird.", inline=False)
	embed.add_field(name="`yeet`",value="Yeets someone.")
	embed.add_field(name="`heal`",value="Heals someone.")
	embed.add_field(name="`kick`",value="Kicks someone.")
	embed.add_field(name="`ban`",value="Used to ban a person.")
	embed.add_field(name="`unban`",value="Unbans a person.")
	embed.add_field(name="`mention`",value="Used to test if mentions work on your server.")
	embed.add_field(name="`info`",value="Used to show the creator of the bot and the github page")
	embed.set_footer(text="",icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
	await ctx.send(embed=embed)
# ================================================================================================================
#@client.command()
# def nsfw(ctx):
 #  if ctx.channel.is_nsfw():
          # embed = discord.Embed(title="sebu pedofil", description="DA ESTE")
 #  async with aiohttp.ClientSession() as cs:
    #       async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
  #                data = await r.json()
 #                 embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar_url}')
                 # embed.set_title(name
  #                embed.set_image(url=data['url'])
            #      embed.set_footer(text="https://www.reddit.com/r/nsfw/")
#
            #      await ctx.send(embed=embed)
@client.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await client.say(submission.url)

# ================================================================================================================
@client.command()
async def shibe(ctx):
	r = requests.get('https://shibe.online/api/shibes?count=1')
	y = r.json()
	embed= discord.Embed(title='Have a shibe.',color=0xff80ff)
	embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar_url}')
	embed.set_image(url=f'{y[0]}')
	print(f"[INFO {ltime}]: IMG URL IS {y[0]}")
	embed.set_footer(text="",icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
	await ctx.send(embed=embed)

# ================================================================================================================
@client.command()
async def cat(ctx):
	r = requests.get('https://shibe.online/api/cats?count=1')
	y = r.json()
	embed = discord.Embed(title='Have a kitty.',color=0xff80ff)
	embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar_url}')
	embed.set_image(url=f'{y[0]}')
	print(f"[INFO {ltime}]: IMG URL IS {y[0]}")
	embed.set_footer(text="",icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
	await ctx.send(embed=embed)
# ================================================================================================================
@client.command()
async def bird(ctx):
	r = requests.get('https://shibe.online/api/birds?count=1')
	y = r.json()
	embed= discord.Embed(title='Have a bird.',color=0xff80ff)
	embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar_url}')
	embed.set_image(url=f'{y[0]}')
	print(f"[INFO {ltime}]: IMG URL IS {y[0]}")
	embed.set_footer(text="",icon_url='https://cdn.discordapp.com/avatars/268211297332625428/e5e43e26d4749c96b48a9465ff564ed2.png?size=128')
	await ctx.send(embed=embed)
# ================================================================================================================


client.run('YOUR TOKEN HERE')
