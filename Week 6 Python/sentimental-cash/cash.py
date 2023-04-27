# TODO
from cs50 import get_float


def main():
    dollars = get_dollars()

    # Calculate the number of quarters to give the customer
    quarters = int(calculate_quarters(dollars))
    dollars = dollars - quarters * 25
    print(quarters)

    # Calculate the number of dimes to give the customer
    dimes = int(calculate_dimes(dollars))
    dollars = dollars - dimes * 10
    print(dimes)

    # Calculate the number of nickels to give the customer
    nickels = int(calculate_nickels(dollars))
    dollars = dollars - nickels * 5
    print(nickels)

    # Calculate the number of pennies to give the customer
    pennies = int(calculate_pennies(dollars))
    dollars = dollars - pennies * 1
    print(pennies)

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print(coins)


def get_dollars():
    while True:
        try:
            n = get_float("Change owed: ") * 100
            if n < 0:
                n = get_float("Change owed: ")
            else:
                return n
        except ValueError:
            pass


def calculate_quarters(dollars):
    q = 25
    return dollars / q


def calculate_dimes(dollars):
    d = 10
    return dollars / d


def calculate_nickels(dollars):
    n = 5
    return dollars / n


def calculate_pennies(dollars):
    p = 1
    return dollars / p


main()
