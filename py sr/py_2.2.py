#py_2.2
import random
sec=random.randint(1,10)

temp=0
while temp!=sec:
    guess=input("输入一个数字:")
    temp=int(guess)
    if temp==sec:
        print("Right")
    else:
        if temp<sec:
            print("小了")
        else:
            print("大了")
