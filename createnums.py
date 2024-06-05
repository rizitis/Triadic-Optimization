def create_numbers_file(filename, max_number):
    with open(filename, 'w') as file:
        for i in range(1, max_number + 1):
            file.write(str(i) + '\n')

# Ορίζουμε το όνομα του αρχείου και το μέγιστο αριθμό
filename = "numbers.txt"
max_number = 1000000000

# Δημιουργούμε το αρχείο με τους αριθμούς
create_numbers_file(filename, max_number)
print(f"Το αρχείο '{filename}' δημιουργήθηκε με επιτυχία.")
