contacts = {}


while True:
    ask = input("Would you like to access your contact list (y/n)?: ").lower().strip()
    if ask == "y":
        print("Okay!")
        see = input("Would you like to 1 = see contacts, 2 = add a contact, 3 = delete a contact?: ").strip()
        if see == "1":
            print(contacts)
        elif see == "2":
            name = input("Please enter the contact name: ").capitalize().strip()
            number = int(input("Please add a phone number: "))
            contacts[name] = number
        elif see == "3":
            delete = input("Enter the contact name you would like to delete?: ").strip().capitalize()
            if delete in contacts:
                del contacts[delete]
                print(contacts)
    else:
        print("Alright, maybe another time!")