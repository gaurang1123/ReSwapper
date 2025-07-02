import os
from PIL import Image

FOLDER = input("Enter follder name")  # Folder containing the original images

# Sequential naming (optional)
use_sequential_names = False

for idx, fname in enumerate(sorted(os.listdir(FOLDER))):
    if not fname.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')):
        continue
    input_path = os.path.join(FOLDER, fname)
    try:
        im = Image.open(input_path).convert("RGB")

        if use_sequential_names:
            out_name = f"image_{idx+1:04d}.jpg"
        else:
            out_name = os.path.splitext(fname)[0] + ".jpg"
        
        out_path = os.path.join(FOLDER, out_name)
        im.save(out_path, "JPEG", quality=95)
        
        # Remove original file if it has a different extension
        if out_name.lower() != fname.lower():
            os.remove(input_path)

        print(f"Saved and replaced: {out_path}")
    except Exception as e:
        print(f"Failed to convert {fname}: {e}")
