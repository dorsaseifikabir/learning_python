from passwordGenerator import PasswordGenerator

while True:
    while True:
        try:
            length = int(
                input("how many characters do you want your password to have?\n"))
        except ValueError:
            print("you must chose a number between 8 to 20!\n")
            continue
        if 1 <= length < 8:
            print(
                "\nyou might as well just choose Kaname for the world to access all of your accounts!\n")
        elif length > 20:
            print("\nyou'll never remember that many characters!\n")
        elif length <= 0:
            print("\nare you as dense as Zero kiriyu?\n")
        else:
            print(f"\n{length} sounds good!\n")
            break

    while True:
        uppercase = input(
            "do you want uppercase characters? y/n\n").lower().strip()
        if uppercase == 'y' or uppercase == 'yes':
            uppercase = True
            break
        elif uppercase == 'n' or uppercase == 'no':
            uppercase = False
            break
        else:
            print("\nit's a yes or no question!\n")

    while True:
        lowercase = input(
            "do you want lowercase characters? y/n\n").lower().strip()
        if lowercase == 'y' or lowercase == 'yes':
            lowercase = True
            break
        elif lowercase == 'n' or lowercase == 'no':
            lowercase = False
            break
        else:
            print("\nit's a yes or no question!\n")

    while True:
        numbers = input("do you want numbers?\n")
        if numbers == 'y' or numbers == 'yes':
            numbers = True
            break
        elif numbers == 'n' or numbers == 'no':
            numbers = False
            break
        else:
            print("\nit's a yes or no question!\n")

    while True:
        special_characters = input("do you want special_characters?\n")
        if special_characters == 'y' or special_characters == 'yes':
            special_characters = True
            break
        elif special_characters == 'n' or special_characters == 'no':
            special_characters = False
            break
        else:
            print("\nit's a yes or no question!\n")
    if uppercase == 0 and lowercase == 0 and numbers == 0 and special_characters == 0:
        print("\nyour password has to have something!\n")
        continue
    else:
        break

choice = PasswordGenerator(
    length, uppercase, lowercase, numbers, special_characters)
generated_password = choice.generate()
print(f"\nhere is your password: {generated_password}\n")
