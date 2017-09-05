#2048
import curses
from random import randrange,choice
from collections import defaultdict

actions=['Up','Left','Down','Right','Restart','Exit'] #不同运行状态
letter_codes=[ord(ch) for ch in 'WASDRQwasdrq'] #对应输入键值
actions_dict=dict(zip(letter_codes,actions*2)) #二者建立对应词典

#界面对象
class GameField(object):
    def __init__(self,height=4,width=4,win=2048):
        self.height=height
        self.width=width
        self.win_value=2048
        self.score=0
        self.highscore=0
        self.reset()
    #随机数生成
    def spawn(self):
        new_element=4 if randrange(100)>89 else 2
        (i,j)=choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j]==0])
        self.field[i][j]=new_element
    #重置界面
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        self.field=[[0 for i in range(self.width)]for j in range(self.height)]#重置棋盘
        self.spawn()
        self.spawn()
    def draw(self,screen):
        help_string1='(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'
        def cast(string):
            screen.addstr(string+'\n')

        def draw_hor_separator():
            line='+'+('+------'*self.width+'+')[1:]
            separator=defaultdict(lambda:line)
            if not hasattr(draw_hor_separator,"counter"):
                draw_hor_separator.counter=0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter+=1
        def draw_row(row):
            cast(''.join('|{:^5}'.format(num)if num>0 else '|    'for num in row)+'|')
        
        screen.clear()

        cast('SCORE:'+str(self.score))
        if 0!=self.highscore:
            cast('HIGHSCORE:'+str(self.highscore))
        for row in self.field:
            draw_hor_separator()
            draw_row(row)

        draw_hor_separator()

        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)
    #移动操作
    def move(self,direction):
        def move_row_left(row):
            #left move
            def tighten(row):#临近元素靠拢
                new_row=[i for i in row if i!=0]
                new_row+=[0 for i in range(len(row)-len(new_row))]
                return new_row
            def merge(row):#相邻元素合并
                pair=False
                new_row=[]
                for i in range(len(row)):
                    if pair:
                        new_row.append(2*row[i])
                        self.score+=2*row[i]
                        pair=False
                    else:
                        if i+1<len(row) and row[i]==row[i+1]:
                            pair=True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row)==len(row)
                return new_row
            return tighten(merge(tighten(row)))
        
        moves={}
        moves['Left']=lambda field:[move_row_left(row) for row in field]
        moves['Right']=lambda field:invert(moves['Left'](invert(field)))
        moves['Up']=lambda field:transpose(moves['Left'](transpose(field)))
        moves['Down']=lambda field:transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field=moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        return any(any(i>=self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    def move_is_possible(self,direction):
        def row_is_left_movable(row):
            def change(i):
                if row[i]==0 and row[i+1]!=0:#可移动
                    return True
                if row[i]==0 and row[i+1]==row[i]:#可合并
                    return True
                return False
            return any(change(i)for i in range(len(row)-1))

        check={}
        check['Left']=lambda field:any(row_is_left_movable(row) for row in field)
        check['Right']=lambda field:check['Left'](invert(field))
        check['Up']=lambda field:check['Left'](transpose(field))
        check['Down']=lambda field:check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False
        

#获取有效输入
def get_user_action(keyboard):
    char='N'
    while char not in actions_dict:
        char=keyboard.getch()
    return actions_dict[char]

#矩阵转置
def transpose(field):
    return [list(row) for row in zip(*field)]
#矩阵逆转
def invert(field):
    return [row[::-1] for row in field]


                

def main(stdscr):
    '''主逻辑'''
    def init():
        #重置
        game_field.reset()
        return 'Game'

    def not_game(state):
        #结束或完成界面
        game_field.draw(stdscr)
        #用户输入判定是否重启
        action=get_user_action(stdscr)
        responses=defaultdict(lambda:state)
        #使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
        responses['Restart'],responses['Exit']='Init','Exit'
        return responses[action]

    def game():
        #画出当前状态
        game_field.draw(stdscr)
        #读取输入得到action
        action=get_user_action(stdscr)
        
        if action=='Restart':
            return 'Init'
        if action=='Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    state_actions={
        'Init':init,
        'Win':lambda:not_game('Win'),
        'Gameover':lambda:not_game('Gameover'),
        'Game':game
        }

    curses.use_default_colors()
    game_field=GameField(win=32)

    state='Init'


    #状态机开始运行
    while state!='Exit':
        state=state_actions[state]()

curses.wrapper(main)
    
