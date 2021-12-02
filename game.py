import random
import time
import os
#import pyttsx3

def ChooseDifficulty():
    global endrange
    global rndans

    difficulty = int(input("請選擇難易度，1.簡單 2.普通 3.困難（輸入數字）"))
    if difficulty == 1:
        endrange = 50
    elif difficulty == 2:
        endrange = 200
    elif difficulty == 3:
        endrange = 500
    else:
        print("輸入的困難度錯誤，請重新輸入！！")
        ChooseDifficulty()
    rndans = random.randrange(1,endrange)
    print("遊戲將在1秒後開始...")
    time.sleep(1)
    os.system('cls')
    GameStart()

def GameStart():
    global gamepass
    global wrongans

    wrongans = 0
    gamepass = 0

    while gamepass == 0:
        ans = input(f"請猜一個數字(範圍:1~{endrange})")

        if ans == "密技":
            gamepass = 1
            break

        num = int(ans)

        if ans.lower() == "end":
            print("遊戲將於一秒後結束")
            time.sleep(1)
            break
        
        if num == rndans:
            gamepass = 1
        elif num > endrange or num < 1:
            wrongans+=1
            print(f"{num}已超出範圍，請重新輸入")
        elif num != rndans:
            if num > rndans:
                print("猜小一點")
            else:
                print("猜大一點")
            wrongans+=1

    if gamepass:
        print("恭喜您猜對囉，猜數高手就是你")
        #engine = pyttsx3.init()
        #engine.say(f"累計答錯題數：{wrongans}")
        #engine.runAndWait()
        print(f"累計答錯題數：{wrongans}")
        while True:
            re = input("是否重新開始遊戲（y/n）")
            if re.lower() == 'y':
                ChooseDifficulty()
                break
            elif re.lower() == 'n':
                input("輸入任意鍵結束遊戲")
                break

if __name__ == '__main__':
    ChooseDifficulty()