import os
from PIL import Image

INPUT_FOLDER = "images"          # Change to your folder name
OUTPUT_FOLDER = "images_jpg"     # Output folder for jpgs

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Sequential numbering (optional)
# If you want to preserve original names, comment out the next line
use_sequential_names = False

for idx, fname in enumerate(sorted(os.listdir(INPUT_FOLDER))):
    if not fname.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')):
        continue
    input_path = os.path.join(INPUT_FOLDER, fname)
    try:
        im = Image.open(input_path).convert("RGB")
        if use_sequential_names:
            out_name = f"image_{idx+1:04d}.jpg"
        else:
            out_name = os.path.splitext(fname)[0] + ".jpg"
        out_path = os.path.join(OUTPUT_FOLDER, out_name)
        im.save(out_path, "JPEG", quality=95)
        print(f"Saved: {out_path}")
    except Exception as e:
        print(f"Failed to convert {fname}: {e}")