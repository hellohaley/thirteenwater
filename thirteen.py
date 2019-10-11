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

# 判断花色相同的情况，much代表需要判断几张同花（much为3或者5） 黑桃红桃草花方块
def CardHua(Cards):
    for i in range(1, 5):
        for j in range(2, 15):
            if card[i][j] == 1:
                sum = sum + 1
        Cards[i][15] = sum
    return Cards;


def CardTHua(Cards, much):
    for i in range(4, 0, -1):
        if Cards[i][15] >= much:
            return i  # 返回我手上是什么颜色的同花 若不符合much的要求，则返回0
            break
    return 0


def CardsDel(Cards, much, ij, Type):  # 删行1,列0
    if Type == 1:
        for time in range(0, much):
            for j in range(14, 1, -1):
                if Cards[ij][j] == 1:
                    Cards[ij][j] == 0
    if Type == 0:
        for time in range(0, much):
            for i in range(4, 0, -1):
                if Cards[i][ij] == 1:
                    Cards[i][ij] == 0


# 至尊青龙
def CardsZZQL(Cards):
    pd = 0
    for i in range(4, 0, -1):
        for j in range(2, 15):
            if Cards[i][j] == 1:
                pd = pd + 1
        if pd == 13:
            return 1  # 青龙
            break
        else:
            pd = 0
    if pd != 13:
        return 0


# 一条龙
def CardsYTL(Cards):
    pd = 0
    pdd = 0
    for j in range(2, 15):
        for i in range(4, 0, -1):
            if Cards[i][j] == 1:
                pd = 1
        if pd == 1:
            pdd = pdd + 1
        pd = 0
    if (pdd == 13):
        return 1
    else:
        return 0


# 十二皇族
def CardsSEHZ(Cards):
    pd = 1
    for j in range(11, 15):
        for i in range(4, 0, -1):
            if Cards[i][j] == 1:
                pd = 0
                return 0
                break
    if pd == 1:
        return 1


# 全大8-14
def CardsQD(Cards):
    pd = 1  # 先假设是拳大
    for j in range(2, 8):  # 除去8-A
        for i in range(4, 0, -1):
            if Cards[i][j] == 1:
                pd = 0
                return 0
                break
    if pd == 1:
        return 1


# 全小2-8
def CardsQX(Cards):
    pd = 1
    for j in range(9, 15):  # 9-A
        for i in range(4, 0, -1):
            if Cards[i][j] == 1:
                pd = 0
                return 0
                break
    if pd == 1:
        return 1


# 凑一色（放在最后便历）
def CardsCYS(Cards):
    ye = 0
    ss = 0
    for j in range(9, 15):  # 9-A
        for i in range(4, 0, -1):
            if Cards[i][j] == 1:
                pd = 0
                return 0
                break
    if pd == 1:
        return 1
