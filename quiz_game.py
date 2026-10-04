from quiz_question import Question
import sys

pokemon_question_prompts = [
    "how many eeveelutions are there?\n a)3\t b)5\n c)7\t d)10\n",
    "what was the first pokemon ever created?\n a)rhydon\t b)mew\n c)arceus\t d)bulbasaur\n",
    "how does growlith evolve into arcanine?\n a)leveling up\t b)firestone\n c)friendship\t d)trade\n"
]
vk_question_prompts = [
    "who is the smartest vaampire?\n a)kaname\t b)zero\n c)aidou\t d)yuuki",
    "who is the best looking vampire?\n a)zero\t\t b)akatsuki\n c)yuuki\t d)kaname\n",
    "who is the strongest vampire?\n a)zero\t b)rido\n c)isaya\t d)kaname\n"
]
horsy_question_prompts = [
    "how long do horses live?\n a)30 years\t b)50 years\n c)17 years\t d)100 years",
    "which of the following isn't a safe horse treat?\n a)apple\t b)avocado\n c)bannana\t d)carrot\n",
    "which one isnn't a registered dicipline in the olimpics?\n a)show jumping\t b)cutting\n c)dressage\t d)eventing\n"
]


def choose_category():
    questions = []
    while True:
        category = input(
            "\nwhich category would you like to choose today?\n\n 1)pokemon\t2)vampire knight\t3)equestrian\n\n").strip()

        if category == '1':
            questions = [
                Question(pokemon_question_prompts[0], "c"),
                Question(pokemon_question_prompts[1], "a"),
                Question(pokemon_question_prompts[2], "b")
            ]
            break
        elif category == '2':
            questions = [
                Question(vk_question_prompts[0], "a"),
                Question(vk_question_prompts[1], "d"),
                Question(vk_question_prompts[2], "d")
            ]
            break
        elif category == '3':
            questions = [
                Question(horsy_question_prompts[0], "a"),
                Question(horsy_question_prompts[1], "b"),
                Question(horsy_question_prompts[2], "b")
            ]
            break
        else:
            print("\nyou must chose 1,2 or 3!\n")
            continue
    return questions


def run_quiz(questions):
    score = 0
    count = 0
    for question in questions:
        while True:
            answer = input(question.prompt).strip().lower()
            if answer == question.answer:
                score += 1
                print("\n\ncorrect!\n\n")
                break
            elif answer not in ['a', 'b', 'c', 'd']:
                print("\n\nyou must choose a/b/c or d!\n\n")
                continue
            else:
                print("\n\nwrong answer!\n\n")
                break
        count += 1

    print(f"\n\nyou've got {score}/{count} questions right!\n\n")

    while True:
        do_continue = input(
            "\n\ndo you want to play again? yes or no!\n\n").strip().lower()
        if do_continue == 'yes':
            return run_quiz(choose_category())
        elif do_continue == 'no':
            sys.exit("have a nice day!")
        else:
            print("you must enter yes or no!")
            continue


run_quiz(choose_category())
