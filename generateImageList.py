import os, json

BASE_DIR = "mateoSamples"
VALID_EXTS = (".jpg", ".jpeg", ".png", ".webp")

# 1) Discover each subfolder under BASE_DIR, collect its images
shoots = {}
for root, dirs, files in os.walk(BASE_DIR):
    # only consider immediate subdirectories
    parts = root.split(os.sep)
    if len(parts) == 2 and files:
        shoot_name = parts[1]
        # full paths for each valid image
        images = sorted(
            os.path.join(root, f).replace("\\", "/")
            for f in files
            if f.lower().endswith(VALID_EXTS)
        )
        if images:
            shoots[shoot_name] = images

# 2) Write the master index: shoots.json
out_shoots = []
for name, images in shoots.items():
    out_shoots.append({
        "name": name,
        "title": name.replace("-", " ").replace("_", " ").title(),
        "cover": images[0],       # first image as cover tile
        "json": f"{name}.json"
    })

with open("shoots.json", "w") as f:
    json.dump(out_shoots, f, indent=2)

# 3) Write one JSON per shoot, listing its full images array
for name, images in shoots.items():
    with open(f"{name}.json", "w") as f:
        json.dump(images, f, indent=2)

print("✔ Wrote shoots.json and individual shoot JSON files")
