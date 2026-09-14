def add_contact():
    name = input("please enter contact name:\n").lower().strip()
    while True:
        try:
            phone = int(input("enter phone number:\n"))
        except ValueError:
            print("\nyou have to enter a phone number!\n")
            continue
        else:
            break
    email = input("enter email address:\n").lower().strip()
    tag = input("enter relationship tag:\n").lower().strip()
    note = input("any notes?\n").lower().strip()
    contact = {'phone': phone, 'email': email, 'tag': tag, 'note': note}
    contacts[name] = contact.copy()
    if name == 'kaname':
        print('\n❤️')
    elif name == 'zero':
        print('\n🤮')
    if tag not in tags:
        tags.append(tag)


def view_contact():
    if contacts:
        for key, value in contacts.items():
            print(f"{key} : {value}")
    else:
        print("\ncontact list is empty!\n")


def search_contact():
    if contacts:
        namae = input("who are you looking for?\n").lower().strip()
        if namae in contacts:
            print(contacts[namae])
        else:
            print("\nthat contact doesn't exist!\n")
            return search_contact()
    else:
        print("\ncontact list is empty!\n")


def edit_contact():
    if contacts:
        who = input("which contact do you want to edit?\n").lower().strip()
        if who in contacts:
            edit = input("what do you want to edit?\n").lower().strip()
            if edit in labels:
                new = input("enter the new info:\n").lower().strip()
                if edit == 'name':
                    contacts[new] = contacts[who]
                    del contacts[who]
                elif edit == 'email':
                    contacts[who][edit] = new
                elif edit == 'tag':
                    contacts[who][edit] = new
                    if new not in tags:
                        tags.append(new)
                elif edit == 'note':
                    contacts[who][edit] = new
            elif edit == 'phone':
                while True:
                    try:
                        new = int(input("enter phone number:\n"))
                    except ValueError:
                        print("\nyou have to enter a phone number!\n")
                        continue
                    else:
                        break
                contacts[who][edit] = new
            else:
                print("\nthat label doesn't exist!\n")
        else:
            print("\nthat contact doesn't exist!\n")
            return edit_contact()
    else:
        print("\ncontact list is empty!\n")


def filter_contact():
    filt = input("what tag do you want to filter?\n").lower().strip()
    if filt in tags:
        for key1, value1 in contacts.items():
            if filt == value1['tag']:
                print(f"{key1} : {value1}")
    else:
        print("\nhey you don't have that tag!\n")
        return filter_contact()


def delete_contact():
    if contacts:
        bye = input("which contact do you want deleted?\n").lower().strip()
        if bye == 'zero':
            print('\ngood choice!\n')
        if bye in contacts.keys():
            del contacts[bye]
        else:
            print("that name doesn't exist it the contacts!\n")
            return delete_contact()
    else:
        print("\ncontact list is empty!\n")


labels = ['name', 'email', 'tag', 'note']
tags = []
contacts = {}
menu = ['add contact', 'view all contacts', 'search contacts',
        'edit contacts', 'filter contacts', 'delete contacts', 'quit']

while True:
    print()
    print('menu'.center(20, '+'))
    for i, list in enumerate(menu):
        print(f"{i+1}. {menu[i]}\n")
    task = input("\nwhat do you want to do?\n")

    if task == '1':
        add_contact()
    elif task == '2':
        view_contact()
    elif task == '3':
        search_contact()
    elif task == '4':
        edit_contact()
    elif task == '5':
        filter_contact()
    elif task == '6':
        delete_contact()
    elif task == '7':
        break
    else:
        print("\nyou have to choose from the menu!\n")
        continue
