import random

counter = 0


def game_start():
    while True:
        range_num = input('Добро пожаловать в числовую угадайку!\n\
Укажите число-границу случайного выбора: ')
        print()
        if range_num.isdigit() and int(range_num) > 1:
            hidden_num = random.randrange(1, int(range_num))
            return int(range_num), hidden_num
        else:
            print('Пожалуйста, введите целое число.')
            print()
            continue


def is_valid(num: str, range_num):
    if num.isdigit() and 1 <= int(num) <= range_num:
        return True
    else:
        False


range_num, hidden_num = game_start()

while True:
    guess = input(f'Попробуйте угадать число от 1 до {range_num}: ')
    print()

    if is_valid(guess, range_num):
        counter += 1
        guess = int(guess)

        if guess > hidden_num:
            print('Слишком много, попробуйте еще раз.', end='\n')
            continue
        elif guess < hidden_num:
            print('Слишком мало, попробуйте еще раз.', end='\n')
            continue
        else:
            print(f'Вы угадали за {counter} попыток, поздравляем!')
            again = input('Если хотите сыграть заново, напишите \'1\'. \
Если хотите закончить игру, напишите \'2\': ')
            print()

            if again == '1':
                counter = 0
                range_num, hidden_num = game_start()
                continue
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break
    
    else:
        print('А может все же введете целое число?', end='\n')
        continue