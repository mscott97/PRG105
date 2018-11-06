import pickle


def main():
    customers = get_info()
    choice = menu()
    if choice == "look":
        lookup(customers)
    elif choice == "add":
        add(customers)
    elif choice == "update":
        change(customers)
    elif choice == "quit":
        print("goodbye")
    else:
        print("Not Valid entry")
        menu()
    if choice != "quit":
        main()
