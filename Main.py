import discord


client = discord.Client()

token = open("token.txt","r").read()


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 722558183033405525:
        print(payload.emoji.name)
        # Find a role corresponding to the Emoji name.
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        role = discord.utils.find(lambda r : r.name == payload.emoji.name, guild.roles)

        if role is not None:
            print(role.name + " was found!")
            print(role.id)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.add_roles(role)
            print("done")

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 722558183033405525:
        print(payload.emoji.name)

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        role = discord.utils.find(lambda r : r.name == payload.emoji.name, guild.roles)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
            print("done")

@client.event
async def on_ready():
    print("Bot is ready!")

client.run(token)