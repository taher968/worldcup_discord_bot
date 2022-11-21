import discord
import os
from secret import *
import json
from datetime import datetime, timezone
import time

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


def load_data():
    world_cup_data = []

    file = open('worldcup_data.json')
    data = json.load(file)

    for i in data:
        datetime_obj = datetime.strptime(i['DateUtc'], '%Y-%m-%d %H:%M:%S')
        local_time = utc_to_local(datetime_obj)
        time = local_time.time()
        # print(time)

    # print(datetime.now().time())

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)


    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!matches'):
            time = datetime.now().time()
            await message.channel.send(time)

    client.run(get_token())


if __name__ == "__main__":
    main()