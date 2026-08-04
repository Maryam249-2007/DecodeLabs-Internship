message = input("Enter your message: ")
shift = 3
encrypted = ""

for letter in message:
    new_letter = ord(letter) + shift
    encrypted += chr(new_letter)

print("Encrypted Text:", encrypted)

decrypted = ""

for letter in encrypted:
    new_letter = ord(letter) - shift
    decrypted += chr(new_letter)

print("Decrypted Text:", decrypted)
