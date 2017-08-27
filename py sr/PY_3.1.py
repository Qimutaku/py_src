#py_3.1
grade=input("请输入一个分数:")
temp=int(grade)

while temp>0:
    if temp>90:
        print("A")
    else:
        if temp>80:
            print("B")
        else :
            if temp>70:
                print("C")
            else:
                print("D")
    grade=input("请输入一个分数:")
    temp=int(grade)
