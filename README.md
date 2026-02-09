# Coffee Delivery Orders CLI (Python)

A command-line system for managing coffee shop **phone delivery orders**, with role-based access for:
- **Clerk** (create orders, view pending)
- **Delivery** (complete deliveries)
- **Manager** (statistics + CSV reports)

This project was originally developed as a university assignment and is published as a portfolio artifact (clean logic, file I/O, reporting, and menu-driven flow).

> ⚠️ Please do not reuse this repository for academic submissions.

---

## Features

### Authentication + Roles
Login using employee credentials stored in CSV files, then access the correct menu based on role.

### Order Management (Clerk)
Create delivery orders with:
- Customer name / address
- Description
- Date (DDMMYY format)
- Total amount
- Auto-generated Order ID

### Delivery Completion (Delivery)
Mark orders as delivered/completed and update stored data.

### Statistics + Reports (Manager)
Generate summaries and export CSV reports (daily totals, full dataset exports, etc.).

---

## Project Files (Current Structure)

Python modules:
- `assessment_01.py` — main entry point
- `menu.py` — menus / navigation
- `clerk.py` — clerk operations
- `delivery.py` — delivery operations
- `manager.py` — manager operations
- `files.py` — CSV/file handling helpers

Data / exports (CSV):
- `employees.csv` — employee login + role info
- `clerks.csv` — clerk-related records (if used)
- `customers.csv` — customers list/data
- `orders.csv` — active orders
- `deliveries.csv` — completed deliveries
- `all_data.csv` — aggregated dataset (if generated)
- `total_orders_day.csv` — totals per day (if generated)

---

## How to Run

### Requirements
- Python 3.10+ recommended (works on most Python 3 versions)

### Run
```bash
python assessment_01.py

