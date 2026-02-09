# Coffee Delivery Orders CLI

A command-line system to manage **phone delivery orders** for a coffee shop, with **role-based access** for Clerks, Delivery staff, and a Manager. :contentReference[oaicite:0]{index=0}

This project was originally developed as a university assignment and is published here as a **portfolio artifact** (clean logic, file I/O, reporting, and validation). :contentReference[oaicite:1]{index=1}

## Features

### Role-based login
- **Clerk:** create orders, check pending/incomplete orders :contentReference[oaicite:2]{index=2}  
- **Delivery:** mark orders as completed :contentReference[oaicite:3]{index=3}  
- **Manager:** view statistics + export reports :contentReference[oaicite:4]{index=4}  

### Order management
Each order stores:
- Customer name
- Customer address
- Description
- Date in **DDMMYY** format
- Total amount  
The system assigns an **auto-increment Order ID**. :contentReference[oaicite:5]{index=5}

### Bulk upload
- Import orders from preformatted **.txt or .csv** files. :contentReference[oaicite:6]{index=6}

### Statistics (Manager)
- Orders by customer
- Orders by day
- Total amount of delivered orders
- Total amount by customer
- Total amount by day :contentReference[oaicite:7]{index=7}

### CSV exports (Manager)
- Customer names
- Orders entered per user
- Full dataset export
- Total amount per day (one record per day) :contentReference[oaicite:8]{index=8}

## How to Run

> Adjust the entry file name if yours is not `main.py`.

```bash
python main.py
