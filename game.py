#coding=utf-8
import random
import time
import os
import pyttsx3

rank1 = dict()
rank2 = dict()
rank3 = dict()

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
    global ndifficulty
    srange = 1

    difficulty = input("請選擇難易度，1.簡單 2.普通 3.困難（輸入數字）")
    if IsNumber(difficulty):
        ndifficulty = int(difficulty)
    else:
        ndifficulty = -1

    if ndifficulty == 1:
        erange = 50
    elif ndifficulty == 2:
        erange = 200
    elif ndifficulty == 3:
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
    global ndifficulty
    wrongans = 0
    gamepass = 0

    st = time.time()

    while gamepass == 0:
        ans = input(f"請猜一個數字(範圍:{srange}~{erange})")

        if ans == "密技":
            print(f"答案為{rndans}")
            continue

        if ans.lower() == "end":
            print("遊戲將於一秒後結束")
            time.sleep(1)
            break
        
        if not IsNumber(ans):
            continue
        
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
        et = time.time()
        print("恭喜您猜對囉，猜數高手就是你")
        print(f"累計答錯題數：{wrongans}")
        print("花費秒數：%.2f"%(round(et-st,2)))
        record = GameRank(ndifficulty,wrongans,round(et-st,2))
        print("\n-----BestRecord-----")
        print("難易度：%s"%(str(ndifficulty).replace('1','簡單').replace('2','普通').replace('3','困難')))
        print("累計答錯：%d"%record[0])
        print("花費秒數：%.2f\n"%record[1])
        
        engine = pyttsx3.init()
        engine.say("恭喜您猜對囉，猜數高手就是你")
        engine.runAndWait()
        engine.say(f"累計答錯題數：{wrongans}")
        engine.runAndWait()

        while True:
            re = input("是否重新開始遊戲？（y/n）")
            if re.lower() == 'y':
                print("正在重新載入遊戲...")
                time.sleep(1.5)
                os.system('cls')
                ChooseDifficulty()
                break
            elif re.lower() == 'n':
                input("輸入任意鍵結束遊戲")
                break

def GameRank(difficulty,nwrong,spend):
    global rank1
    global rank2
    global rank3

    r = ChooseRank(difficulty)
    try:
        ospend = r[nwrong]
    except KeyError:
        ospend = 0
    if ospend == 0 or spend < ospend:
        r[nwrong] = spend
    tmplist = list(r.keys())
    tmplist.sort()
    return tmplist[0],r[tmplist[0]]

def ChooseRank(difficulty):
    if difficulty == 1:
        return rank1
    elif difficulty == 2:
        return rank2
    elif difficulty == 3:
        return rank3

if __name__ == '__main__':
    ChooseDifficulty()
