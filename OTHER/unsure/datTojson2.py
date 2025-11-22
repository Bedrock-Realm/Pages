# dats_to_merged_json.py
# pip install nbtlib

import nbtlib
import json
import os


def nbt_to_dict(tag):
    if isinstance(tag, nbtlib.Compound):
        return {k: nbt_to_dict(v) for k, v in tag.items()}
    elif isinstance(tag, nbtlib.List):
        return [nbt_to_dict(i) for i in tag]
    elif isinstance(tag, (nbtlib.ByteArray, nbtlib.IntArray, nbtlib.LongArray)):
        return list(tag)
    else:
        return tag  # int, float, str, etc.


def extract_item(i):
    return {
        "Count": i.get("Count", 0),
        "Damage": i.get("Damage", 0),
        "Name": i.get("Name", ""),
        "Slot": i.get("Slot", 0),
        "WasPickedUp": i.get("WasPickedUp", 0),
        "tag": i.get("tag", {})
    }


def transform_player(data, uuid, name="Unknown"):
    """Convert full NBT JSON into your desired schema"""
    player = {
        "name": name,
        "xuid": "2535460561105730",
        "uuid": uuid,
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
    return player


if __name__ == "__main__":
    folder = "."  # current folder, change if needed
    all_players = []

    for filename in os.listdir(folder):
        if filename.endswith(".dat"):
            file_path = os.path.join(folder, filename)
            try:
                nbt_file = nbtlib.load(file_path)
                data_dict = nbt_to_dict(nbt_file)
                uuid = os.path.splitext(filename)[0]  # use filename as UUID
                player_data = transform_player(data_dict, uuid)
                all_players.append(player_data)
                print(f"✅ Processed {filename}")
            except Exception as e:
                print(f"❌ Failed to process {filename}: {e}")

    # Merge all players into one JSON
    output_json = {
        "max": len(all_players),
        "players": all_players
    }

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=2)

    print(f"🎉 Done! {len(all_players)} players saved to output.json")
