#图像字符串转化
from PIL import Image
import argparse

ascii_char=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
parse=argparse.ArgumentParser()
parse.add_argument ('file')#输入文件
parse.add_argument('-o','--output')#输出文件
parse.add_argument('--width',type=int,default=80)
parse.add_argument('--height',type=int,default=80)
#宽高可选参数
args=parse.parse_args()
#解析字符串为对象内容
IMG=args.file
OUTPUT=args.output
WIDTH=args.width
HEIGHT=args.height
#变量设置
def get_char(r,g,b,alpha=256):#未给出alpha时默认为256
    '''转化像素为字符串'''
    if alpha==0:
        return ' '
    length=len(ascii_char)
    gray=int(0.2126*r+0.7152*g+0.0722*b)
    unit=(256.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__=='__main__':
    im=Image.open(IMG)
    im=im.resize((WIDTH,HEIGHT),Image.LANCZOS)

    txt=''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt+=get_char(*im.getpixel((j,i)))
        txt+='\n'

    print (txt)

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open('output.txt','w') as f:
            f.write(txt)
    
    
