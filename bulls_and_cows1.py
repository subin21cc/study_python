# 숫자 야구 게임1
'''
숫자야구란 감춰진 3개의 숫자가 무엇인지 맞추는 게임입니다.
1) 3자리 숫자와 위치가 모두 맞아야 성공입니다.
2) 숫자는 0~9까지 구성되어 있으며, 각 숫자는 한번씩만 사용 가능합니다
3) 숫자와 자리의 위치가 맞으면 스트라이크(S), 숫자만 맞으면 볼(B) 입니다.
4) 숫자가 하나도 맞지 않을 경우 아웃(OUT) 으로 표시됩니다.

예시) 감춰진 숫자가 123 이라고 할 경우
- a. 102 = 1S 1B
- b. 124 = 2S
'''
import random


def print_hello():
    print('숫자야구란 감춰진 3개의 숫자가 무엇인지 맞추는 게임입니다.')
    print('1) 3자리 숫자와 위치가 모두 맞아야 성공입니다.')
    print('2) 숫자는0~9까지 구성되어 있으며, 각 숫자는 한번씩만 사용됩니다.')
    print('3) 숫자와 자리의 위치가 맞으면 스트라이크(S), 숫자만 맞으면 볼(B)입니다.')
    print('4) 숫자가 하나도 맞지 않을 경우 아웃(OUT)으로 표시됩니다.\n')

    print('게임을 시작합니다.\n')


def print_game_title(game_count):
    print('--------------------')
    print('{}번쩨 게임을 시작합니다.'.format(game_count))

def is_valid_num_str(str):
    for i in range(3):
        for j in range(3):
            if i != j:
                if str[i] == str[j]:
                    return False
    return True


def make_3_str(n):
    ret = '00' + str(n)
    return ret[-3:]


def get_random_num_str():
    # num = []
    # while len(num) != 3:
    #     ran = random.randrange(0, 9)
    #     if ran not in num:
    #         num.append(ran)
    while True:
        ret = make_3_str(random.randrange(12, 987+1))
        if is_valid_num_str(ret):
            return ret


def get_ball_count(n1, n2):
    strike = 0
    ball = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                if n1[i] == n2[j]:
                    strike += 1
            else:
                if n1[i] == n2[j]:
                    ball += 1

    return strike, ball


def run_bulls_and_cows():
    com_guess = get_random_num_str()
    guess_count = 0

    while True:
        guess = input('각 자리 숫자가 다른 세자리 수를 입력하세요. ')
        s, b = get_ball_count(com_guess, guess)
        guess_count += 1
        if s == 0 and b == 0:
            print('OUT')
        else:
            if s == 3:
                print('정답입니다.')
                print('{}번만에 맞췄습니다.'.format(guess_count))
                break
            print('{}S, {}B'.format(s, b))


def print_bye():
    print('게임을 종료했습니다.')


if __name__ == '__main__':
    game_count = 1
    game_try_sum = 0
    print_hello()
    run_bulls_and_cows()

    while True:
        game_count += 1

        game_continue = input('게임을 계속하시겠습니까? (Y/N) [Y]:')
        if game_continue == 'N' or game_continue == 'n':
            break
        print_game_title(game_count)
    print_bye()

