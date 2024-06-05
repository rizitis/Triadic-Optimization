import random

def calculate_mean(data):
    return sum(data) / len(data)

def main():
    # Διαβάζουμε τους αριθμούς από το αρχείο "numbers.txt"
    with open("numbers.txt", 'r') as file:
        data = [int(line.strip()) for line in file]

    # Τυχαία ανάκατεμένη λίστα με τους αριθμούς
    random.shuffle(data)

    # Υπολογισμός του συνολικού αριθμού δειγμάτων
    total_samples = len(data)

    # Υπολογισμός του μεγέθους κάθε τμήματος (33%)
    segment_size = total_samples // 3

    # Τυχαία επιλογή τμημάτων από τη λίστα των αριθμών
    first_segment = data[:segment_size]
    second_segment = data[segment_size:2 * segment_size]
    third_segment = data[2 * segment_size:]

    # Υπολογισμός του μέσου όρου για κάθε τμήμα
    first_segment_mean = calculate_mean(first_segment)
    second_segment_mean = calculate_mean(second_segment)
    third_segment_mean = calculate_mean(third_segment)

    print("Ο μέσος όρος του πρώτου τμήματος είναι:", first_segment_mean)
    print("Ο μέσος όρος του δεύτερου τμήματος είναι:", second_segment_mean)
    print("Ο μέσος όρος του τρίτου τμήματος είναι:", third_segment_mean)

if __name__ == "__main__":
    main()
