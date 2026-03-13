import os
from PIL import Image as PilImage  

# === CONFIG ===
base_path = r"C:\Users\LENOVO\Desktop\RenamedFolders"
start_folder = "AS02208"
end_folder = "AS02700"

# === FUNCTION TO CHECK FOLDER RANGE ===
def is_in_range(folder_name):
    try:
        num = int(folder_name[2:])  # extract numeric part e.g. 2280 from AS02280
        return int(start_folder[2:]) <= num <= int(end_folder[2:])
    except ValueError:
        return False

# === MAIN LOOP ===
for folder in os.listdir(base_path):
    if not is_in_range(folder):
        continue

    folder_path = os.path.join(base_path, folder)
    if not os.path.isdir(folder_path):
        continue

    print(f"Compressing images in: {folder}")

    # Loop through images
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(folder_path, file)
            try:
                with PilImage.open(img_path) as img:
                    # Convert PNGs or palette images to RGB
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    # Compress (adjust quality as needed)
                    img.save(img_path, "JPEG", quality=30, optimize=True)
            except Exception as e:
                print(f"Error compressing {file} in {folder}: {e}")

print("✅ All selected folders compressed successfully.")
