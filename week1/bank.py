def main():
    greeting = input("Greeting: ").lower().strip()
    match greeting:
        case _ if "hello" in greeting:
            print("$0")
        case _ if "h" in greeting:
            print("$20")
        case _ :                 #the "_" means 'everything else not previously mentioned'
            print("$100")
main()
