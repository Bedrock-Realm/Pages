const fs = require("fs");

// Read the file
const data = JSON.parse(fs.readFileSync("items.json", "utf8"));

// Access inventory
const inventory = data.players[0].inventory;

// Remove duplicates by Name
const seen = new Set();
const uniqueInventory = inventory.filter((item) => {
  if (seen.has(item.Name)) return false;
  seen.add(item.Name);
  return true;
});

// Replace inventory with unique list
data.players[0].inventory = uniqueInventory;

// Save back to file
fs.writeFileSync("items_clean.json", JSON.stringify(data, null, 2));

console.log("✅ Duplicates removed! Cleaned file saved as items_clean.json");
