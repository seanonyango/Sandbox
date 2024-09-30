
minimum_password_length = int(input('Enter minimum password length: '))
password = input("Enter your password: ")
while len(password) < minimum_password_length:
    print('Password must be at least ', minimum_password_length, "characters")
    password = input("Enter your password: ")
print("*" * len(password))
