import json
async def get_channel(guild_id):
  with open ("channel.json", "r") as f:
    prefixes = json.load(f)
  try:
    return prefixes[str(guild_id)]
  except NameError:
    return "no channel found"