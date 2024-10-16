import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def calculadora(ctx, operacion = "", num1 = 0, num2 = 0):
    if operacion  == "suma":
        resultado = num1 + num2

    elif operacion  == "resta":
        resultado = num1 - num2  

    elif operacion  == "multiplicacion" or operacion == "multiplicación":
        resultado = num1 * num2

    elif operacion  == "division" or operacion == "división":
        if num2 != 0:   
            resultado = num1 / num2

    else: 
        await ctx.send("Esta calculadora es de matemáticas básicas: + - x ÷")
        return

    await ctx.send(f"El resultado de tu {operacion} es: {resultado}")      

@bot.command()
async def flip_coin(ctx, flip = ""):
    flip = random.randint(0,2)
    if flip == 0:
        await ctx.send("CARA!!")
    else:
        await ctx.send("CRUZ!!")      

                

bot.run("TOKEN")
