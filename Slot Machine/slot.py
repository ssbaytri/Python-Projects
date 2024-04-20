MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive number!")
        else:
            print("Please enter a number!")

    return amount


def get_lines_number():
    while True:
        lines = input("Enter a number of lines to bet on (1 - " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines!")
        else:
            print("Please enter a number!")

    return lines


def get_bet():
    while True:
        bet_amount = input("How much do you want to bet on each line? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"bet amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a number!")

    return bet_amount


def main():
    balance = deposit()
    lines = get_lines_number()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough to bet that amount, you current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")


if __name__ == '__main__':
    main()
