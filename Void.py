# https://discordapp.com/oauth2/authorize?client_id=601852212041351168&scope=bot&permission=67648       Invitation Link

import discord

def server_report(server):
    online_members = 0
    offline_members = 0
    idle_dnd_members = 0
    for people in server.members:
        if str(people.status) == "online":
            online_members+=1
        if str(people.status) == "offline":
            offline_members+=1
        if str(people.status)!= "online":
            if str(people.status)!= "offline":
                idle_dnd_members+=1
    return online_members, offline_members, idle_dnd_members

client = discord.Client()
status = discord.Game("void.help() for help")
help_message = open("help.txt", "r").read()

@client.event                   #event decorator/wrappper
async def on_ready():
    print(f"We have logged in as {client.user}")
    await client.change_presence(status=discord.Status.online, activity=status)

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    server = client.get_guild(601857155997499543)                                        #Change this before deploying to osiris

    if "void.greet()" == message.content.lower():
        await message.channel.send("```Welcome to Osiris!!!```")

    if "void.quote()" == message.content.lower():
        await message.channel.send("```\nFight for 'honour' or for 'loyalty'...\nYou might as well be fighting for dust. If you want to do it, do it for your own sake!```")

    if "void.member_count()" == message.content.lower():
        await message.channel.send(f"```py\nMembers: {server.member_count}```")

    if "void.server_report()" == message.content.lower():
        online, offline, idle = server_report(server)
        await message.channel.send(f"```py\nSERVER REPORT\n\nOnline: {online}\nIdle/Do Not Disturb: {idle}\nOffline: {offline}```")

    if "void.info()" == message.content.lower(): 
        await message.channel.send("Beep Bop Beep, My name is Void and I am a Discord Bot")
        await message.channel.send("```\nCoded by: Kartikeya Shorya (@PredatorK9#6682)\nLanguage: Python```")

    if "void.help()" == message.content.lower():
        await message.channel.send("*Here are the list of commands for your boi*    (**Void**)")
        await message.channel.send(f"```{help_message}```")

    if "void.shutdown()" == message.content:
        if "PredatorK9#6682" == str(message.author):
            await message.channel.send("```Shutting Down...```")
            await client.logout()
        else:
            await message.channel.send("```PERMISSION DENIED```")

client.run("Your Token Here")
