# main.py
from auth import register, login
from will import Will

def main():
    print("=== Digital Will Creator ===")
    choice = input("1. Register\n2. Login\nChoice: ")

    username = input("Username: ")
    password = input("Password: ")

    if choice == "1":
        success, msg = register(username, password)
    else:
        success, msg = login(username, password)

    print(msg)
    if not success:
        return

    will = Will(username)

    while True:
        print("\n--- Will Menu ---")
        print("1. Add Asset")
        print("2. Export Will")
        print("3. Exit")
        opt = input("Choose: ")

        if opt == "1":
            name = input("Asset Name: ")
            category = input("Category (Digital/Property/Bank/etc): ")
            value = input("Value: ")
            beneficiary = input("Beneficiary: ")
            note = input("Notes: ")
            will.add_asset(name, category, value, beneficiary, note)
            print("Asset added.")
        elif opt == "2":
            file = will.export_to_file()
            print(f"Will exported to: {file}")
        elif opt == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
