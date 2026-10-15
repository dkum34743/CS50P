def main():
    time_input = input("What time is it? (hr:min) ")
    hours = convert(time_input)
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")



def convert(time):
    hour, minutes = time.split(":")
    return float(hour) + float(minutes) / 60

if __name__ == "__main__":
    main()
