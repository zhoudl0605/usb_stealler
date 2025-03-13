# Morse Code Dictionary for Encoding Digits (0-9)
MORSE_CODE_DICT = {
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}

# Convert a file to an octal representation


def file_to_octal(file_path):
    try:
        with open(file_path, 'rb') as file:
            byte_content = file.read()  # Read the file in binary mode
            # Convert each byte to a 3-digit octal
            octal_representation = [format(byte, '03o')
                                    for byte in byte_content]
            print(f"File converted to octal: {octal_representation}")
            return octal_representation
    except FileNotFoundError:
        return "File not found. Please check the path."

# Convert octal numbers to Morse code


def octal_to_morse(octal_representation):
    morse_code = []
    for octal in octal_representation:
        for digit in octal:  # Convert each digit of the octal value separately
            if digit in MORSE_CODE_DICT:
                morse_code.append(MORSE_CODE_DICT[digit])
    return ' '.join(morse_code)  # Separate Morse codes with spaces

# Save Morse code to a file


def save_morse_to_file(morse_code, output_file):
    try:
        with open(output_file, 'w') as file:
            file.write(morse_code)  # Write Morse code to the file
        print(f"Morse code saved to: {output_file}")
    except Exception as e:
        print(f"Failed to save file: {e}")


# Example Usage
file_path = 'example.txt'  # Input file path
octal_rep = file_to_octal(file_path)

if isinstance(octal_rep, list):  # Ensure the function returned valid data
    morse = octal_to_morse(octal_rep)  # Convert octal to Morse code
    save_morse_to_file(morse, 'file_in_morse.txt')  # Save Morse code to a file
else:
    print(octal_rep)  # Print error message if file was not found
