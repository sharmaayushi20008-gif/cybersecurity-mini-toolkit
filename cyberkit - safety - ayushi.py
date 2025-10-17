# Cybersecurity Mini Toolkit v1.0
# Author: Ayushi
# Open-source: GitHub
# Purpose: Help students stay safe online with password checking, phishing detection, and text encryption

import re

# -------------------------------
# 1. Password Strength Checker
# -------------------------------
def check_password_strength(password):
    """
    Checks the strength of a password based on length, letters, numbers, and special characters.
    Prints the result as Weak, Medium, or Strong.
    """
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    if strength <= 2:
        print("Password Strength: Weak 🔴")
    elif strength <= 4:
        print("Password Strength: Medium 🟠")
    else:
        print("Password Strength: Strong 🟢")

# -------------------------------
# 2. Phishing Link Detector
# -------------------------------
def check_phishing(url):
    """
    Performs a simple check to detect suspicious keywords in a URL.
    Prints whether the URL is likely safe or suspicious.
    """
    suspicious_keywords = ["login", "verify", "update", "account", "secure"]
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        print("⚠️ Suspicious URL detected!")
    else:
        print("✅ URL seems safe (basic check)")

# -------------------------------
# 3. Text Encryption / Decryption
# -------------------------------
def encrypt_text(text, shift=3):
    """
    Encrypts text using a simple Caesar cipher with a shift (default=3).
    """
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt_text(text, shift=3):
    """
    Decrypts text encrypted with the Caesar cipher.
    """
    return encrypt_text(text, -shift)

# -------------------------------
# Main Menu
# -------------------------------
def main():
    print("🛡️ Welcome to the Cybersecurity Mini Toolkit")
    while True:
        print("\nSelect an option:")
        print("1. Check Password Strength")
        print("2. Check URL for Phishing")
        print("3. Encrypt Text")
        print("4. Decrypt Text")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            pwd = input("Enter password: ")
            check_password_strength(pwd)
        elif choice == "2":
            url = input("Enter URL: ")
            check_phishing(url)
        elif choice == "3":
            txt = input("Enter text to encrypt: ")
            print("Encrypted Text:", encrypt_text(txt))
        elif choice == "4":
            txt = input("Enter text to decrypt: ")
            print("Decrypted Text:", decrypt_text(txt))
        elif choice == "5":
            print("Goodbye! Stay safe online! 🛡️")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Run the program
if __name__ == "__main__":
    main()
