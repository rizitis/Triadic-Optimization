import random

def main():
    # Read lines from "lines.txt"
    with open("lines.txt", 'r') as file:
        lines = file.readlines()

    # Shuffle the lines randomly
    random.shuffle(lines)

    # Split into three random segments
    segment_size = len(lines) // 3
    segment1 = lines[:segment_size]
    segment2 = lines[segment_size:2*segment_size]
    segment3 = lines[2*segment_size:]

    # Randomly determine the order to write segments to files
    segments = [segment1, segment2, segment3]
    random.shuffle(segments)

    # Write segments to separate files
    write_segment_to_file(segments[0], "1.txt")
    write_segment_to_file(segments[1], "2.txt")
    write_segment_to_file(segments[2], "3.txt")

    print("Lines have been randomly shuffled and split into 3 files: 1.txt, 2.txt, 3.txt")

def write_segment_to_file(segment, filename):
    with open(filename, 'w') as file:
        file.writelines(segment)

if __name__ == "__main__":
    main()

