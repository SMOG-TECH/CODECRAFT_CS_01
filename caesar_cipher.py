# Caesar Cipher Encryption & Decryption Tool
# Author:Sanya
# Internship: CodeCraft Cybersecurity Internship

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Main Program
if __name__ == "__main__":
    print("\n=== Caesar Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter your message: ")
    shift_value = int(input("Enter shift value (1-25): "))

    if choice == 'E':
        encrypted = encrypt(message, shift_value)
        print(f"\nEncrypted Message: {encrypted}")
    elif choice == 'D':
        decrypted = decrypt(message, shift_value)
        print(f"\nDecrypted Message: {decrypted}")
    else:
        print("Invalid choice. Please select E or D.")
