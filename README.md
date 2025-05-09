---

# Digital Banking Management System

A simple Python-based banking system that allows users to create an account, deposit and withdraw money, check their balance, and view transaction history.

## Features

* **Create Account**: Create a new user account with a unique name.
* **Deposit Money**: Deposit money into the account.
* **Withdraw Money**: Withdraw money from the account.
* **Check Balance**: Check the current account balance.
* **Transaction History**: View all past deposits and withdrawals.

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* File Handling

## How to Run the Project

### Prerequisites

Make sure you have Python installed on your machine.

### Steps to Run:

1. **Clone the Repository**:

   Open the terminal/command prompt and run the following command:

   ```bash
   git clone https://github.com/your_username/Digital_Banking_Management_System.git
   ```

2. **Navigate to the Project Folder**:

   ```bash
   cd Digital_Banking_Management_System
   ```

3. **Run the Script**:

   Run the Python script using the following command:

   ```bash
   python main.py
   ```

   or

   ```bash
   python3 main.py
   ```

4. **Test the System**:

   The program will display the menu. Follow the prompts to test different features such as deposit, withdrawal, balance check, etc.

## Example Output:

Here's an example of how the program works when you run it:

```
Welcome to Digital Bank!
Enter your name: Mohana
Account created successfully for Mohana.

1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Exit
Enter your choice: 2
Enter deposit amount: 1000
New balance: 1000.0

1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Exit
Enter your choice: 3
Enter withdrawal amount: 500
New balance: 500.0

1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Exit
Enter your choice: 4
Current balance: 500.0

1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Exit
Enter your choice: 5
Transaction History:
Deposited: 1000
Withdrawn: 500

1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Exit
Enter your choice: 6
Thank you for using Digital Bank. Goodbye!
```

## What to Check

* **Deposit and Withdraw**: Make sure that balance is updating correctly.
* **Transaction History**: Verify that transactions are logged correctly.
* **Error Handling**: Enter invalid inputs (like letters instead of numbers) and check if the program handles them gracefully.

---
