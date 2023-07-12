while True:
        clear_output()
        name = input("Enter the person's name (or 'quit' to exit): ")
        if name.lower() == 'quit':
            print("Printing all names and addresses:")
            for person, address in address_book.items():
                print(f"Name: {person}\tAddress: {address}")
            break


