# 숫자 맞추기 게임 1
'''
컴퓨터가 1~max_num 중 숫자 하나를 랜덤으로 고름
(max_num은 사용자로부터 입력받음)
사용자가 숫자 하나를 입력
입력받은 숫자가 컴퓨터가 고른 숫자 보다 높으면(낮으면) '맞춰야할 수보다 높습니다(낮습니다)'를 출력
사용자가 숫자를 맞출 때끼지 반복
사용자가 숫자를 맞추면 정지
'''

import random

max_num = 100

answer = ''
count_list = []
sum_count = 0
game_count = 0

while answer != 'no':
    ran = random.randrange(1, max_num+1)
    guess = ''
    print('1 ~', max_num, '중의 숫자 하나를 맞춰보세요. (중간에 그만두고 싶다면 -1을 입력하세요.)')
    count = 0

    while True:
        guess = int(input('숫자를 입력하세요 : '))
        count += 1

        if guess == -1:
            break
        elif guess > ran:
            print(guess, '보다 작습니다.')
        elif guess < ran:
            print(guess, '보다 큽니다.')
        else:
            break

    if guess == -1:
        break
    else:
        print(count, '번만에 맞았습니다. 계속하시겠습니까? ')
        count_list.append(count)
        game_count += 1
        sum_count += count

    while True:
        answer = input('yes or no : ')

        if answer == 'yes' or 'no':
            break
        else:
            print('입력을 잘못하셨습니다.')

print(game_count, '번 플레이하셨습니다.')
print('평균', round(sum_count/len(count_list),2), '회로 맞았습니다.(소수점 두번째자리에서 반올림)')

