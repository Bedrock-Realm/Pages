import json


def transform_player(data, name="BehaviorPack"):
    """Convert full NBT JSON into your desired schema"""
    player = {
        "name": name,
        "xuid": "2535460561105730",
        "uuid": "f45e5bf0-05cc-45b1-a3b9-9eb74bb3ae35",
        "world": "overworld",
        "playergamemode": data.get("PlayerGameMode", 0),
        "x": int(data.get("Pos", [0, 0, 0])[0]),
        "y": int(data.get("Pos", [0, 0, 0])[1]),
        "z": int(data.get("Pos", [0, 0, 0])[2]),
        "rotation": data.get("Rotation", []),
        "SpawnX": data.get("SpawnBlockPositionX", 0),
        "SpawnY": data.get("SpawnBlockPositionY", 0),
        "SpawnZ": data.get("SpawnBlockPositionZ", 0),
        "DeathX": data.get("DeathPositionX", 0),
        "DeathY": data.get("DeathPositionY", 0),
        "DeathZ": data.get("DeathPositionZ", 0),
        "inventory": [extract_item(i) for i in data.get("Inventory", [])],
"enderchestinventory": [extract_item(i) for i in data.get("EnderChestInventory", [])],
"mainhand": [extract_item(i) for i in data.get("Mainhand", [])],
"offhand": [extract_item(i) for i in data.get("Offhand", [])],
"armor": [extract_item(i) for i in data.get("Armor", [])],
    }
    return {"max": 1, "players": [player]}
    
def extract_item(i):
    return {
        "Count": i.get("Count", 0),
        "Damage": i.get("Damage", 0),
        "Name": i.get("Name", ""),
        "Slot": i.get("Slot", 0),
        "WasPickedUp": i.get("WasPickedUp", 0),
        "tag": i.get("tag", {})
    }

if __name__ == "__main__":
    # Load the JSON exported from nbtlib
    with open("playerdata.json", "r", encoding="utf-8") as f:
        nbt_data = json.load(f)

    # Transform into desired output
    output_json = transform_player(nbt_data)

    # Save to output.json
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=2)

    print("✅ Conversion complete! Saved to output.json")
