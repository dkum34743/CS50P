def main():
    amount_due = 50
    while amount_due > 0:
        print("Amount Due: " + str(amount_due))
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            amount_due -= coin  # amount_due = amount_due - coin
    print("Change Owed: " + str(-amount_due))

main()
