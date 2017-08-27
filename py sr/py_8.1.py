#py_8.1
filename=input("请输入文件名：")
file=open("d:\\"+filename,'w')
print("请输入文件内容 -o退出：\n")
while True:
    text=input()
    if(text!='-o'):
        file.writelines(text)
    else:
        break
file.close()

