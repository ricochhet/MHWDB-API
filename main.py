import requests
import json

MHW_URLS = [
    {"name": "Ailments", "url": "https://mhw-db.com/ailments"},
    {"name": "Armor", "url": "https://mhw-db.com/armor"},
    {"name": "ArmorSets", "url": "https://mhw-db.com/armor/sets"},
    {"name": "Charms", "url": "https://mhw-db.com/charms"},
    {"name": "Decorations", "url": "https://mhw-db.com/decorations"},
    {"name": "Items", "url": "https://mhw-db.com/items"},
    {"name": "Locations", "url": "https://mhw-db.com/locations"},
    {"name": "Monsters", "url": "https://mhw-db.com/monsters"},
    {"name": "MotionValues", "url": "https://mhw-db.com/motion-values"},
    {"name": "Skills", "url": "https://mhw-db.com/skills"},
    {"name": "Weapons", "url": "https://mhw-db.com/weapons"},
]


def GAME_MHW():
  for i in MHW_URLS:
    response = requests.get(i["url"])
    response.raise_for_status()
    with open(f"./databases/Game/MHW/{i['name']}.json", 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)


GAME_MHW()
