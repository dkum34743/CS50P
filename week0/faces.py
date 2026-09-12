emoji=input()

def convert(emoji):
    if ":)" in emoji:
        emoji=emoji.replace(":)", "🙂")
    if ":(" in emoji:
        emoji=emoji.replace(":(", "🙁")
    print(emoji)
convert(emoji)
