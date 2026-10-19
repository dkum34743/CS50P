def main():
    camel = input("camelCase: ")
    snake = ""

    for char in camel:                  ## creates a variable char to use
        if char.isupper():
            snake += "_" + char.lower() ## += combines snake itself with "_" together
        else:
            snake += char

    print(snake)

    main()
