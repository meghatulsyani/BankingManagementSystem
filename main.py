class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.account_no = acc_no
        self.transaction_history = []  # To store transaction history

    def debit(self, amt):
        if amt > self.balance:
            print("Insufficient balance.")
            return False
        self.balance -= amt
        self.transaction_history.append(f"Debited: RS. {amt}")
        print(f"RS. {amt} was debited")
        print("Current Balance:", self.final_bal())
        return True

    def credit(self, amt):
        self.balance += amt
        self.transaction_history.append(f"Credited: RS. {amt}")
        print(f"RS. {amt} was credited")
        print("Current Balance:", self.final_bal())

    def final_bal(self):
        return self.balance

    def view_account_details(self):
        print(f"\nAccount No: {self.account_no}")
        print(f"Current Balance: RS. {self.final_bal()}")
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def transfer(self, amt, target_account):
        if self.debit(amt):  # Try to debit first
            target_account.credit(amt)
            print(f"Transferred: RS. {amt} to Account No: {target_account.account_no}")


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_no = input("Enter Account Number: ")
        balance = float(input("Enter Initial Balance: "))
        if acc_no in self.accounts:
            print("Account with this number already exists.")
        else:
            new_account = Account(balance, acc_no)
            self.accounts[acc_no] = new_account
            print(f"Account {acc_no} created with initial balance RS. {balance}.")

    def view_account(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            self.accounts[acc_no].view_account_details()
        else:
            print("Account not found.")

    def deposit(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            amt = float(input("Enter amount to deposit: "))
            self.accounts[acc_no].credit(amt)
        else:
            print("Account not found.")

    def withdraw(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            amt = float(input("Enter amount to withdraw: "))
            self.accounts[acc_no].debit(amt)
        else:
            print("Account not found.")

    def transfer_money(self):
        source_acc_no = input("Enter Source Account Number: ")
        target_acc_no = input("Enter Target Account Number: ")
        if source_acc_no in self.accounts and target_acc_no in self.accounts:
            amt = float(input("Enter amount to transfer: "))
            self.accounts[source_acc_no].transfer(amt, self.accounts[target_acc_no])
        else:
            print("One or both accounts not found.")

    def run(self):
        while True:
            print("\nBanking Management System")
            print("1. Create Account")
            print("2. View Account Details")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Transfer Money")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.view_account()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                self.withdraw()
            elif choice == '5':
                self.transfer_money()
            elif choice == '6':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Running the Banking Management System
if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.run()
