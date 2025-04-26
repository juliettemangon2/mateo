import os
import json

folder = "exhibits"
files = []

for filename in os.listdir(folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.heic')):
        files.append(f"{folder}/{filename}")

# Save to exhibits.json
with open("exhibits.json", "w") as f:
    json.dump(files, f, indent=2)

print(f"Wrote {len(files)} files to exhibits.json")
