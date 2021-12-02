import random
import time
import os
#import pyttsx3

def IsNumber(s):
    try:
        if s=='NaN':
            return False
        float(s)
        return True
    except ValueError:
        return False

def ChooseDifficulty():
    global srange
    global erange
    global rndans

    srange = 1

    difficulty = input("請選擇難易度，1.簡單 2.普通 3.困難（輸入數字）")
    if IsNumber(difficulty):
        Ndifficulty = int(difficulty)
    else:
        Ndifficulty = -1
    if Ndifficulty == 1:
        erange = 50
    elif Ndifficulty == 2:
        erange = 200
    elif Ndifficulty == 3:
        erange = 500
    else:
        print("輸入的困難度錯誤，請重新輸入！！")
        ChooseDifficulty()
    rndans = random.randrange(srange,erange)
    print("遊戲將在1秒後開始...")
    time.sleep(1)
    os.system('cls')
    GameStart()

def GameStart():
    global srange
    global erange
    global rndans

    wrongans = 0
    gamepass = 0

    while gamepass == 0:
        ans = input(f"請猜一個數字(範圍:{srange}~{erange})")

        if ans == "密技":
            print(f"答案為{rndans}")
            continue

        if ans.lower() == "end":
            print("遊戲將於一秒後結束")
            time.sleep(1)
            break

        num = int(ans)
        
        if num == rndans:
            gamepass = 1
        elif num > erange or num < srange:
            wrongans+=1
            print(f"{num}已超出範圍，請重新輸入")
        elif num != rndans:
            if num > rndans:
                print("猜小一點")
                erange = num
            else:
                print("猜大一點")
                srange = num
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
                print("正在重新載入遊戲...")
                time.sleep(1.5)
                os.system('cls')
                ChooseDifficulty()
                break
            elif re.lower() == 'n':
                input("輸入任意鍵結束遊戲")
                break

if __name__ == '__main__':
    ChooseDifficulty()
