""" while True:
    try:
        num = int (input ("Pick a number: "))
        if num == 0:
            print("Good bye!")
            exit()
        elif num < 0:
            print("Pick a positive number!")
        else:
            for i in range(1 , num+1):
                star = i * "*"
                print(star)
        exit()
    except ValueError as error:
        print("You have to pick a number") """


def get_number():
    while True:
        try:
            return int(input("Pick a number: "))
        except ValueError:
            print("You have to pick a number")


def print_stars(num):
    for i in range(1, num + 1):
        print(i * "*")


def main():
    while True:
        num = get_number()

        if num == 0:
            print("Goodbye!")
            break

        if num < 0:
            print("Pick a positive number!")
            continue

        print_stars(num)


main()