contacts = {}

while True:
    ask = input("Would you like to access your contact list (y/n)?: ").lower().strip()
    if ask == "y":
        print("Okay!")
        see = input("Would you like to 1 = see contacts, 2 = add a contact?: ").strip()
        if see == "1":
            print(contacts)
        elif see == "2":
            name = input("Please enter the contact name: ").capitalize().strip()
            number = int(input("Please add a phone number: "))
            email = input("Would you like to add a email address (y/n)?: ").lower().strip()
            if email == "y":
                add_email = input("Enter a email address: ").strip()
            else:
                print("Moving on!")
            contacts[name] = number, add_email
       # elif see == "3":
        #    delete = input("Enter the contact name you would like to delete?: ").strip().lower
        #    if delete == contacts[name]:
        #        del contacts[name]
         #       print(contacts)
    else:
        print("Alright, maybe another time!")