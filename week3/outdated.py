def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Date: ").strip()

        try:
            if "/" in date:
                parts = date.split("/")
                if len(parts) == 3:
                    month = int(parts[0])
                    day = int(parts[1])
                    year = int(parts[2])

                    if 1 <= month <= 12 and 1 <= day <= 31:
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break

            elif "," in date:
                parts = date.split(",")
                if len(parts) == 2:
                    month_day, year = parts
                    md_parts = month_day.strip().split()
                    if len(md_parts) == 2:
                        month_name, day = md_parts
                        if month_name in months:
                            month = months.index(month_name) + 1
                            day = int(day)
                            year = int(year.strip())

                            if 1 <= day <= 31:
                                print(f"{year:04d}-{month:02d}-{day:02d}")
                                break

        except (ValueError, IndexError):
            pass


main()
