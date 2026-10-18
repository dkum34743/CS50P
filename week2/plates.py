def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ## Rule 1: Length must be 2-6
    if len(s) < 2 or len(s) > 6:
        return False

    ## Rule 2: Must start with at least 2 letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    ## Rule 3: Only letters and numbers (no punctuation/spaces)
    if not s.isalnum():
        return False

    ## Rule 4 & 5: Numbers must be at the end, and first number can't be '0'
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':          ## first digit can't be 0
                return False
            if not s[i:].isdigit():  ## everything after first digit must also be digits
                return False
            break

    return True


main()
