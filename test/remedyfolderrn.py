import os
import pandas as pd
from PIL import Image
from mysql.connector import pooling

# here remedy folders from mobile will rename and in db pic loaction will update
# === DATABASE CONNECTION POOL ===
db_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=10,
    host="localhost",
    user="root",
    password="nare@2058",
    database="remedydb",
    autocommit=True,
    connection_timeout=60
)

def get_db_connection():
    return db_pool.get_connection()

# === CONFIG ===
excel_path = r"C:\Users\LENOVO\Downloads\remedyfolderidsmd1.xlsx"
base_path = r"C:\Users\LENOVO\Desktop\remedypics"
remedy_pictures_base = r"C:\Users\LENOVO\Desktop\RemedyPictures"

# === LOAD EXCEL ===
df = pd.read_excel(excel_path)
df.columns = df.columns.str.strip()

# === MAIN LOOP ===
for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if not os.path.isdir(folder_path):
        continue

    parts = folder.split("_")
    if len(parts) >= 4:
        table_id = parts[1] + parts[2]        # Example: C22S2
        pile_no = parts[3].replace("RP", "").replace("P", "")  # Remove R

        # Match Excel rows
        match = df[
            (df["Table ID"].astype(str).str.upper() == table_id.upper()) &
            (df["Pile No"].astype(str) == pile_no)
        ]

        if not match.empty:
            remedy_id = str(match.iloc[0]["Remedy ID"]).strip()

            # Compress + rename all images in folder
            images = [
                f for f in os.listdir(folder_path)
                if f.lower().endswith(('.jpg', '.jpeg', '.png'))
            ]

            for i, img in enumerate(sorted(images), start=1):
                new_img_name = f"{remedy_id}_{table_id}_Pile{pile_no}_Side{i}.jpg"
                old_img_path = os.path.join(folder_path, img)
                new_img_path = os.path.join(folder_path, new_img_name)

                try:
                    with Image.open(old_img_path) as im:
                        im = im.convert("RGB")
                        im.save(new_img_path, "JPEG", quality=40, optimize=True)
                    os.remove(old_img_path)
                    print(f"Compressed + Renamed: {img} → {new_img_name}")
                except Exception as e:
                    print(f"Error compressing {img}: {e}")

            # Rename folder → Remedy ID
            new_folder_path = os.path.join(base_path, remedy_id)
            os.rename(folder_path, new_folder_path)
            print(f"Folder renamed: {folder} → {remedy_id}")

            # Build Picture Location path
            picture_location = os.path.join(remedy_pictures_base, remedy_id)

            # === Update DB only for matched Remedy IDs ===
            try:
                conn = get_db_connection()
                cursor = conn.cursor()

                # UPDATED QUERY — added Date Completed = CURDATE()
                cursor.execute(
                    """
                    UPDATE remedy 
                    SET 
                        `Picture Location` = %s,
                        `Date Completed` = CURDATE()
                    WHERE `Remedy ID` = %s
                    """,
                    (picture_location, remedy_id)
                )

                conn.close()
                print(f"✅ DB updated for Remedy ID: {remedy_id}")
            except Exception as e:
                print(f"⚠️ Database update failed for {remedy_id}: {e}")

        else:
            print(f"No match found for folder: {folder}")
    else:
        print(f"Skipping invalid folder: {folder}")

print(" Done — Only matched folders renamed, compressed, and DB updated.")
