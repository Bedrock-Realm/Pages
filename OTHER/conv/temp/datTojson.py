# First, install nbtlib if you don't have it:
# pip install nbtlib
import nbtlib
import json
import glob
import os

# Convert NBT to a standard Python dict
def nbt_to_dict(tag):
    if isinstance(tag, nbtlib.Compound):
        return {k: nbt_to_dict(v) for k, v in tag.items()}
    elif isinstance(tag, nbtlib.List):
        return [nbt_to_dict(i) for i in tag]
    elif isinstance(tag, nbtlib.ByteArray) or isinstance(tag, nbtlib.IntArray) or isinstance(tag, nbtlib.LongArray):
        return list(tag)  # convert arrays to regular Python lists
    else:
        return tag  # int, float, str, etc.

# Find all .dat files in current directory
dat_files = glob.glob("*.dat")

if not dat_files:
    print("No .dat files found in current directory!")
else:
    # Dictionary to hold all player data
    all_players = {}
    
    for dat_file in dat_files:
        try:
            # Load the NBT file
            nbt_file = nbtlib.load(dat_file)
            
            # Convert to dict
            data_dict = nbt_to_dict(nbt_file)
            
            # Use filename (without extension) as key
            player_id = os.path.splitext(dat_file)[0]
            all_players[player_id] = data_dict
            
            print(f"✓ Processed: {dat_file}")
        except Exception as e:
            print(f"✗ Error processing {dat_file}: {e}")
    
    # Save all player data to one JSON file
    with open("playerdata.json", "w") as f:
        json.dump(all_players, f, indent=2)
    
    print(f"\n✓ Successfully converted {len(all_players)} player files to playerdata.json!")