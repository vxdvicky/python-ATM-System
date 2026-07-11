class ATM:

    def __init__(self):
        self.__pin = 1234
        self.__balance = 2000
        self.__history = []

    # ---------------- LOGIN ---------------- #

    def login(self):

        attempts = 3

        while attempts > 0:

            pin = int(input("Enter Your PIN: "))

            if pin == self.__pin:
                print("\nLogin Successful")
                return True

            attempts -= 1

            if attempts > 0:
                print(f"Incorrect PIN. Attempts Left: {attempts}")

        print("\nYour Card Has Been Blocked.")
        return False

    # ---------------- CHECK BALANCE ---------------- #

    def check_balance(self):
        print(f"\nCurrent Balance : {self.__balance}")

    # ---------------- DEPOSIT ---------------- #

    def deposit(self):

        amount = float(input("Enter Amount To Deposit: "))

        if amount <= 0:
            print("Invalid Amount")
            return

        self.__balance += amount
        self.__history.append(f"Deposited {amount}")

        print("Money Deposited Successfully.")
        print(f"Updated Balance : {self.__balance}")

    # ---------------- WITHDRAW ---------------- #

    def withdraw(self):

        amount = float(input("Enter Amount To Withdraw: "))

        if amount <= 0:
            print("Invalid Amount")

        elif amount > self.__balance:
            print("Insufficient Balance")

        else:
            self.__balance -= amount
            self.__history.append(f"Withdraw {amount}")

            print("Money Withdrawn Successfully.")
            print(f"Remaining Balance : {self.__balance}")

    # ---------------- CHANGE PIN ---------------- #

    def change_pin(self):

        old_pin = int(input("Enter Current PIN: "))

        if old_pin == self.__pin:

            new_pin = int(input("Enter New PIN: "))
            confirm_pin = int(input("Confirm New PIN: "))

            if new_pin == confirm_pin:
                self.__pin = new_pin
                print("PIN Changed Successfully.")
            else:
                print("PIN Does Not Match.")

        else:
            print("Incorrect Current PIN.")

    # ---------------- TRANSACTION HISTORY ---------------- #

    def transaction_history(self):

        if len(self.__history) == 0:
            print("\nNo Transactions Found.")

        else:
            print("\nTransaction History")

            for i in self.__history:
                print(i)

    # ---------------- MENU ---------------- #

    def menu(self):

        while True:

            print("\n========== ATM MENU ==========")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            try:

                choice = int(input("Enter Your Choice: "))

                if choice == 1:
                    self.check_balance()

                elif choice == 2:
                    self.deposit()

                elif choice == 3:
                    self.withdraw()

                elif choice == 4:
                    self.change_pin()

                elif choice == 5:
                    self.transaction_history()

                elif choice == 6:
                    print("\nThank You For Using Our ATM.")
                    break

                else:
                    print("Invalid Choice.")

            except ValueError:
                print("Please Enter Numbers Only.")


# ---------------- MAIN ---------------- #

bank = ATM()

if bank.login():
    bank.menu()