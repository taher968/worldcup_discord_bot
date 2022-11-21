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
    return data

def get_times(data):
    time = list()
    for i in data:
        datetime_obj = datetime.strptime(i['DateUtc'], '%Y-%m-%d %H:%M:%S')
        local_time = utc_to_local(datetime_obj)
        # time[i] = local_time.time()
        time.append(local_time)
    return time


    # print(datetime.now().time())

def find_matches(data, time):
    current_date = datetime.now().date()
    # current_date = current_time.date()

    send_message = "Today's games are: \n"

    for i in range(0,len(time)):
        if time[i].date() == current_date:
            send_message = send_message + data[i]['HomeTeam'] + " vs " + data[i]['AwayTeam'] + " " + time[i].strftime("%H:%M") + " EST" + "\n"
    
    return send_message


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    data = load_data()
    time = get_times(data)


    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('!matches'):
            # time = datetime.now().time()
            send_message = find_matches(data,time)
            await message.channel.send(send_message)

    client.run(get_token())


if __name__ == "__main__":
    main()