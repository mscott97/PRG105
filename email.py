
import pickle


def main():
    # declare variables
    customers = get_info()
    choice = menu()
    if choice == "look":
        lookup(customers)
    elif choice == "add":
        add(customers)
    elif choice == "update":
        change(customers)
    elif choice == "remove":
        delete(customers)
    elif choice == "quit":
        save_file(customers)
    else:
        print("not valid entry")
        menu()


def get_info():
    # get file, unpickle, store in dictionary
    try:
        customer_file = open('customers.dat', 'rb')
        customers_dictionary = pickle.load(customer_file)
    except:
        customers_dictionary = {}
    return customers_dictionary


def menu():
    # display menu
    chosen = 0

    try:
        while chosen < 1 or chosen >2:
            print("----------- Customer Accounts --------------")
            print("1:   Add a new customer")
            print("2:   Quit")
            chosen = int(input("Please enter the number of your selection:"))
            if chosen < 1 or chosen > 2:
                print("Not a valid selection.")
            else:
                if chosen == 1:
                    return "add"
                elif chosen == 2:
                    return "quit"
    except ValueError:
        print("You need to have a numeric entry from the above list")
        menu()


def lookup(customers_lookup):
    # lookup and display a current customer
    print("lookup")


def add(customers_add):
    # add a new customer
    print("add")


def change(customers_change):
    # update customer information
    print("change")


def delete(customers_delete):
    # delete a customer
    print("delete")


def save_file(customers_pickle):
    # pickle and dump the file
    print("save")


main()


