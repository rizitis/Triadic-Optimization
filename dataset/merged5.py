import random

def main():
    # Read lines from "merged.txt" and count the total number of lines
    with open("merged.txt", 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)

    # Shuffle the lines randomly
    random.shuffle(lines)

    # Calculate sizes for val_data.txt and test_data.txt
    val_size = total_lines // 10
    test_size = total_lines - val_size

    # Ensure test_size is approximately 4/5 of total_lines
    # Calculate the difference
    test_size_diff = total_lines // 10 - val_size
    # Adjust test_size
    test_size = val_size + test_size_diff

    # Split into val_data and test_data
    val_data = lines[:val_size]
    test_data = lines[val_size:val_size + test_size]

    # Write segments to separate files
    write_segment_to_file(val_data, "val_data.txt")
    write_segment_to_file(test_data, "test_data.txt")

    print(f"Data has been split randomly into val_data.txt ({len(val_data)} lines) and test_data.txt ({len(test_data)} lines).")

def write_segment_to_file(segment, filename):
    with open(filename, 'w') as file:
        file.writelines(segment)

if __name__ == "__main__":
    main()

