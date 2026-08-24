from question import Question

question_prompts = ["what type is sylveon?\n a)normal\n b)fairy\n c)psychic\n\n",
                   "how many eeveelutions are there?\n a)3\n b)5\n c)7\n\n",
                   "what evolution stone is used on eevee to get glaceon?\n a)icestone\n b)frozenstone\n c)coldstone\n\n"
                   ]

questions = [
  Question(question_prompts[0] ,"b"),
  Question(question_prompts[1] ,"c"),
  Question(question_prompts[2] ,"a")
]

def run_test(questions):
    score = 0
    for q in questions:
        answer = input(q.prompt)
        if answer == q.answer:
            score +=1
    print(f"you've got {score}/{len(question_prompts)} correct!")

run_test(questions)

