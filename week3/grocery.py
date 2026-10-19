def main():
    groceries = {}

    while True:
        try:
            item = input().strip().upper()
            if not item:
                continue
            groceries[item] = groceries.get(item, 0) + 1
        except EOFError:
            for item in sorted(groceries.keys()):
                print(f"{groceries[item]} {item}")
            break

main()
