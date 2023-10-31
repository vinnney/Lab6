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
        elif option == "2":
            exit()
if __name__ == "__main__":
    main()
