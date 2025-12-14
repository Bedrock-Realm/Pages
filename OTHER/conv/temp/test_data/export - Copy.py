import json

DIMENSION_MAP = {
    0: "overworld",
    1: "nether",
    2: "end"
}

def is_empty_item(item):
    return (
        item.get("Count", 0) == 0 and
        item.get("Name", "") == "" and
        item.get("tag", {}) == {}
    )

def is_empty_container(items):
    return all(is_empty_item(i) for i in items)

def is_empty_player(data):
    """
    A player is EMPTY if ALL item containers are empty.
    Position, gamemode, world, etc are ignored.
    """
    containers = [
        data.get("Inventory", []),
        data.get("EnderChestInventory", []),
        data.get("Mainhand", []),
        data.get("Offhand", []),
        data.get("Armor", [])
    ]

    return all(is_empty_container(container) for container in containers)

def transform_player(data, name, uuid):
    dimension_id = data.get("DimensionId", 0)
    world = DIMENSION_MAP.get(dimension_id, "overworld")

    spawn_dimension_id = data.get("SpawnDimension", dimension_id)
    spawn_dimension = DIMENSION_MAP.get(spawn_dimension_id, "overworld")

    return {
        "name": name,
        "xuid": "2535460561105730",
        "uuid": uuid,
        "world": world,
        "SpawnDimension": spawn_dimension,
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
    with open("playerdata.json", "r", encoding="utf-8") as f:
        all_players_data = json.load(f)

    players_list = []
    skipped = 0

    for server_uuid, nbt_data in all_players_data.items():

        if is_empty_player(nbt_data):
            skipped += 1
            print(f"⚠ Skipped empty player (no items): {server_uuid}")
            continue

        player = transform_player(
            nbt_data,
            name=server_uuid,
            uuid=server_uuid
        )
        players_list.append(player)
        print(f"✓ Processed player: {server_uuid}")

    output_json = {
        "max": len(players_list),
        "players": players_list
    }

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=2)

    print(
        f"\n✅ Conversion complete! "
        f"Processed {len(players_list)} players, "
        f"skipped {skipped} empty players."
    )
