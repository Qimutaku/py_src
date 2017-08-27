#design
import time as t

class timer:
    def __init__(self):
        self.pro="还未开始计时！"
        self.lasted=[]
        self.unit=['年','月','天','小时','分钟','秒']
    def start(self):
        self.t1=t.localtime()
        print("计时器开始")
    def stop(self):
        self.t2=t.localtime()
        self._calc()
        print("计时器结束")
    def test(self):
        print(str(self.t1)+'\n')
        print(str(self.t2))
    #def a(self):
    #print(str(self.t2)-str(self.t1))
    def _calc(self):
        self.lasted=[]
        self.pro="The sum times:"
        for each in range(6):
            self.lasted.append(self.t2[each]-self.t1[each])
          
            if self.lasted[each]:
                self.pro+=str(self.lasted[each])+self.unit[each]
        #print(self.pro)
    def __str__(self):
        '''类进行字符串化'''
        return self.pro
    #__repr__=__str__ #设置输入对象名称时内容：__repr__
    def __repr__(self):
        return self.pro

    def test2(self):
        a=input("input:")
        if not a:
            print("error")
        else :
            print("yes")
