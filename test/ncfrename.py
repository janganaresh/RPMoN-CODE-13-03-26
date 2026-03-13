import os
import pandas as pd
from PIL import Image

#asessment folserds from mobile will rename with assid and redue the some size
excel_path = r"C:\Users\LENOVO\Downloads\nocoderename (4).xlsx"
base_path = r"C:\Users\LENOVO\Desktop\area5asspics"

df = pd.read_excel(excel_path)
df.columns = df.columns.str.strip()

for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path):
        parts = folder.split("_")
        if len(parts) >= 4:
            table_id = parts[1] + parts[2]   
            pile_no = parts[3].replace("P", "")  


            match = df[
                (df["Table ID"].astype(str).str.upper() == table_id.upper()) &
                (df["Pile No"].astype(str) == pile_no)
            ]

            if not match.empty:
                assessment_id = match.iloc[0]["Assessment ID"]

                images = [f for f in os.listdir(folder_path)
                          if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

                for i, img in enumerate(sorted(images), start=1):
                    ext = os.path.splitext(img)[1]
                    new_img_name = f"{assessment_id}_{table_id}_Pile{pile_no}_Side{i}.jpg" 
                    old_img_path = os.path.join(folder_path, img)
                    new_img_path = os.path.join(folder_path, new_img_name)

                    with Image.open(old_img_path) as im:
                        im = im.convert("RGB")  
                        im.save(new_img_path, "JPEG", quality=20, optimize=True)  
                    

                    os.remove(old_img_path)  
                    print(f"Compressed + Renamed: {img} → {new_img_name}")

              
                new_folder_path = os.path.join(base_path, assessment_id)
                os.rename(folder_path, new_folder_path)
                print(f"Folder renamed: {folder} → {assessment_id}\n")

            else:
                print(f"No match found for folder: {folder}")
        else:
            print(f"Skipping invalid folder: {folder}")

print(" Done renaming + compressing images!")