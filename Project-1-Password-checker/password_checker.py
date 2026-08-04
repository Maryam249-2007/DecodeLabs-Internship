password = input("Enter your password: ")

length = len(password)

has_upper = False
has_number = False
has_symbol = False

for char in password:
    if char.isupper():
        has_upper = True

    if char.isdigit():
        has_number = True

    if not char.isalnum():
        has_symbol = True

if length >= 8 and has_upper and has_number and has_symbol:
    print("Strong Password")

elif length >= 6 and (has_upper or has_number):
    print("Medium Password")

else:
    print("Weak Password")