import torch

# Read the text file
with open('lines.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Create a set of unique characters and sort them
chars = sorted(set(text))
print(chars)

# Write the vocabulary to a text file
with open('vocab.txt', 'w', encoding='utf-8') as f:
    for char in chars:
        f.write(char + '\n')

# Create dictionaries for encoding and decoding
string_to_int = {ch: i for i, ch in enumerate(chars)}
int_to_string = {i: ch for i, ch in enumerate(chars)}

# Function to encode text to integers
encode = lambda s: [string_to_int.get(c, 0) for c in s]  # Use 0 if character not found

# Function to decode integers back to text
decode = lambda l: ''.join(int_to_string[i] for i in l)

# Create a PyTorch tensor from the encoded text
data = torch.tensor(encode(text), dtype=torch.long)
print(data[:1000])  # Print first 1000 elements of the tensor

# Example: Convert back to text
decoded_text = decode(data.tolist())
print(decoded_text[:1000])  # Print the first 1000 characters of the decoded text

