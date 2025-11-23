## 👤 **Player Data Workflow**

### **1. Extract Player Files**
1. Open **Universal Minecraft Editor**
2. Export each player as a `.dat` file
3. Place all exported files into the `conv/` folder

### **2. Prepare the Conversion File**
Rename the player file you want to process:

    Player-UUID.dat → playerdata.dat

Make sure it lives inside the `conv/` directory.

### **3. Convert `.dat` → `.json`**
Run the conversion script:

    python datTojson.py

This produces:

    playerdata.json

### **4. Export Final Output**
Run:

    python export.py

This generates:

    output.json

Copy the results and merge it into:

    players.json

---

## 🗺️ **Map Exporting**

### **Export the Full Realm Map**
1. Open **Unmined**
2. Load your **RealmWorld**
3. Export the entire world map as a **1.1 PNG** (full-world render)

---
