from files import get_order, get_customer, get_delivery, get_usrs
import csv

# Total orders of a specific customer
def spec_customer_orders():
    name = input("Write the customer's name: ")
    orders = get_order()
    ttl = 0
    for key in orders:
        if orders[key]["name"] == name:
            ttl += 1
    if ttl == 0:
        print("Customer does not exit")
    elif ttl > 0:
        print(name, "has a total of", ttl, "orders")

# Total orders on a specific day
def spec_day_orders():
    date = input("Write the date(YYYY/MM/DD): ")
    if len(date) == 10 and date[4] == '/' and date[7] == '/':
        orders = get_order()
        ttl = 0
        for key in orders:
            if orders[key]["date"] == date:
                ttl += 1
        if ttl == 0:
            print("No orders on", date)
        if ttl == 1:
            print("There was 1 order on", date)
        elif ttl > 1:
            print("There were a total of", ttl, "orders on", date)
    else: 
        print("Invalid date format. Please enter the date in the format YYYY/MM/DD.")

# Total amount of orders
def total_amount_orders():
    deliveries = get_delivery()
    ttl_am = 0
    for key in deliveries:
        if deliveries[key]["completed"] == "1":
            ttl_am += float(deliveries[key]["amount"])
    print("There was a total amount of", ttl_am, "from the orders")

# Total amount of orders from a specific customer
def spec_customer_amount():
    name = input("Write the customer's name: ")
    orders = get_order()
    ttl_am = 0
    for key in orders:
        if orders[key]["name"] == name:
            ttl_am += float(orders[key]["amount"])
    if ttl_am > 0:
        print(name, "has a total amount of", ttl_am, "from all their orders")
    else:
        print("Customer does not exit")
    
# Total amount of orders on a specific day
def spec_day_amount():
    date = input("Write the date(YYYY/MM/DD): ")
    if len(date) == 10 and date[4] == '/' and date[7] == '/':
        orders = get_order()
        ttl_am = 0
        for key in orders:
            if orders[key]["date"] == date:
                ttl_am += float(orders[key]["amount"])
        if ttl_am == 0:
            print("No orders on", date)
        elif ttl_am > 1:
            print("There were a total amount of", ttl_am, "on the orders on", date)
    else: 
        print("Invalid date format. Please enter the date in the format YYYY/MM/DD.")

# All customer names in a csv file
def customer_names():
    customers = get_customer()
    file = open("customers.csv", "r")
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
    file.close()

# Counters with all the orders from the clerks in a csv file
def total_orders_user():
    file = open("clerks.csv", "r")
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
    file.close()

# All data (Orders, employees) in a new csv file 
def all_data_ex():
    orders = get_order()
    deliveries = get_delivery()
    employees = get_usrs()
    # Export data into CSV file
    all_data= []
    headers = ["id", "name", "address", "description", "date", "amount", "completed", "tips"]
    # Add orders
    for order_id, order_info in orders.items():
        row = [order_id, order_info["name"], order_info["address"],
               order_info["description"], order_info["date"],
               order_info["amount"], "-", "-"]
        if order_id in deliveries:
            row[6] = deliveries[order_id]["completed"]
            row[7] = deliveries[order_id]["tips"]
        all_data.append(row)
    # Add employees
    for employee_name, employee_info in employees.items():
        all_data.append([employee_name, employee_info["role"]])
    # Write evwerything to the csv
    file = open("all_data.csv", "w", newline='')
    writer = csv.writer(file)
    writer.writerows([headers] + all_data)
    file.close()
    # Print every row from CSV file
    file = open("all_data.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        print(row)
    file.close()

# Total amount of orders everyday in a csv file
def total_orders_day():
    orders = get_order()
    # Calculate total amount of the orders per day
    orders_per_day = {}
    for order_id, order_info in orders.items():
        date = order_info["date"]
        amount = float(order_info["amount"])
        orders_per_day[date] = orders_per_day.get(date, 0) + amount
    # Print every row from CSV file
    file_name = "total_orders_day.csv"
    file = open(file_name, "w", newline='')
    writer = csv.writer(file)
    writer.writerow(["Date", "Amount"])
    for date, total_amount in orders_per_day.items():
        writer.writerow([date, total_amount])
        print(date, total_amount)
