import random
i=1#每局答题的次数
count=0#错误的局数
name=input('请输入您的姓名：')
print(f'''{name}你好，欢迎来到猜数字游戏''')
print('游戏规则如下：你可以在1~50之间选择一个数字，并且你有3次机会回答(为一局），不要输入不在范围内的数字哟，不然会浪费掉一次机会的呢，机会有限好好珍惜呀！连败三局将获得一次自我拯救机会，快来试试吧！')
number=random.randint(1,50)
#规则
while True:
    print(number)
    guess=int(input('输入你猜的数字吧'))
    if guess<1 or guess>50:
        print('你输入的数字不在范围内，浪费掉一次机会呦')
        print(f'''你还有{3-i}次机会''')
    elif guess<number and i!=3:
        print('你输入的偏小，再试试吧！')
        print(f'''你还有{3 - i}次机会''')
    elif guess>number and i!=3:
        print('你输入的偏大，再试试小一点的数吧！')
        print(f'''你还有{3 - i}次机会''')
    elif guess!=number and i>=3:
        print('真可惜，本轮机会已经用完了，下次再努力吧！')
        print(f'''正确答案是:{number}''')
        count=count+1#一局三次机会全错
        again = input('*****不甘心？是否再来一局y/n:')
        i=0
        if again!='y':
            break
    else :
        print(f'''恭喜你，用了{i}次机会猜对了，真不错！！！''')#答对一局
        again=input('*****是否再来一局y/n:')
        i=0
        count=0
        if again!='y':
            break
            #复活机会
    if count==3:
        print('你已经三局连败，若是想复活，回答对下列问题吧，请听题：')
        s=random.choice(['+','-','*'])
        a=random.randint(1,10)
        b=random.randint(1,10)
        d=input("{}{}{}=".format(a,s,b))
        answer=input('请输入你的答案：')
        if s=='+':
            if int(answer)!=int(a+b):
                print('真遗憾，你答错了，没有复活机会喽！')
                break#复活失败
            else:
                print("恭喜你答对了，你可以继续游戏了！")
                count = 0#复活成功
        elif s=='-':
            if int(answer)!=int(a-b):
                print('真遗憾，你答错了，没有复活机会喽！')
                break
            else:
                print("恭喜你答对了，你可以继续游戏了！")
                count = 0
        elif s == '*':
            if int(answer) != int(a * b):
                print('真遗憾，你答错了，没有复活机会喽！')
                break
            else :
              print("恭喜你答对了，你可以继续游戏了！")
              count=0
    i=i+1
