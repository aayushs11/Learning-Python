# Caesar Cipher Encryption
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97  # ASCII for 'A' (65) and 'a' (97)
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged
    return encrypted_text

# Caesar Cipher Decryption
def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97  # ASCII for 'A' (65) and 'a' (97)
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Non-alphabet characters remain unchanged
    return decrypted_text

# Example usage
if __name__ == "__main__":
    # Ask the user if they want to encrypt or decrypt
    operation = input("Do you want to encrypt or decrypt? (Enter 'e' for encrypt or 'd' for decrypt): ").strip().lower()

    # Ask for the text and shift value
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (integer): "))

    # Perform the operation
    if operation == 'e':
        result = caesar_encrypt(text, shift)
        print(f"Encrypted Text: {result}")
    elif operation == 'd':
        result = caesar_decrypt(text, shift)
        print(f"Decrypted Text: {result}")
    else:
        print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")
