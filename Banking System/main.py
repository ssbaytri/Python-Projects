# Banking System Program

def show_balance(balance):
    print("***************************")
    print(f"Your balance is ${balance:.2f}")
    print("***************************")


def deposit():
    print("***************************")
    amount = float(input("Enter an amount to be deposited: "))
    print("***************************")
    if amount < 0:
        print("***************************")
        print("Invalid amount to deposit!")
        print("***************************")
        return 0
    else:
        return amount


def withdraw(balance):
    print("***************************")
    amount = float(input("Enter the amount to be withdrawn: "))
    print("***************************")
    if amount > balance:
        print("***************************")
        print("Insufficient funds!")
        print("***************************")
        return 0
    elif amount < 0:
        print("***************************")
        print("Amount must be greater than 0")
        print("***************************")
        return 0
    else:
        return amount


def main():
    balance = 0
    running = True

    while running:
        print("****************************")
        print("****** Banking System ******")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1 -> 4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            running = False
        else:
            print("*********************")
            print("Invalid Choice!")
            print("*********************")

    print("*************************")
    print("Have a nice day!")
    print("*************************")


if __name__ == "__main__":
    main()
