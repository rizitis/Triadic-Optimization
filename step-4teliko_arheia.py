import os
import random
import shutil

def main():
    # Φάκελος με τα δεδομένα
    data_folder = 'all_data/'

    # Ανάγνωση των ονομάτων των αρχείων από τον φάκελο
    files = os.listdir(data_folder)

    # Τυχαία ανάκατεμα των αρχείων
    random.shuffle(files)

    # Υπολογισμός του συνολικού αριθμού αρχείων
    total_files = len(files)

    # Υπολογισμός του μεγέθους κάθε τμήματος (33%)
    segment_size = total_files // 3

    # Δημιουργία φακέλων για τα τμήματα
    folders = ['data1', 'data2', 'data3']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Διαχωρισμός των αρχείων και μεταφορά στους αντίστοιχους φακέλους
    for i, folder in enumerate(folders):
        start_index = i * segment_size
        end_index = (i + 1) * segment_size if i < 2 else total_files  # Ensure all files are included
        for file in files[start_index:end_index]:
            shutil.move(os.path.join(data_folder, file), os.path.join(folder, file))

if __name__ == "__main__":
    main()
