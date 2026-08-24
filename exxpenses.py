""" expenses = [10.50 , 8 , 5 , 15 , 20 , 5 , 3]

sum = 0

for x in expenses:
    sum = sum + x

print(sum) """



def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense

    return total


def main():
    expenses = [10.50, 8, 5, 15, 20, 5, 3]

    total = calculate_total(expenses)

    print(total)


main()