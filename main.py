class BankAccount:
    def __init__(self, account_holder, password, initial_balance=0):
        self.account_holder = account_holder
        self.password = password
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        """Deposit money to the account"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            return f"New balance: {self.balance}"
        return "Deposit amount must be greater than 0."

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawn: {amount}")
                return f"New balance: {self.balance}"
            return "Insufficient funds!"
        return "Withdrawal amount must be greater than 0."

    def get_balance(self):
        """Get current balance"""
        return f"Current balance: {self.balance}"

    def get_transaction_history(self):
        """Get transaction history"""
        return "\n".join(self.transaction_history) if self.transaction_history else "No transactions yet."

    def authenticate(self, entered_password):
        """Authenticate user by password"""
        return self.password == entered_password


def main():
    print("Welcome to Digital Bank!")
    
    
    name = input("Enter your name: ")
    password = input("Set your password: ")
    account = BankAccount(name, password)

    
    authenticated = False
    while not authenticated:
        entered_password = input("Enter your password to access the account: ")
        if account.authenticate(entered_password):
            authenticated = True
            print(f"Account successfully authenticated for {account.account_holder}.")
        else:
            print("Invalid password! Please try again.")
    
    
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transaction History\n5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            try:
                amount = float(input("Enter deposit amount: "))
                print(account.deposit(amount))
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
        elif choice == 2:
            try:
                amount = float(input("Enter withdrawal amount: "))
                print(account.withdraw(amount))
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
        elif choice == 3:
            print(account.get_balance())
        elif choice == 4:
            print("Transaction History:")
            print(account.get_transaction_history())
        elif choice == 5:
            print("Thank you for using Digital Bank. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
