from PIL import Image, ImageDraw, ImageFont
import os

# Settings
output_folder = "mateoSamples"
image_sizes = [(1200, 800), (800, 1200), (1000, 1000)]  # Landscape, Portrait, Square
num_images_per_size = 5
font_size = 120
font_color = 50  # Dark gray text

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load a font (fallback to default if arial not found)
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except:
    font = ImageFont.load_default()

# Generate images
image_count = 1
for size in image_sizes:
    width, height = size
    for i in range(1, num_images_per_size + 1):
        # Create a gray image
        img = Image.new('L', size, color=200)  # 'L' = grayscale mode

        # Draw the image number in the center
        draw = ImageDraw.Draw(img)
        text = str(image_count)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        position = ((width - text_width) // 2, (height - text_height) // 2)
        draw.text(position, text, fill=font_color, font=font)

        # Save the image
        filename = f"{image_count:02}.jpg"
        img.save(os.path.join(output_folder, filename))
        image_count += 1
