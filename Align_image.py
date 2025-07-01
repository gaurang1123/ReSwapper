import os
import cv2
import numpy as np
from insightface.app import FaceAnalysis
from insightface.utils import face_align

# Configuration
input_dir = 'images_jpg'
output_dir = 'output_faces'
gender_filter = 'female'  # options: 'male', 'female', or None for no filter

os.makedirs(output_dir, exist_ok=True)

# Initialize InsightFace
app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0)

# Process images
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_dir, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f"[ERROR] Could not read {filename}")
            continue

        faces = app.get(img)

        if not faces:
            print(f"[INFO] No face detected in {filename}")
            continue

        for i, face in enumerate(faces):
            gender = 'male' if face.gender == 1 else 'female'

            # Apply gender filter
            if gender_filter and gender != gender_filter:
                continue

            # Align and crop face
            aligned_face = face_align.norm_crop(img, face.kps)

            # Save face
            face_filename = f"{os.path.splitext(filename)[0]}_{gender}_face{i+1}.jpg"
            cv2.imwrite(os.path.join(output_dir, face_filename), aligned_face)
            print(f"[SAVED] {face_filename}")

print("✅ Done processing all images.")
