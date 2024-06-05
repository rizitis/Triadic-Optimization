import os
import random
import shutil

# Define relative paths
data1_path = "data1"
data3_path = "data3"
merged_path = "merged"
test_path = 'test_data'
val_path = 'val_data'

# Create merged, test, and val folders if they don't exist
for folder in [merged_path, test_path, val_path]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Merge data1 and data3 folders into the merged folder
for folder in [data1_path, data3_path]:
    for file in os.listdir(folder):
        shutil.copy(os.path.join(folder, file), os.path.join(merged_path, file))

# Count number of .txt files in the merged folder
txt_files = [file for file in os.listdir(merged_path) if file.endswith('.txt')]
txt_count = len(txt_files)

# Randomly select one-fifth of .txt files for test and val folders
random.shuffle(txt_files)
num_files_to_move = txt_count // 5
test_files = txt_files[:num_files_to_move]
val_files = txt_files[num_files_to_move:num_files_to_move * 2]

# Move files to test folder
for file in test_files:
    src_path = os.path.join(merged_path, file)
    dst_path = os.path.join(test_path, file)
    shutil.move(src_path, dst_path)
    print(f"Moved {file} to 'test' folder.")

# Move files to val folder
for file in val_files:
    src_path = os.path.join(merged_path, file)
    dst_path = os.path.join(val_path, file)
    shutil.move(src_path, dst_path)
    print(f"Moved {file} to 'val' folder.")

