# The info that a clerk will enter to the system

from files import get_order, get_delivery, get_customer
import csv
import shutil
import os

# Clerks adds order infromation
def add_order(clerkname):
    name = input("Customers's Name: ")
    address = input("Customer's Address: ")
    description = input("Order Description: (Use space between different items) ")
    date = input("Order's Date (YYYY/MM/DD): ")
    amount = input("Order Amount: ")
    completed = "0"
    tips = "-"
    orders = get_order()
    deliveries = get_delivery()
    customers = get_customer()
    new_id = len(orders) + 1
    # Write the order on the orders.csv for the clerks 
    file = open("orders.csv", "a")
    file.write(str(new_id)+","+name+","+address+","+description+","+date+","+amount+"\n")
    file.close()
    # Write the order on the delvieries.csv for the delivery to see and to check for icomplete orders
    file = open("deliveries.csv", "a")
    file.write(str(new_id)+","+name+","+address+","+description+","+date+","+amount+","+completed+","+tips+"\n")
    file.close()
    # Write the customer name in a new csv for the manager to check
    file = open("customers.csv", "a")
    file.write(str(name)+"\n")
    file.close()
    # Update clerks order count
    clerks_orders = []
    file = open("clerks.csv", "r", newline='')
    clerks_orders = list(csv.DictReader(file))
    for clerk in clerks_orders:
        if clerk["name"] == clerkname:
            clerk["orders"] = str(int(clerk["orders"]) + 1)
            break
    else:
        clerks_orders.append({"name": clerkname, "orders": "1"})
    file.close()
    file = open("clerks.csv", "w", newline='')
    rows = ["name", "orders"]
    file_writer = csv.DictWriter(file, fieldnames=rows)
    file_writer.writeheader()
    file_writer.writerows(clerks_orders)
    file.close()

# Clerk checks for incomplete orders
def check_incomplete_orders():
    deliveries = get_delivery()
    for key in deliveries:
        if deliveries[key]["completed"] == "0":
            print("Order with the id",key, "hasn't yet been delivered")


