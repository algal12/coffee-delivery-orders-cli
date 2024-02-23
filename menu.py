from files import get_usrs
from clerk import add_order, check_incomplete_orders
from delivery import print_delivery_orders, add_completion
from manager import spec_customer_orders, spec_day_orders, total_amount_orders, spec_customer_amount, spec_day_amount, customer_names, total_orders_user, all_data_ex, total_orders_day

# Login menu
def login():
    usrnm = input("Username: ")
    psswrd = input("Password: ")
    usrs = get_usrs()
    if usrnm in usrs:
        if psswrd == usrs[usrnm]["psswrd"] and usrs[usrnm]["active"] == '1':
            role = usrs[usrnm]["role"]
        else:
            role = None
            print("Wrong Password")
    else: 
        role = None
        print("This user does not exist")
    return usrnm, role

# Clerk menu
def clerk_menu(usrnm):
    print("<---- CLERK ---->")
    print("1. Add Order")
    print("2. Check for Incomplete Orders")
    print("0. Exit")
    choice = int(input("Choose: "))
    clerkname = usrnm
    return choice, clerkname

# Delivery menu
def delivery_menu():
    print("<---- DELIVERY ---->")
    print("1. View pending orders")
    print("2. Mark order as complete")
    print("0. Exit")
    choice = int(input("Choose: "))
    return choice

# Manager menu
def manager_menu():
    print("<---- MANAGER ---->")
    print("1. View number of orders from a customer")
    print("2. View number of order in a day")
    print("3. View total amount of orders delivered")
    print("4. View total amount of the orders from a customer")
    print("5. View total amount of the orders from a day")
    print("6. View all the names of the customers")
    print("7. View all the orders entered per user")
    print("8. View all data")
    print("9. View total amount of the orders per day")
    print("0. Exit")
    choice = int(input("Choose: "))
    return choice

# Role check and proceed
usrnm, role = login()
while True:
    if role == "clerk":
        choice, clerkname = clerk_menu(usrnm)
        if choice == 1:
            add_order(clerkname)
        elif choice == 2:
            check_incomplete_orders()
        elif choice == 0 :
            print("Signing out...")
            break
        else: 
            print("Wrong choice")
    elif role == "delivery":
        choice = delivery_menu()
        if choice == 1:
            print_delivery_orders()
        elif choice == 2:
            add_completion()
        elif choice == 0 :
            print("Signing out...")
            break
        else: 
            print("Wrong choice")
    elif role == "manager":
        choice = manager_menu()
        if choice == 1:
            spec_customer_orders()
        elif choice == 2:
            spec_day_orders()
        elif choice == 3:
            total_amount_orders()
        elif choice == 4:
            spec_customer_amount()
        elif choice == 5:
            spec_day_amount()
        elif choice == 6:
            customer_names()
        elif choice == 7:
            total_orders_user()
        elif choice == 8:
            all_data_ex()
        elif choice == 9:
            total_orders_day()
        elif choice == 0 :
            print("Signing out...")
            break
        else: 
            print("Wrong choice")
    else:
        break
print("End of Coffee Shop application")