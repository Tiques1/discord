import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready() -> None:
    print(f"Logged in as {client.user}")

@tasks.loop(minutes=0.1)  # измените интервал, если нужно
async def update_channel_name():
    guild_id = 1089140452701257758  # замените на ID вашего сервера
    guild = client.get_guild(guild_id)
    if guild:
        role_names = ['Администратор', 'Член Совета директоров']
        channel = discord.utils.get(guild.channels, id=1239943762659115008)
        if channel:
            member_count = sum(1 for member in guild.members if any(role.name in role_names for role in member.roles))
            await channel.edit(name=f'Участников: {member_count}')
        else:
            print('Канал не найден')

update_channel_name.start()
client.run(TOKEN)
