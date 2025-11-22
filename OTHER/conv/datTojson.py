# First, install nbtlib if you don't have it:
# pip install nbtlib

import nbtlib
import json

# Load the NBT file
nbt_file = nbtlib.load("playerdata.dat")  # <-- your player NBT file

# The root compound is the nbt_file itself
data = nbt_file  # no need for .root or [None]

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


data_dict = nbt_to_dict(data)

# Convert to JSON string
json_str = json.dumps(data_dict, indent=2)

# Save it
with open("playerdata.json", "w") as f:
    f.write(json_str)

print("NBT successfully converted to JSON!")
