import discord
from discord.ext import commands

# Replace with your bot token (don't share it publicly!)
TOKEN = 'Token girin'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} çevrimiçi!')

# Define the dictionary
sözlük = {
    "Plastik": "Dönüştürülebilir",
    "Karton": "Dönüştürülebilir",
    "Strafor": "Dönüştürülemez",
    "Metal": "Dönüşebilir",
    "Uranyum": "Dönüşemez",
    "Pil": "Dönüşebilir",
    "Fosil Yakıt": "Dönüştürülemez"
}

@bot.command()
async def gdmi(ctx, malzeme):

    malzeme = malzeme.lower()

    if malzeme in sözlük:
        await ctx.send(sözlük[malzeme])
    else:
        await ctx.send("Bu malzeme sözlükte bulunmuyor!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Bu komut için gerekli argümanları eksiksiz girin!')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('Bu geçerli bir komut değil!')
    elif isinstance(error, KeyError):
        await ctx.send("Bu malzeme sözlükte bulunmuyor!")

bot.run(TOKEN)
