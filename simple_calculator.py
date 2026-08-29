while True:
    try:
        chosen_operator = input('input chosen operation:\n')

        if chosen_operator == 'q' or chosen_operator == 'quit':
            break

        numa = int(input('input first number:\n'))
        numb = int(input('input second number:\n'))

        operator = {
            '+': lambda: numa + numb,
            'plus': lambda: numa + numb,
            '-': lambda: numa - numb,
            'minus': lambda: numa - numb,
            '*': lambda: numa * numb,
            'x': lambda: numa * numb,
            'times': lambda: numa * numb,
            '/': lambda: numa / numb,
            'divided by': lambda: numa / numb,
            '//': lambda: numa // numb,
            'floor division': lambda: numa // numb,
            '%': lambda: numa % numb,
            'modulus': lambda: numa % numb,
            'power': lambda: numa ** numb,
            '**': lambda: numa ** numb,
            'pow': lambda: numa ** numb
        }

        if chosen_operator in operator:
            answer = operator[chosen_operator]()
            print(f" the answer is: {answer}")
        else:
            print("the operator you chose is not available")

    except ZeroDivisionError:
        print("you can't divide a number by zero! (zero sucks kaname rules)")
    except ValueError:
        print("you have to enter a number!")
