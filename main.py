import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits
    password = ""
    for i in range(10):
        password += random.choice(chars)
    return password

print("1. Generate & Save Password")
print("2. Search Password")

choice = input("Choose option: ")

if choice == "1":
    website = input("Website: ")
    username = input("Username: ")
    password = generate_password()

    file = open("passwords.txt", "a")
    file.write(website + " | " + username + " | " + password + "\n")
    file.close()

    print("Saved Password:", password)

elif choice == "2":
    search = input("Enter website name: ")
    file = open("passwords.txt", "r")

    found = False
    for line in file:
        if search in line:
            print("Found:", line)
            found = True

    file.close()

    if not found:
        print("No password found")
