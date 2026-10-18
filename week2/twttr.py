def main():
    user_input = input(str("Input: "))
    for char in "aeiouAEIOU":
        user_input = user_input.replace(char, "")
    print(user_input)

main()
