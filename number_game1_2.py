# 숫자 맞추기 게임

import random

MAX_RANDOM_NUM = 100


def print_hello():
    print('python NumberGame1')
    print('일정한 범위의 랜덤한 숫자를 맞추는 게임입니다. 시작합니다.\n')


def print_game_title(game_count):
    print('----------------')
    print('{}번째 게임을 시작합니다.'.format(game_count))


# game_run()
#   @return : 정답을 맞춘 횟수 (0: 포기)
def game_run():
    try_count = 0
    random_num = random.randint(1, MAX_RANDOM_NUM + 1)
    while True:
        try_count += 1
        s = '[{}] 1부터 {}사이의 정수를 입력하세요(게임종료는 -1): '.format(try_count, MAX_RANDOM_NUM)
        guess_num = int(input(s))
        if guess_num == -1:
            return 0
        elif guess_num < random_num:
            print('{}보다 큽니다'.format(guess_num))
        elif guess_num > random_num:
            print('{}보다 작습니다'.format(guess_num))
        else:
            print('축하합니다. {}번만에 맞췄습니다.'.format(try_count))
            return try_count


def print_bye(game_count, game_try_sum):
    print('=============')
    print('게임을 종료했습니다.')
    print('게임 횟수 : {}'.format(game_count))
    print('게임당 평균 시도 횟수 : {}'.format(game_try_sum / game_count))


if __name__ == '__main__':
    game_count = 0
    game_try_sum = 0
    print_hello()

    while True:
        game_count += 1
        print_game_title(game_count)
        game_try = game_run()
        if game_try == 0:
            game_count -= 1
            break
        game_try_sum += game_try

        game_continue = input('게임을 계속하시겠습니까? (Y/n) [Y]:')
        if game_continue == 'N' or game_continue == 'n':
            break

    print_bye(game_count, game_try_sum)
