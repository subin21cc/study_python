# 숫자 야구 게임2
"""
1) 사용자가 세자리 수 하나를 정함(단, 세자리 수는 각 자리 숫자가 다르고 각 자리 수는0~9까지 가능)
2) 컴퓨터가 세자리 수 하나를 제시함
3) 사용자는 숫자의 자리와 위치가 모두 맞으면 'S', 위치만 맞으면 'B'
4) 하나도 맞지 않을 경우 'OUT'을 입력
"""

import random


def print_hello():
    print('숫자야구란 감춰진 3개의 숫자가 무엇인지 맞추는 게임입니다.')
    print('1) 사용자가 세자리 수 하나를 정합니다.(단, 세자리 수는 각 자리 숫자가 다르고 각 자리 수는 0~9까지 가능')
    print('2) 컴퓨터가 세자리 수 하나를 제시합니다.')
    print('3) 사용자는 숫자의 자리와 위치가 모두 맞으면 S, 위치만 맞으면 B을 입력합니다.')
    print('4) 숫자가 하나도 맞지 않을 경우 OUT을 입력합니다.\n')

    print('게임을 시작합니다.\n')


def is_valid_num_str(str):
    for i in range(3):
        for j in range(3):
            if i != j:
                if str[i] == str[j]:
                    return False
    return True


def get_random_num_str():
    while True:
        ret = make_number(random.randrange(12, 987 + 1))
        if is_valid_num_str(ret):
            return ret


def make_number(n):
    ret = '00' + str(n)
    return ret[-3:]


def init_list():
    global num_list
    for i in range(1000):
        if not is_valid_num_str(make_number(i)):
            num_list[i] = False


def check_list(s_count, b_count):
    global num_list

    for i in range(1000):
        if not num_list[i]:
            continue
        if get_ball_count(guess_num, num_list[i]) != (s_count, b_count):
            return False


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


num_list = [True] * 1000

if __name__ == '__main__':
    init_list()
    print_hello()
    while True:
        guess_num = get_random_num_str()
        print("추측하는 숫자 : {}".format(guess_num))
        s_count, b_count = map(int, input('볼카운트를 입력하세요(_S _B) : ').split())
        check_list(s_count, b_count)

        if s_count == 3:
            break
