import json
async def get_action(guild_id):
  with open ("action.json", "r") as f:
    prefixes = json.load(f)
  try:
    return prefixes[str(guild_id)]
  except NameError:
    return "B"

async def get_mute_role(guild_id):
  with open ("m_role.json", "r") as f:
    prefixes = json.load(f)
  try:
    return prefixes[str(guild_id)]
  except NameError:
    return "null"

