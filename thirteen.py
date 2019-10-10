# -*- coding: utf-8 -*-
import os
import sys

# 2 ♦0 ♣1 ♥2 ♠3
# 3 ♦4 ♣5 ♥6 ♠7
#获取牌型桶
def getBucket(cards):
    #创建数组
    bucket = []
    for i in range(6):
        bucket.append([])
        for j in range(16):
            bucket[i].append(0)
    #赋值有牌的地方
    for i in cards:
        bucket[i/4][i%4]=1;
    return backet

#创建一个空的出牌数组
def getPost():
    Post = []
    for i in range(3):
        bucket.append([])
        for j in range(5):
            bucket[i].append(0)
    return Post
#统计同数值花色的多少
def CardVal(cards):
    for i in range(14,1,-1):
        num=0
        for j in range(2,5):
            if cards[j][i]==1:
                num=num+1
        cards[5][i]=num
    return cards

cards=input()
bucket=getBucket()
#判断同花顺 判断同花个数 在判断有无联顺五个
def THShun(cards):
    a=CardHua()
    for i in range(1,5):
        if a[i][15]>=5:
            for j in range(14,5,-1):
                count=0
                for k in range(5):
                    if a[i][j-k]==1:
                        count=count+1
                if count==5:
                    return i,j
    return 0,0
#判断炸弹 传入数组相同数值四个花色则是炸弹
def ZDan(cards):
    a=CardVal()
    for i in range(14,1):
        if a[5][i]==4:
            return i
    return 0



