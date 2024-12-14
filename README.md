# **BANKING SYSTEM**

This Python project simulates a basic banking system, where users can perform banking operations like account creation, login, checking balances, transfers, withdrawals, and account deletion. I stored user data (e.g., usernames, passwords, balances) in a CSV file to act as a lightweight database. Below is a more detailed look into how the system works and some of the key parts of the code that make it function.

## **Key Code Sections:**

### **1. File Handling with CSV**  
In this project, I used Python’s built-in `csv` module to store and retrieve user information. Here’s how I implemented it to act as a simple database:
```python
# File Handling for Reading and Writing CSV (Lines 20-30)
def read_accounts():
    with open('accounts.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        return list(csv_reader)

def write_accounts(accounts):
    with open('accounts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(accounts)
