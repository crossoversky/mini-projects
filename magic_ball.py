import random


def choice(answers : list):
    random_answer = random.choice(answers)
    return random_answer


answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Знаки говорят: да',
           'Можешь быть в этом уверен', 'Мне кажется, да', 'Вероятнее всего', 'Хорошие перспективы',
           'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Даже не думай',
           'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Мой ответ — нет', 'Весьма сомнительно',
           'По моим данным, нет', 'Перспективы не очень хорошие']


print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.', end='\n')

name = input('Введите Ваше имя: ')
print(f'Здорово! Приятно познакомиться, {name}!')


while True:
    print(f'Задайте Ваш вопрос, {name}!')
    question = input()
    answer = choice(answers)
    print(answer, end='\n')

    print('Если хотите задать еще один вопрос, напишите \'1\'. Иначе — \'0\'.')
    user_choice = input()
    if user_choice == '1':
        continue
    else:
        print('Возвращайтесь при возникновении вопросов!')
        break