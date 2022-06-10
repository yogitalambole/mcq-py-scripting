class question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

prompt = [
    "Convert the given fraction into mixed fraction 22/7.\n a)4 and 11/7\n b)3 and 1/7\n c)3 and 2/7\n d)4 and 1/7\n\n",
    "Write an equivalent fraction of 9/15.\n a)18/30\n b)15/30\n c)30/18\n d)15/18\n\n",
    "Find the value of 3(4/7)/7.\n a)30/50\n b)15/49\n c)30/49\n d)25/49\n\n"
]

questions = [
    question(prompt[0], 'b'),
    question(prompt[1], 'a'),
    question(prompt[2], 'd')
]

def run_mcq(questions):
    for question in questions:
        answer =  input(question.prompt)
        if answer==question.answer:
            print('----- correct -----\n\n')
        else:
            print('~~~~~~ wrong ~~~~~~\n\n')

run_mcq(questions)
