import csv
# Users/Employees file
def get_usrs():
    file = open("employees.csv")
    reader = csv.DictReader(file)
    usrs = {}
    for row in reader:
        usrs[row["usrnm"]] = row 
    return usrs 

# Orders file
def get_order():
    file = open("orders.csv")
    reader = csv.DictReader(file)
    orders = {}
    for row in reader:
        orders[row['id']] = row 
    return orders

# Deliveries file
def get_delivery():
    file = open("deliveries.csv")
    reader = csv.DictReader(file)
    deliveries = {}
    for row in reader:
        deliveries[row['id']] = row
    file.close()
    return deliveries

# Delivery ID file
def get_delivery_id(did):
    file = open("deliveries.csv")
    reader = csv.DictReader(file)
    for row in reader:
        if row['id'] == did:
            return row
    return None

# Customer names file
def get_customer():
    file = open("customers.csv")
    reader = csv.DictReader(file)
    customers = {}
    for row in reader:
        customers[row['name']] = row 
    return customers
