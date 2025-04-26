import os
import json

base_folder = "mateoSamples"
extensions = (".jpg", ".jpeg", ".png", ".webp")

shoots = {}

# walk through mateoSamples and group images by subfolder
for root, dirs, files in os.walk(base_folder):
    for file in files:
        if file.lower().endswith(extensions):
            folder = os.path.relpath(root, base_folder)
            if folder not in shoots:
                shoots[folder] = []
            shoots[folder].append(os.path.join(root, file).replace("\\", "/"))

# Save a master shoots.json file
shoot_list = []
for shoot, images in shoots.items():
    if images:
        shoot_list.append({
            "name": shoot,
            "cover": images[0]   # first image of folder = cover photo
        })

with open("shoots.json", "w") as f:
    json.dump(shoot_list, f, indent=2)

# Save a separate JSON per shoot
for shoot, images in shoots.items():
    filename = shoot.replace(" ", "_").lower() + ".json"
    with open(filename, "w") as f:
        json.dump(images, f, indent=2)

print("Done!")
