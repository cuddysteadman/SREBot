import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)
latest_release = "0.0.4"
latest_prerelease = "0.0.5-pre1"
latest_alpharelease = "0.0.4-pre2-pre3 (deprecated)"
@client.event
async def on_ready() :
  print("We have logged in as {0.user}".format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$sre"))
@client.event
async def on_member_join(member):
  channel = client.get_channel(826819255320051774)
  await member.send("Welcome {} to the SkyblockReinvented Discord Server! \nI'm SREBot. I'm here to make your experience here more enjoyable! You can type $sre help in the #bot-commands channel on the SRE Discord to find out more info about what I can do. \nI hope you enjoy your stay!".format(member.mention))
@client.event
async def on_message(message):
  if message.channel.id != 825780174368407602 and message.channel.id != 825770755052404756:
    return
  if message.author == client.user:
    return
  if message.content == "$sre":
    await message.channel.send("Please enter a command! You can do $sre help for a list of commands.")
  if message.content.startswith("$sre github"):
    await message.channel.send("The github for SRE is: https://github.com/theCudster/SkyblockReinvented")
  if message.content.startswith("$sre discord"):
    await message.channel.send("The Discord link is https://discord.gg/xkeYgZrRbN ! Invite your friends!")
  if message.content.startswith("$sre rules"):
    await message.channel.send("1. Follow the Discord TOS.\n2. Use channels appropriately. \n3. Foul language is allowed as long as it is not directed anyone. \n4. No impersonating. \n5. No NSFW content. \n6. No spamming.\n7. Feel free to ping me if you need support with the mod or want to discuss code / features. This does NOT include the #suggestion-discussion channel - I will look at your suggestions individually and come to YOU with questions. \n8. If you ping for a reason other than above, you will be warned.\n 9. 3 warns = ban.\n10. Do not send files directly to members of the server. Let me know if you have code to discuss. (This is part of rule 7, but I wanted to clarify")
  if message.content.startswith("$sre help"):
    await message.channel.send("My commands are:\n$sre discord \n$sre github \n$sre acknowledgements\n$sre rules\n$sre release\n$sre prerelease\n$sre alpharelease")
  if message.content.startswith("$sre acknowledgements"):
    await message.channel.send("Sychic, My-Name-Is-Jeff, Angry-Pineapple3121, and AzuredBlue (Skytils: https://github.com/Skytils/SkytilsMod)\nMoulberry (NEU: https://github.com/Moulberry/NotEnoughUpdates)\nCobble8 (SkyblockPersonalized: https://github.com/Cobble8/SkyblockPersonalized)\nBiscuit (SkyblockAddons: https://github.com/BiscuitDevelopment/SkyblockAddons)\nbowser0000 (Danker's Skyblock Mod: https://github.com/bowser0000/SkyblockMod)\nSk1er LLC (ModCore: https://github.com/Sk1erLLC (not exactly a github, but it was the closest I could find since the source code isn't public to my knowledge))")
  if message.content.startswith("$sre release"):
    await message.channel.send(("The latest release is " + latest_release + ". You can find it in {0.mention}.").format(client.get_channel(825779822399193138)))
  if message.content.startswith("$sre alpharelease"):
    await message.channel.send(("The latest alpharelease is " + latest_alpharelease + ". You can find it in {0.mention}.".format(client.get_channel(829393703483211807))))
  if message.content.startswith("$sre prerelease"):
    await message.channel.send(("The latest prerelease is " + latest_prerelease + ". You can find it in {0.mention}.").format(client.get_channel(825539271431553024)))
client.run('ODI2MTUyNTQ2ODYyNzU5OTY2.YGIUhA.Wpp2npCFfpy8RdQ_1Gk0wB_HYRQ')