# Dictionary mapping Morse code to digits (0-9)
MORSE_TO_DIGIT = {
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9'
}

# Convert Morse code to an octal string
def morse_to_octal(morse_code):
    octal_representation = []
    morse_words = morse_code.split(' ')  # Split Morse code by spaces
    for word in morse_words:
        if word in MORSE_TO_DIGIT:
            octal_representation.append(MORSE_TO_DIGIT[word])  # Convert Morse to digits
    return ''.join(octal_representation)

# Convert an octal string to bytes (fixed function)
def octal_to_bytes(octal_string):
    byte_data = []
    # Process every three octal digits as one byte
    for i in range(0, len(octal_string), 3):
        triplet = octal_string[i:i+3]
        if len(triplet) != 3:
            # Skip if the last group has fewer than three digits (padding issue)
            continue

        print(f"Octal {int(triplet)}")
        byte_data.append(int(triplet, 8))  # Convert octal to integer (byte)
    return byte_data

# Write byte data to a file
def write_bytes_to_file(file_path, byte_data):
    with open(file_path, 'wb') as f:
        f.write(bytearray(byte_data))  # Write as binary data

# Restore a file from Morse code
def restore_file_from_morse(morse_code, file_path):
    octal_string = morse_to_octal(morse_code)  # Convert Morse code to octal
    print(f"Converted octal data: {octal_string}")

    byte_data = octal_to_bytes(octal_string)  # Convert octal to byte data
    print(f"Converted byte data: {byte_data}")

    write_bytes_to_file(file_path, byte_data)  # Write bytes to file
    print(f"File successfully restored as {file_path}")

# Example usage: Read Morse code from a file and restore the original file
with open("file_in_morse.txt", "r") as f:
    morse_code = f.read()
    restore_file_from_morse(morse_code, "restored_file.txt")
