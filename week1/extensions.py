def main():
    file_name = input("input file name: ").strip().lower
    if ".gif" in file_name:
        print("image/gif")
    elif ".jpg" in file_name or ".jpeg" in file_name:
        print("image/jpeg")
    elif ".png" in file_name:
        print("image/png")
    elif ".pdf" in file_name:
        print("document/pdf")
    elif ".txt" in file_name:
        print("document/txt")
    elif ".zip" in file_name:
        print("archive/zip")
    else:
        print("application/octet-stream")

main()
