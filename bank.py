class Bank:
    def __init__(self):
        self.cust_data = {
            '56789': [533, 'shanmuk', 0],
            '12345': [654, 'pooj', 15],
            '45000': [789, 'rahul', 123],
            '9876': [345, 'sneha', 150],
            '30000': [120, 'arjun', 50],
            '22222': [555, 'meera', 99]
        }
        self.current_customer = None  # To store the logged-in customer's data

    def data(self, card_number):
        return self.cust_data.get(card_number, None)

    def card_check(self, card_number):
        self.current_customer = self.data(card_number)
        if self.current_customer:
            cvv = int(input("Card found! Enter CVV: "))
            if self.current_customer[0] == cvv:
                print("CVV Verified!")
                self.services()  # Proceed to services
            else:
                print("Wrong CVV, access denied!")
        else:
            print("Card number not found!")

    def withdraw(self):
        if self.current_customer is None:
            print("No customer logged in!")
            return
        
        amount = int(input("Enter withdrawal amount: "))
        if self.current_customer[2] < amount:
            print("Insufficient balance!")
        else:
            self.current_customer[2] -= amount
            print(f"Withdrawal successful! Remaining balance: {self.current_customer[2]}")

    def deposit(self):
        if self.current_customer is None:
            print("No customer logged in!")
            return
        
        amount = int(input("Enter deposit amount: "))
        self.current_customer[2] += amount
        print(f"You have deposited {amount} successfully! New balance: {self.current_customer[2]}")

    def check_balance(self):
        if self.current_customer is None:
            print("No customer logged in!")
            return
        
        print(f"Your balance is: {self.current_customer[2]}")

    def services(self):
        print(f"welcome {self.current_customer[1]}")
        while True:
            print("\n1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit")
            choice = int(input("Choose an option: "))
            match choice:
                case 1:
                    self.withdraw()
                case 2:
                    self.deposit()
                case 3:
                    self.check_balance()
                case 4:
                    print("Thank you for banking with us!")
                    break
                case _:
                    print("Wrong input, try again!")

    def card_details(self):
        print("Welcome to ***** Bank")
        card_number = input("Enter your card number: ")
        self.card_check(card_number)


obj = Bank()
obj.card_details()
