from files import get_delivery, get_delivery_id
import shutil
import os

# Prints all the orders not yet delivered
def print_delivery_orders():
    deliveries = get_delivery()
    for key in deliveries:
        if deliveries[key]['completed'] == "0":
            print(key, "is awaiting completion")

# Marks order as complete and adds tips 
def add_completion():
    did = input("Give order ID for delivery: ")
    delivery = get_delivery_id(did)
    if delivery is None:
        print("Order to deliver not found.")
    else:
        completed = input("Order delivered?: ")
        if completed == "Yes" or completed == "yes" or completed == "Y" or completed == "y":
            tip = input("How many tips?: ")
            # Creates temporary file to copy and paste the new details
            deliveries = get_delivery()
            temp_file = open("temp_delivery.csv", "w")
            temp_file.write("id,name,address,description,date,amount,completed,tips\n")
            for key in deliveries:
                if key == did:
                    deliveries[key]["completed"] = "1"
                    deliveries[key]["tips"] = tip
                temp_file.write(deliveries[key]["id"]+","+deliveries[key]["name"]+","+
                                deliveries[key]["address"]+","+deliveries[key]["description"]+","+
                                deliveries[key]["date"]+","+deliveries[key]["amount"]+","+
                                deliveries[key]["completed"]+","+deliveries[key]["tips"]+"\n")
            temp_file.close()
            shutil.copyfile("temp_delivery.csv", "deliveries.csv")
            os.remove("temp_delivery.csv")
            print("Order marked as delivered")
        else:
            print("Order not marked as delivered")