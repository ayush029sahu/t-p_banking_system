import random
import pandas as pd

# User class definition
class User:
    def _init_(self, name, dob, city, address, email, contact, password, balance):
        self.__name = name  # private
        self.__dob = dob  # private
        self.__city = city  # private
        self.__address = address  # private
        self.__email = email  # protected
        self.__contact = contact  # private
        self.__password = password  # private
        self.__balance = balance  # private
        self.__account_number = self.generate_account_number()  # private
        self.__active = True  # private

    def generate_account_number(self):
        # Generate account number as a string
        return str(random.randint(1000000000, 9999999999))

    def show_balance(self):
        print(f"Your balance: {self.__balance}")

    def change_password(self, new_password):
        self.__password = new_password
        print("Password updated successfully.")

    def deactivate_account(self):
        self.__active = False
        print("Account status updated to: Inactive")

    def activate_account(self):
        self.__active = True
        print("Account status updated to: Active")

    def get_account_number(self):
        return self.__account_number  # public getter for account_number

    def validate_password(self, password):
        return self.__password == password

    def _str_(self):
        return f"Name: {self._name}, Account Number: {self.account_number}, Balance: {self._balance}"

# Transaction class definition
class Transaction:
    def _init_(self, account_number, type, amount):
        self.__account_number = account_number  # private
        self.__type = type  # private
        self.__amount = amount  # private

    def process(self):
        # Logic to process the transaction
        return {"account_number": self._account_number, "type": self.type, "amount": self._amount}

# Bank system class definition
class BankSystem:
    def _init_(self):
        self.users = []  # public
        self.transactions = []  # public

    def add_user(self):
        name = input("Enter name: ")
        dob = input("Enter DOB (DD-MM-YYYY): ")
        city = input("Enter city: ")
        address = input("Enter address: ")
        email = input("Enter email: ")

        contact = input("Enter contact number: ")
        password = input("Create password: ")

        first_balance = float(input("Enter first deposit (minimum 2000): "))
        while first_balance < 2000:
            first_balance = float(input("Minimum balance is 2000. Enter again: "))

        user = User(name, dob, city, address, email, contact, password, first_balance)
        self.users.append(user)
        print(f"User created successfully. Account Number: {user.get_account_number()}")

    def show_users(self):
        if self.users:
            for user in self.users:
                print(user)  # Shows user info without password and other private details
        else:
            print("No users found.")

    def login(self):
        account_number = input("Enter account number: ")
        password = input("Enter password: ")
        
        # Find the user based on the account_number
        user = next((u for u in self.users if u.get_account_number() == account_number), None)

        if user and user.validate_password(password):
            print(f"Welcome, {user.get_account_number()}!")
            while True:
                print("\n1. Show Balance")
                print("2. Show Transactions")
                print("3. Credit Amount")
                print("4. Debit Amount")
                print("5. Transfer Amount")
                print("6. Activate/Deactivate Account")
                print("7. Change Password")
                print("8. Logout")

                choice = int(input("Choose an option: "))

                if choice == 1:
                    user.show_balance()
                elif choice == 2:
                    print("Transactions:")
                    user_transactions = [t for t in self.transactions if t["account_number"] == account_number]
                    if user_transactions:
                        for transaction in user_transactions:
                            print(transaction)
                    else:
                        print("No transactions found.")
                elif choice == 3:
                    amount = float(input("Enter amount to credit: "))
                    user_balance = user.User_balance + amount  # Accessing private variable using name mangling
                    user.User_balance = user_balance  # Updating balance
                    self.transactions.append(Transaction(account_number, "Credit", amount).process())
                    print(f"Amount credited. New Balance: {user_balance}")
                elif choice == 4:
                    amount = float(input("Enter amount to debit: "))
                    if user.User_balance >= amount:
                        user_balance = user.User_balance - amount
                        user.User_balance = user_balance
                        self.transactions.append(Transaction(account_number, "Debit", amount).process())
                        print(f"Amount debited. New Balance: {user_balance}")
                    else:
                        print("Insufficient balance.")
                elif choice == 5:
                    recipient_account = input("Enter recipient account number: ")
                    amount = float(input("Enter amount to transfer: "))
                    recipient = next((u for u in self.users if u.get_account_number() == recipient_account), None)

                    if recipient and user.User_balance >= amount:
                        user_balance = user.User_balance - amount
                        user.User_balance = user_balance
                        recipient_balance = recipient.User_balance + amount
                        recipient.User_balance = recipient_balance
                        self.transactions.append(Transaction(account_number, "Transfer Out", amount).process())
                        self.transactions.append(Transaction(recipient_account, "Transfer In", amount).process())
                        print(f"Amount transferred. New Balance: {user_balance}")
                    else:
                        print("Transfer failed.")
                elif choice == 6:
                    if user.User_active:
                        user.deactivate_account()
                    else:
                        user.activate_account()
                elif choice == 7:
                    new_password = input("Enter new password: ")
                    user.change_password(new_password)
                elif choice == 8:
                    print("Logged out")
                    break
                else:
                    print("Invalid option")
        else:
            print("Invalid account number or password.")

# Main code that runs the system
def main():
    system = BankSystem()
    while True:
        print("\n--- BANKING SYSTEM ---")
        print("1. Add User")
        print("2. Show Users")
        print("3. Login")
        print("4. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            system.add_user()
        elif choice == 2:
            system.show_users()
        elif choice == 3:
            system.login()
        elif choice == 4:
            print("Exiting")
            break
        else:
            print("Invalid choice")

if _name_ == "_main_":
    main()
