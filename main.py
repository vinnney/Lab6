#Vincent Lin

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")

def main():
    while True:
        menu()
        option = str(input("Please enter an option: "))
        if option == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        if option == "2":
            newpass = ""
            for element in password:
                if element == "0":
                    newpass += "3"
                elif element == "1":
                    newpass += "4"
                elif element == "2":
                    newpass += "5"
                elif element == "3":
                    newpass += "6"
                elif element == "4":
                    newpass += "7"
                elif element == "5":
                    newpass += "8"
                elif element == "6":
                    newpass += "9"
                elif element == "7":
                    newpass += "0"
                elif element == "8":
                    newpass += "1"
                elif element == "9":
                    newpass += "2"
            print(f"The encoded password is {newpass}, and the original password is {password}.")
        elif option == "3":
            exit()
if __name__ == "__main__":
    main()
