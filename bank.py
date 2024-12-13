from pyfiglet import Figlet
from tabulate import tabulate
import sys
import csv
import time

def main():
    print(title())
    print(menu())
    user=input("Input: ")
    while True:
        if "L" in user:
            x=login()
            print(x)
            if x=="Login successful":
                print(account_menu())
                account_input=input("Input: ")
                if account_input=="E":
                    sys.exit()
                elif account_input=="T":
                    print(transfer())
                elif account_input=="W":
                    print(withdraw())
            break
        elif "C" in user:
            print(create_account())
            break
        elif "E" in user:
            sys.exit()
        elif "D" in user:
            print(delete())
        else:
            print("Please Input Something Valid")
            user=input("Input: ")



def title():
    figlet=Figlet()
    font="big"
    figlet.setFont(font=font)
    rendered_title=figlet.renderText("WELCOME TO THE BANK")
    return rendered_title

def menu():
    data = {"OPTIONS": ["LOGIN", "CREATE ACCOUNT", "DELETE ACCOUNT", "EXIT"],
            "KEY": ["L", "C", "D", "E"]}
    return tabulate(data, headers="keys", tablefmt="double_grid")


def login():
    global username
    global password
    tries=3
    for i in range(tries):
        username = input("Username: ")
        password = input("Password: ")
        for _ in range(6):
            print(".", end="", flush=True)
            time.sleep(0.75)
        print()
        with open("account.csv", "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if row[0] == username and row[1] == password:
                    return "Login successful"
                else:
                    tries-=1
            print("Wrong username or password")
    return "Ran out of tries"


def account_menu():
    with open("account.csv", "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if row[0] == username and row[1] == password:
                    balance=row[2]
    data = {"OPTIONS": ["BALANCE","TRANSFER", "WITHDRAW", "EXIT"],
            "KEY": [balance,"T", "W", "E"]}
    return tabulate(data, headers="keys", tablefmt="double_grid")


def transfer():
    amount = int(input("How much money would you like to transfer? "))
    updated = False
    with open("account.csv", "r") as file:
        csvreader = csv.reader(file)
        rows = list(csvreader)
    for row in rows:
        if row[0] == username and row[1] == password:
            in_bank = int(row[2])
            total = in_bank + amount
            row[2] = str(total)
            updated = True
            break
    if updated:
        with open("account.csv", "w", newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(rows)
        return f"You now have ${total}"
    else:
        return "Account not found or incorrect login."


def withdraw():
    amount = int(input("How much money would you like to withdraw? "))
    updated = False
    with open("account.csv", "r") as file:
        csvreader = csv.reader(file)
        rows = list(csvreader)
    for row in rows:
        if row[0] == username and row[1] == password:
            in_bank = int(row[2])
            total = in_bank - amount
            if total<0:
                return "Not enough funds in account"
            else:
                row[2] = str(total)
                updated = True
                break
    if updated:
        with open("account.csv", "w", newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(rows)
        return f"You now have ${total}"


def create_account():
    c_username = input("Username: ")
    c_password = input("Password: ")
    balance = input("How much money would you like to deposit for it (if none type 0)? ")
    for _ in range(6):
            print(".", end="", flush=True)
            time.sleep(0.75)
    print()
    try:
        balance = int(balance)
    except ValueError:
        return "Invalid balance input. Please enter a valid number."
    with open("account.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password", "balance"])
        writer.writerow({"username": c_username, "password": c_password, "balance": balance})
    return "Account successfully created. Please login."

def delete():
    d_confirmation = input("Are you sure you want to delete your account with us? ").lower()
    updated_rows = []
    attempts = 3
    while attempts > 0:
        if d_confirmation == "yes":
            print("Please enter your username and password below:")
            d_username = input("Username: ")
            d_password = input("Password: ")
            print("Wait as we check for your login in our database")
            for _ in range(6):
                print(".", end="", flush=True)
                time.sleep(0.75)
            print()
            break
        elif d_confirmation == "no":
            return sys.exit("Okay, exiting program")
        else:
            print("Invalid Input")
            attempts -= 1
            if attempts == 0:
                return sys.exit("Too many invalid attempts. Exiting program.")
            else:
                d_confirmation = input("Are you sure you want to delete your account with us? ").lower()
    with open("account.csv", "r") as file:
        rows = csv.reader(file)
        account_found = False
        for row in rows:
            if d_username == row[0] and d_password == row[1]:
                account_found = True
                print("We have found your account in our database")
                final_confirmation = input("As further confirmation, please say yes again to deleting your account: ").lower()
                if final_confirmation == "yes":
                    print("Deleting your account...")
                    continue
                else:
                    return sys.exit("Okay, exiting program")
            updated_rows.append(row)
    if account_found:
        with open("account.csv", "w", newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(updated_rows)
        print("Your account has been successfully deleted.")
        sys.exit("Thank you for using our services")
    else:
        print("Account not found or incorrect credentials.")
        sys.exit("Exiting program.")
if __name__ == "__main__":
    main()
