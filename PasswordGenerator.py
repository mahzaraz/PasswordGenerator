import random
import string

length = int(input("\nEnter the length: "))


def generate():
    while True:
        try:
            print('''Choose character set for password from given below
                     1. Lower Letter
                     2. Upper Letter
                     3. Numbers
                     4. Symbols
                     5. Press 5 when your choices are done
                     6. Press CTRL+C to quit
                     ''')

            characterList = ""

            while True:
                choice = int(input("Write your choices "))
                try:
                    if choice == 1:
                        characterList += string.ascii_lowercase

                    elif choice == 2:
                        characterList += string.ascii_uppercase

                    elif choice == 3:
                        characterList += string.digits

                    elif choice == 4:
                        characterList += string.punctuation

                    elif choice == 5:
                        break

                except ValueError:
                    print("Please choose a valid option!")

            password = []

            for i in range(length):
                randomcharacters = random.choice(characterList)
                password.append(randomcharacters)

            print("\nYour password is:\n\n " + "".join(password) + "\n")
        except KeyboardInterrupt:
            break


generate()
