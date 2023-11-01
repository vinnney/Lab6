#Vincent Lin
new_password = ""
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
def encode():
    global new_password  # made global for later use when decoding
    password = input("Please enter your password to encode: ")
    for i in password:
        if i == "0":  # the if else statements check for each possible number 0-9
            new_password += "3"
        elif i == "1":
            new_password += "4"
        elif i == "2":
            new_password += "5"
        elif i == "3":
            new_password += "6"
        elif i == "4":
            new_password += "7"
        elif i == "5":
            new_password += "8"
        elif i == "6":
            new_password += "9"  # each number is added by 3
        elif i == "7":
            new_password += "0"
        elif i == "8":
            new_password += "1"
        elif i == "9":
            new_password += "2"
    return print("Your password has been encoded and stored!")
def main():
    while True:
        menu()
        option = str(input("Please enter an option: "))
        if option == "1":
            encode()
        if option == "2":
            exit() #later fix
        elif option == "3":
            exit()
if __name__ == "__main__":
    main()
