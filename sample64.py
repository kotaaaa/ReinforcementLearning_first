# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
from time import sleep
import random

GENMAX=100
STATENO=64
ACTIONNO=4
ALPHA=0.1
GAMMA=0.9
EPSILON=0.3
REWARD=10
GOAL=63
UP=0
DOWN=1
LEFT=2
RIGHT=3
LEVEL=500
# s_list = []
s_first_list = [0]

def updateq(s,snext,a,qvalue):
    qv = 0
    if(snext==GOAL):
        qv=qvalue[s][a]+ALPHA*(REWARD-qvalue[s][a])
    else:
        qv=qvalue[s][a]+ALPHA*(GAMMA*qvalue[snext][set_a_by_q(snext,qvalue)]-qvalue[s][a]);
    return qv

def selecta(s, qvalue):
    a=0

    if(random.random()<EPSILON):

        while True:
            a=random.randrange(4)
            if(qvalue[s][a]!=0):
                break

    else:
        a=set_a_by_q(s,qvalue);
    return a

def set_a_by_q(s,qvalue):
    maxq=0
    maxaction=0
    i=0
    for i in range(ACTIONNO):
        if(qvalue[s][i]>maxq):
              maxq=qvalue[s][i]
              maxaction=i

    return maxaction

def nexts(s,a):
    next_s_value=[]
    next_s_value=[-8,8,-1,1]
    return s+next_s_value[a];

def printqvalue(qvalue):
    i=0
    j=0

    for i in range(STATENO):
        print(i,"\t");
        for j in range(ACTIONNO):
            # // printf("Action-%d ",j);
            print(qvalue[i][j]," \t");
            # // printf("\n");
        print("\n");

def show_rect(screen, place):# (0<=place<=64)
        pygame.draw.rect(screen,(250,180,0),Rect((place%8)*50,int(place/8)*50,50,50))   # 四角形を描画(塗りつぶしなし)
        pygame.display.update()     # 画面を更新

def pygame_show(show_list):

    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((400, 400))    # 大きさ400*400の画面を生成
    pygame.display.set_caption("Test")              # タイトルバーに表示する文字
    screen.fill((255,255,255))        # 画面を黒色(#000000)に塗りつぶし
    # screen = wrappers.Monitor(screen, './movie/movie1')
    i=0
    # while(i<=64):
    for i in range(len(show_list)):
        screen.fill((255,255,230))        # 画面を黒色(#000000)に塗りつぶし
        show_rect(screen, show_list[i])
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()    # Pygameの終了(画面閉じられる)
                sys.exit()
        i+=1
        sleep(0.3)

def main():
    qvalue = [[0 for i in range(ACTIONNO)] for j in range(STATENO)]
    for i in range(STATENO):
        for j in range(ACTIONNO):
            qvalue[i][j]=random.random()
            if(i<=7):
                qvalue[i][UP]=0
            if(i>=56):
                qvalue[i][DOWN]=0
            if(i%8==0):
                qvalue[i][LEFT]=0
            if(i%8==7):
                qvalue[i][RIGHT]=0

    for i in range(GENMAX):
        s=0
        s_list=[0]
        for t in range(LEVEL):
            a=selecta(s,qvalue)
            print(t,": s=",s," a=",a)
            snext=nexts(s,a)
            qvalue[s][a]=updateq(s,snext,a,qvalue)
            s=snext
            s_list.append(s)
            # if((t==0)and(i==0)):
            if(i==0):
                s_first_list.append(s)
            if(s==63):
            # if(GOAL==str(s)):
                break;

        print("last_state>> ",s,"\n");
        # if(s==GOAL):
        if(s==63):
        # if(GOAL==str(s)):
            print("GOOOOOOOOOAL\n");

    print(s_list)
    print(s_first_list)
    print(len(s_list))
    print(len(s_first_list))
    pygame_show(s_list)


if __name__ == '__main__':
    main()
