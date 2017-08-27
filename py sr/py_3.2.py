#py_3.2
grade=int(input("输入一个分数："))
if 90<=grade<=100:
    print("A")
elif 80<=grade:
    print("B")
elif 70<=grade:
    print("C")
elif 60<=grade:
    print("D")
elif 0<=grade:
    print("N")
else:
    print("error")
