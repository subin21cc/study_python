# 숫자 맞추기 게임 2
'''
사용자가 1~max_num 중 숫자 하나를 랜덤으로 고름
(max_num은 사용자로부터 입력받음)
컴퓨터가 숫자 하나를 출력
출력한 숫자가 사용자가 고른 숫자 보다 높으면(낮으면) '맞춰야할 수보다 높습니다(낮습니다)'를 입력
컴퓨터가 숫자를 맞출 때끼지 반복
컴퓨터가 숫자를 맞추면 정지
'''

min_num = 0
max_num = 100

answer = input()

while True:
    middle = int((min_num+max_num)//2)
    print(middle)
    answer = input("값보다 up/down/answer?")
    if answer == "up":
        min_num = middle
    elif answer == "down":
        max_num = middle
    elif answer == "answer":
        print("맞았습니다.")
        break