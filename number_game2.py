# 숫자 맞추기 게임 2
'''
사용자가 1~max_num 중 숫자 하나를 랜덤으로 고름
(max_num은 사용자로부터 입력받음)
컴퓨터가 숫자 하나를 출력
출력한 숫자가 사용자가 고른 숫자 보다 높으면(낮으면) '맞춰야할 수보다 높습니다(낮습니다)'를 입력
컴퓨터가 숫자를 맞출 때끼지 반복
컴퓨터가 숫자를 맞추면 정지
'''


def print_hello():
    min_num = 0
    max_num = 100
    print('숫자 하나를 생각한 뒤, 컴퓨터가 그 숫자를 맞추게 해보세요.(단,1~{}까지의 수)'.format(max_num))


def run_number_game():
    min_num = 1
    max_num = 100

    while True:
        middle = int((min_num + max_num) // 2)
        print(middle)
        answer = input("값보다 up/down/answer?")

        if answer == "up":
            min_num = middle + 1
        elif answer == "down":
            max_num = middle - 1
        elif answer == "answer":
            print("맞았습니다.")
            return 0


if __name__ == '__main__':
    print_hello()
    run_number_game()
