import os
import pandas as pd
import shutil

# for uploading the foldersin mms ,by using this we can rename as per the serial number.
# Excel file path
excel_path = r'C:\Users\LENOVO\Desktop\AssessmentSerial_No.xlsx'

# Source folder (where original folders exist)
source_base = r'C:\Users\LENOVO\Desktop\AssessmentPictures'

# Destination folder (where renamed folders will be copied)
destination_base = r'C:\Users\LENOVO\Desktop\RenamedFolders'

# Create destination folder if it doesn't exist
os.makedirs(destination_base, exist_ok=True)

# Read Excel
df = pd.read_excel(excel_path)

# ✅ Filter only rows where Sl.No >= 1509
df = df[df['Sl.No'] >= 2208]

# Loop through each row
for index, row in df.iterrows():
    sl_no = int(row['Sl.No'])  # e.g., 1509
    old_name = str(row['Assessment ID']).strip()  # e.g., AS01628
    new_name = f"AS{sl_no:05d}"  # e.g., AS01509

    old_path = os.path.join(source_base, old_name)
    new_path = os.path.join(destination_base, new_name)

    if not os.path.exists(old_path):
        print(f"❌ Folder not found: {old_path}")
        continue

    # If folder with new name already exists, add a dot
    if os.path.exists(new_path):
        new_path += '.'
        print(f"⚠️ {new_name} already exists in destination. Renaming to: {os.path.basename(new_path)}")

    try:
        shutil.copytree(old_path, new_path)
        print(f"✅ Copied & Renamed: {old_name} → {os.path.basename(new_path)}")
    except Exception as e:
        print(f"❌ Error copying {old_name}: {e}")
