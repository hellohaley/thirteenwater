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

#统计同数值花色的多少并统计同花色数值的多少
def CardVal(cards):
    for i in range(2,15):
        num=0
        for j in range(1,5):
            if cards[j][i]==1:
                sum=sum+1
        cards[5][i]=sum
    for i in range(1, 5):
        for j in range(2, 15):
            if card[i][j] == 1:
                sum = sum + 1
        Cards[i][15] = sum
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
def CardTHua(Cards, much):
    for i in range(4, 0, -1):
        if Cards[i][15] >= much:
            return i  # 返回我手上是什么颜色的同花 若不符合much的要求，则返回0
            break
    return 0

# 删行1,列0
#something wrong
def CardsDel(Cards, much, ij, Type):
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


# 至尊青龙 13 张牌为清一色（同花色） 的从 1（A）－13（K）
def CardsZZQL(Cards):
    for i in range(1,5):
        if cards[15][i]==13:
            return 1
    return 0


# 一条龙 13 张牌为从 1（A）－13（K）
def CardsYTL(Cards):
    pd = 0
    for i in range(2, 15):
        if Cards[5][i] == 0:
            return 0
    return 1


# 十二皇族 13 张牌中 12 张都是大于 10 的牌（J、 Q、 K、 A）
def CardsSEHZ(Cards):
    sum=0
    for i in range(14,9,-1):
        sum+=cards[5][i]
    if sum==12:
        return 1
    else:
        return 0

#三同花顺 头墩，中墩，底墩都为同花顺
def STHShun():

    return 0
#三分天下 13张牌出现 3 副炸弹加一张杂牌
def SFTXia():
    sum = 0
    for i in range(2, 9):
        if cards[5][i]==4:
            sum =sum+1
    if sum == 3:
        return 1
    else:
        return 0
    return 0

# 全大 8-14
def CardsQD(Cards):
    sum = 0
    for i in range(14, 7, -1):
        sum += cards[5][i]
    if sum == 13:
        return 1
    else:
        return 0

# 全小 2-8
def CardsQX(Cards):
    sum = 0
    for i in range(2, 9):
        sum += cards[5][i]
    if sum == 13:
        return 1
    else:
        return 0

# 凑一色（放在最后便历）13 张牌都是方块、梅花或者黑桃、红心（指的在杂牌无任何特殊牌型出现的情况下））
def CardsCYS(Cards):
    if (Cards[1][15]==0 and Cards[3][15]==0):#/如果都没有红色的卡，说明是黑色的凑一色
        return 1
    elif (Cards[2][15]==0 and Cards[4][15]==0):#/如果都没有黑色的卡，说明是红色的凑一色
        return 1
    else:
        return 0

#双怪冲三 指的是 2 对葫芦+1 个对子+任意一张杂牌
def EDCSan(cards):
    sumt=0
    sumd=0
    for i in range(2,15):
        if cards[5][i]==3:
            sumt=sumt+1
        if cards[5][i]==2:
            sumd=sumd+1
    if sumt==2 and sumd ==3:
        return 1
    else:
        return 0

#四套三条 指的是 4 套相同的三张牌+任意一张杂牌
def STSTiao(cards):
    sum=0
    for i in range(2, 15):
        if cards[5][i] == 3:
            sum = sum + 1
    if sum == 4:
        return 1
    else:
        return 0

#五对三条 指的是 5 个对子+三张相同的牌型（三张牌冲头）
def WDSTiao(cards):
    sumt=0
    sumd=0
    for i in range(2,15):
        if cards[5][i]==2:
            sumd=sumd+1
        if cards[5][i]==3:
            sumt=sumt+1
    if sumt==1 and sumd==5:
        return 1
    else:
        return 0

#六对半 指的是 6 个对子+任意一张杂牌
def LDBan(cards):
    sum=0
    for i in range(2,15):
        if cards[5][i]==2:
            sum=sum+1
    if sum==6:
        return 1
    else:
        return 0
#三顺子 指三敦水都是顺子牌（也成杂顺）

#三同花 指三敦水都是同一种花色牌（也成杂花）
def STHua(cards):
    sum=[]
    for i in range(1,5):
        if cards[1][15]>0:
            sum.append(cards[i][15])
    if len(sum)==3:
        countf=0
        countt=0
        for i in sum:
            if i==5:
                countf=countf+1
            if i==3:
                countt=countt+1
        if countf==2 and countt=1:
            return 1
    elif len(sum)==2:
        countt=0
        countf=0
        counte=0
        countten=0
        for i in sum:
            if i==3:
                countt=countt+1
            elif i==5:
                countf=count+1
            elif i==8:
                counte=counte+1
            elif i==10:
                countten=countten+1
        if countt==1 and countten==1:
            return 1
        elif countf==1 and counte==1:
            return 1
    return 0
