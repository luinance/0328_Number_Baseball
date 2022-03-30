# 2021189042 우준범 1차 과제
# 숫자 야구

import random

while True:
    first = random.randint(1, 9)
    second = random.randint(1, 9)
    while second == first:
        second = random.randint(1, 9)
    third = random.randint(1, 9)
    while third == first or third == second:
        third = random.randint(1, 9)

    # 숫자 입력받기
    player1 = player2 = player3 = strike = ball = 0
    while player1 != first or player2 != second or player3 != third:
        player1 = int(input('첫 번째 수를 입력하시오 : '))
        while not 1 <= player1 <= 9:
            player1 = int(input('첫 번째 수를 다시 입력하시오 : '))
        player2 = int(input('두 번째 수를 입력하시오 : '))
        while player2 == player1 or not 1 <= player2 <= 9:
            player2 = int(input('두 번째 수를 다시 입력하시오 : '))
        player3 = int(input('세 번째 수를 입력하시오 : '))
        while player3 == player1 or player3 == player2 or not 1 <= player3 <= 9:
            player3 = int(input('세 번째 수를 다시 입력하시오 : '))
        if player1 == first:
            strike += 1
        else:
            if player1 == second or player1 == third:
                ball += 1
        if player2 == second:
            strike += 1
        else:
            if player2 == first or player2 == third:
                ball += 1
        if player3 == third:
            strike += 1
        else:
            if player3 == first or player3 == second:
                ball += 1

        if strike == 0 and ball == 0:
            print("아웃~")
        else:
            if strike != 3:
                print(strike, " 스트라이크")
                print(ball, "볼")
                ball = 0
                strike = 0
            else:
                if strike == 3:
                    print("You Win!")
