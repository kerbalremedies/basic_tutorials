def holy_grail():
    questions = ['name', 'quest', 'favourite colour']
    answers = ['Lancelot', 'The Holy Grail', 'Blue']

    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))

holy_grail()