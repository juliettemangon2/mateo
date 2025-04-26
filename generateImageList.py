import os, json

base = "mateoSamples"
exts = (".jpg", ".jpeg", ".png", ".webp")

# 1) collect shoots
shoots = {}
for root, _, files in os.walk(base):
    # root = mateoSamples/shootFolder
    parts = root.split(os.sep)
    if len(parts) == 2 and files:  # exactly one level down
        shoot = parts[1]
        shoots[shoot] = sorted(
            os.path.join(root, f).replace("\\","/")
            for f in files if f.lower().endswith(exts)
        )

# 2) write shoots.json
out_shoots = []
for shoot, images in shoots.items():
    out_shoots.append({
        "name": shoot,
        "title": shoot.replace("-", " ").replace("_"," ").title(),
        "cover": images[0],        # first image as cover
        "json": f"{shoot}.json"
    })
with open("shoots.json", "w") as f:
    json.dump(out_shoots, f, indent=2)

# 3) write one JSON per shoot
for shoot, images in shoots.items():
    with open(f"{shoot}.json", "w") as f:
        json.dump(images, f, indent=2)

print("Wrote shoots.json and individual shoot JSON files.")
