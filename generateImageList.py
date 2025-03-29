import os
import json

folder = "mateoSamples"
extensions = (".jpg", ".jpeg", ".png", ".webp")

image_list = sorted([f for f in os.listdir(folder) if f.lower().endswith(extensions)])

with open("images.json", "w") as f:
    json.dump(image_list, f)
