# 숫자 맞추기 게임 1
'''
컴퓨터가 1~n 중 숫자 하나를 랜덤으로 고름
(n은 사용자로부터 입력받음)
사용자가 숫자 하나를 입력
입력받은 숫자가 컴퓨터가 고른 숫자 보다 높으면(낮으면) '맞춰야할 수보다 높습니다(낮습니다)'를 출력
사용자가 숫자를 맞출 때끼지 반복
사용자가 숫자를 맞추면 정지
'''

import random
max_num = 100
ran = random.randrange(1, max_num+1)
guess = 0

while guess == ran:
    guess = int(input())
    if guess > ran:
        print('')



