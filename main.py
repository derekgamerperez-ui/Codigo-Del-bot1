
import discord
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(
                model_path='./keras_model.h5',
                labels_path='./labels.txt',
                image_path=f'./{attachment.filename}'
            ))
    else:
        await ctx.send("You forgot to upload the image :(")


@bot.command()
async def ping(ctx):
    latencia = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong! Latencia: {latencia} ms")


@bot.command()
async def hola(ctx):
    await ctx.send(f"👋 ¡Hola, {ctx.author.mention}! ¿Qué tal?")


@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)
    await ctx.send(f"🎲 Te salió un **{numero}**")


@bot.command()
async def moneda(ctx):
    resultado = random.choice(["Cara 🪙", "Cruz 🪙"])
    await ctx.send(f"El resultado es: **{resultado}**")


@bot.command()
async def ayuda_bot(ctx):
    mensaje = """
🤖 COMANDOS DEL BOT

🔍 !check — clasifica una imagen con IA (en desarrollo).
🏓 !ping — comprueba la latencia.
👋 !hola — saluda al usuario.
🎲 !dado — lanza un dado.
🪙 !moneda — lanza una moneda.
ℹ️ !info — muestra información del bot.
"""
    await ctx.send(mensaje)


@bot.command()
async def info(ctx):
    await ctx.send(
        f"🤖 **{bot.user.name}**\n"
        f"🆔 ID: `{bot.user.id}`\n"
        f"📡 Latencia: `{round(bot.latency * 1000)} ms`\n"
        f"🧠 Bot con sistema de clasificación de imágenes mediante IA.\n"
        f"🚧 El comando !check está en desarrollo."
    )
