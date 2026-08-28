from datetime import date
import re
import sys

today = date.today()
name = input("Entr your name:\n")

menu = ['Add task', 'view task', 'compelete task', 'delete task', 'quit']
to_do_list = []
title = 'To do list'

print("hello " + name + ".")
print(f"today is: {today}")
print()
print("what would you like to do today?\n")
print()
while True:
    try:
        print(title.center(18, "="))

        for i, option in enumerate(menu, start=1):
            print(f"{i}. {option}")

        choice = int(input("pleasse enter a number from the menu:\n"))
        if choice in range(1, 6):
            if choice == 1:
                task = input("what would you like to add?\n")
                to_do_list.append(task + " ❌")
            elif choice == 2:
                if not to_do_list:
                    print("your to do list is empty!")
                else:
                    for j, view in enumerate(to_do_list, start=1):
                        print(f"{j}. {view}")
            elif choice == 3:
                tick = int(input("which task did you compelete?\n"))
                if "✅" in to_do_list[tick-1]:
                    print("you've already completed that task!")
                else:
                    resault = re.sub("❌", "✅", to_do_list[tick-1])
                    print(resault)
                    to_do_list[tick-1] = resault
            elif choice == 4:
                dele = int(input("which task would you like to delete?\n"))
                del to_do_list[dele-1]
            elif choice == 5:
                sys.exit(f"have a good day {name}!")
        else:
            print("please choose a number from the menu!")
    except ValueError:
        print("please choose a number from the menu!")
