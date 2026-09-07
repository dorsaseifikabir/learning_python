def add_expense():
    expense['category'] = input("what is the category?\n")
    expense['price'] = float(input("how much did you spend?\n"))
    expense['description'] = input("do you want to add a note?\n")
    expneses.append(expense.copy())
    if expense['category'] not in category:
        category.append(expense['category'])


def view_expenses():
    if not expneses:
        print("your expense list is empty!\n")
    else:
        for i, j in enumerate(expneses, start=1):
            print(f"{i}. {j}")


def view_total():
    total = 0
    for expense in expneses:
        total += expense['price']
    return total


def view_expenses_by_category():
    print(category)
    view = input("what category?\n")
    if view not in category:
        print("that category is not available!\n")
        return view_expenses_by_category()
    for i in expneses:
        if i['category'] == view:
            print(i)


def delete_expense():
    if not expneses:
        print("your expense list is empty!\n")
    else:
        choice = int(input("which expense do you want to delete?\n"))
        del expneses[choice-1]


expneses = []
expense = {}
category = []

print("hello! what would you like to do today?")

menu = {
    1: {'add expense': 'place holder'},
    2: {'view expenses': 'place holder'},
    3: {'view total': 'place holder'},
    4: {'view expenses by category': 'place holder'},
    5: {'delete expense': 'place holder'},
    6: {'quit': 'place holder'}
}


while True:
    for key1, value1 in menu.items():
        for key2 in value1:
            print(f"{key1}. {key2}")
    task = input("choose a number from the menu:\n")
    if task == '1':
        add_expense()
    elif task == '2':
        view_expenses()
    elif task == '3':
        print(f"the total money spen is: ${view_total()}")
    elif task == '4':
        view_expenses_by_category()
    elif task == '5':
        delete_expense()
    elif task == '6':
        break
    else:
        continue
