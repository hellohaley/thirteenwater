# -*- coding: utf-8 -*-
import os
import sys


# 2 ♦0 ♣1 ♥2 ♠3
# 3 ♦4 ♣5 ♥6 ♠7

# 获取牌型桶
def getBucket(arr_card):
    # 创建数组
    bucket = []
    for i in range(6):
        bucket.append([])
        for j in range(16):
            bucket[i].append(0)
    # 赋值有牌的地方
    for i in arr_card:
        a = int(i / 4)
        b = int(i % 4)
        bucket[a][b] = 1
    return bucket


# 统计同数值花色的多少并统计同花色数值的多少
def CardVal(cards_):
    for i in range(2, 15):
        sum = 0
        for j in range(1, 5):
            if cards_[j][i] == 1:
                sum = sum + 1
        cards_[5][i] = sum
    for i in range(1, 5):
        sum = 0
        for j in range(2, 15):
            if cards_[i][j] == 1:
                sum = sum + 1
        cards_[i][15] = sum
    return cards_


# 至尊青龙 13 张牌为清一色（同花色） 的从 1（A）－13（K）
def CardsZZQL():
    for i in range(1, 5):
        if cards[15][i] == 13:
            return i
    return 0


# 一条龙 13 张牌为从 14（A）－13（K）######出牌顺序
def CardsYTL():
    count = 0
    for i in range(2, 15):
        if cards[5][i] == 1:  # 每个数字只有一张
            count = count + 1
    if count == 13:
        return 1
    return 0


# 十二皇族 13 张牌中 12 张都是大于 10 的牌（J、 Q、 K、 A）
def CardsSEHZ():
    sum = 0
    for i in range(14, 10, -1):
        sum += cards[5][i]
    if sum == 12:
        return 1
    else:
        return 0


# 三同花顺 头墩，中墩，底墩都为同花顺 ---------------------------------------------------------------
def CardsSTHS():
    m = 0
    for m in range(2):
        i, jj = THShun(cards, 5)  # 最大吨与倒数第二吨都变为0
        if i > 0:
            for j in (jj, jj - 5, -1):
                cards[i][j] = 0
        i, jj = THShun(cards, 3)
        if i > 0:
            return 1  # 此时最低吨也有了，所以成公
    return 0


# 三分天下 13张牌出现 3 副炸弹加一张杂牌
def CardsSFTX():
    sum = 0
    for i in range(2, 9):
        if cards[5][i] == 4:
            sum = sum + 1
    if sum == 3:
        return 1
    else:
        return 0


# 全大 8-14
def CardsQD():
    sum = 0
    for i in range(14, 7, -1):
        sum += cards[5][i]
    if sum == 13:
        return 1
    else:
        return 0


# 全小 2-8
def CardsQX():
    sum = 0
    for i in range(2, 9):
        sum += cards[5][i]
    if sum == 13:
        return 1
    else:
        return 0


# 凑一色（放在最后便历）13 张牌都是方块、梅花或者黑桃、红心（指的在杂牌无任何特殊牌型出现的情况下））
def CardsCYS():
    if (cards[1][15] == 0 and cards[3][15] == 0):  # /如果都没有红色的卡，说明是黑色的凑一色
        return 1
    elif (cards[2][15] == 0 and cards[4][15] == 0):  # /如果都没有黑色的卡，说明是红色的凑一色
        return 1
    else:
        return 0


# 双怪冲三 指的是 2 对葫芦+1 个对子+任意一张杂牌
def CardsSGCS():
    sumt = 0
    sumd = 0
    for i in range(2, 15):
        if cards[5][i] == 3:
            sumt = sumt + 1
        if cards[5][i] == 2:
            sumd = sumd + 1
    if sumt == 2 and sumd == 3:
        return 1
    else:
        return 0


# 四套三条 指的是 4 套相同的三张牌+任意一张杂牌
def CardsSTST():
    sum = 0
    for i in range(2, 15):
        if cards[5][i] == 3:
            sum = sum + 1
    if sum == 4:
        return 1
    else:
        return 0


# 五对三条 指的是 5 个对子+三张相同的牌型（三张牌冲头）
def CardsWDST():
    sumt = 0
    sumd = 0
    for i in range(2, 15):
        if cards[5][i] == 2:
            sumd = sumd + 1
        if cards[5][i] == 3:
            sumt = sumt + 1
    if sumt == 1 and sumd == 5:
        return 1
    else:
        return 0


# 六对半 指的是 6 个对子+任意一张杂牌
def CardsLDB():
    sum = 0
    for i in range(2, 15):
        if cards[5][i] == 2:
            sum = sum + 1
    if sum == 6:
        return 1
    else:
        return 0


# 三顺子 指三敦水都是顺子牌（也成杂顺）  --------------------------------------------------------------------------
def CardsSSZ():
    for i in range(2, 15):
        if cards[5][i] > 3:
            return 0
        else:
            big = 0
            small = 0
            for i in range(2):
                for j in range(14, 5, -1):
                    count = 0
                    for k in range(5):
                        if a[5][j - k] >= 1:
                            count = count + 1
                            a[5][j - k] = a[5][j - k] - 1
                    if count == 5:
                        big = big + 1
            if big != 2:
                return 0
            else:
                for j in range(14, 5, -1):
                    count = 0
                    for k in range(3):
                        if a[5][j - k] == 1:
                            count = count + 1
                    if count == 3:
                        small = small + 1
                if small == 1:
                    return 1
    return 0


# 三同花 指三敦水都是同一种花色牌（也成杂花）
def CardsSTH():
    sum = []
    for i in range(1, 5):
        if int(cards[1][15]) > 0:
            sum.append(cards[i][15])
    if len(sum) == 3:
        countf = 0
        countt = 0
        for i in sum:
            if i == 5:
                countf = countf + 1
            if i == 3:
                countt = countt + 1
        if countf == 2 and countt == 1:
            return 1
    elif len(sum) == 2:
        countt = 0
        countf = 0
        counte = 0
        countten = 0
        for i in sum:
            if i == 3:
                countt = countt + 1
            elif i == 5:
                countf = count + 1
            elif i == 8:
                counte = counte + 1
            elif i == 10:
                countten = countten + 1
        if countt == 1 and countten == 1:
            return 1
        elif countf == 1 and counte == 1:
            return 1
    return 0


# 判断同花顺 判断同花个数 在判断有无联顺much个
def CardsTHS(cards_,much):
    for i in range(1, 5):
        if cards_[i][15] >= much:
            for j in range(14, much, -1):
                count = 0
                for k in range(much):
                    if cards_a[i][j - k] == 1:
                        count = count + 1
                if count == much:
                    return i, j
    return 0, 0


# 判断炸弹 传入数组相同数值四个花色则是炸弹
def CardsZD(cards_):
    for i in range(14, 1, -1):
        if cards_[5][i] == 4:
            return i
    return 0


# 判断花色相同的情况，much代表需要判断几张同花（much为3或者5） 黑桃红桃草花方块
def CardsTH(cards_,much):
    for i in range(4, 0, -1):
        if cards_[i][15] >= much:
            return i  # 返回我手上是什么颜色的同花 若不符合much的要求，则返回0
    return 0


# 删行1,列0
def CardsDel(cards_,much, ij, type):
    if type == 1:
        for time in range(0, much):
            for j in range(14, 1, -1):
                if cards_[ij][j] == 1:
                    cards_[ij][j] = 0
    if type == 0:
        for time in range(0, much):
            for i in range(4, 0, -1):
                if cards_[i][ij] == 1:
                    cards_[i][ij] = 0


# 判断有无特殊牌型
def isSpacial():
    if CardsZZQL() != 0:
        return 1
    elif CardsYTL() != 0:
        return 1
    elif CardsSEHZ() != 0:
        return 1
    elif CardsSTHS() != 0:
        return 1
    elif CardsSFTX() != 0:
        return 1
    elif CardsQD() != 0:
        return 1
    elif CardsQX() != 0:
        return 1
    elif CardsCYS() != 0:
        return 1
    elif CardsSGCS() != 0:
        return 1
    elif CardsSTST() != 0:
        return 1
    elif CardsWDST() != 0:
        return 1
    elif CardsLDB() != 0:
        return 1
    elif CardsSSZ() != 0:
        return 1
    elif CardsSTH() != 0:
        return 1
    else:
        return 0


# 按格式输出三墩
def postThree():
    i = 0
    for j in range(3):
        if j == 0:
            for k in range(3):
                print(post[i])
                print(" ")
                i = i + 1
        else:
            for k in range(5):
                print(post[i])
                print(" ")
                i = i + 1
        print("\n")


# 输出所有牌
def postAll():
    for i in pai:
        print(i)


#判断普通牌型
def judge1():
    post1=post
    left=pai
    cards_=cards
    a,b=CardsTHS(cards_,5)
    op=0
    if a!=0 and b!=0:
        for i in range(5):
            post1.append(cards_[a][b-i])
            left.remove((b-i)*4+a)
            cards_[a][b - i]=0
        op=9
    else:
        dz=0
        st=0
        zd=0
        sp=0
        th=0
        for i in range(2,15):
            if cards_[5][i]==4:
                zd=zd+1
            elif cards_[5][i]==3:
                st=st+1
            elif cards_[5][i]==2:
                dz=dz+1
            elif cards_[5][i]==1:
                sp=sp+1
        if zd!=0:
            op=8
            for i in range(14,1,-1):
                if cards_[5][i]==4:
                    for j in range(1,5):
                        post1.append(i*4+j)
                        left.remove(i*4+j)
                        cards_[j][i]=0
                    zd=zd-1
                    break
        elif st!=0 and dz!=0:
            for i in range(14,1,-1):
                if cards_[5][i]==3:
                    for j in range(1,5):
                        if cards_[j][i]!=0:
                            post1.append(i * 4 + j)
                            left.remove(i * 4 + j)
                            cards_[j][i] = 0
                    st=st-1
                    break
            for i in range(2, 15):
                if cards_[5][i]==2:
                    for j in range(1,5):
                        if cards_[j][i]!=0:
                            post1.append(i * 4 + j)
                            left.remove(i * 4 + j)
                            cards_[j][i] = 0
                    dz=dz-1
                    break
            op=7
        else:
            #有同花
            for i in range(4,0,-1):
                #同花
                if cards_[i][15]>=5:
                    th=th+1
                    op=6
                    if cards_[i][15]==5:
                        for j in range(2, 15):
                            if cards_[i][j] != 0:
                                post1.append(j * 4 + i)
                                left.remove(j * 4 + i)
                                cards_[i][j] = 0
                    else:
                        for j in range(2, 15):
                            if cards_[i][j] != 0:
                                post1.append(j * 4 + i)
                                left.remove(j * 4 + i)
                                cards_[i][j] = 0
                                break
                        k=0
                        for j in range(2,15):
                            if cards_[i][j]!=0 and cards_[5][j]==1:
                                post1.append(j * 4 + i)
                                left.remove(j * 4 + i)
                                cards_[i][j] = 0
                                k=k+1
                            if k==4:
                                break
                        if k<4:
                            k=4-k
                            for j in range(2,15):
                                if cards_[i][j]!=0:
                                    post1.append(j * 4 + i)
                                    left.remove(j * 4 + i)
                                    cards_[i][j] = 0
                                    k = k - 1
                                if k==0:
                                    break
                    break
            #无同花，判断顺子
            if op==0:
                for i in range(14,5,-1):
                    len = 0
                    for j in range(5):
                        if cards_[5][i-j]>1:
                            len=len+1
                    if len == 5:
                        op = i
                        break
                #有顺子
                if op!=0:
                    for i in range(op,op-5,-1):
                        for j in range(1,5):
                            if cards_[j][i]!=0:
                                post1.append(i * 4 + j)
                                left.remove(i * 4 + j)
                                cards_[j][i] = 0
                                break
                    op=5
                #无顺子
                else:
                    st=0
                    dz=0
                    sp=0
                    for i in range(2, 15):
                        if cards_[5][i] == 3:
                            st = st + 1
                        elif cards_[5][i] == 2:
                            dz = dz + 1
                        elif cards_[5][i] == 1:
                            sp = sp + 1
                    #有三条
                    if st>0:
                        for i in range(14,1,-1):
                            if cards_[5][i]==3:
                                op=4
                                for j in (1,5):
                                    if cards_[j][i]!=0:
                                        post1.append(i * 4 + j)
                                        left.remove(i * 4 + j)
                                        cards_[j][i] = 0
                                break
                    #没有三条有对子
                    elif dz>0:
                        #有二对
                        if dz>=2:
                            op=3
                            for i in range(14,1,-1):
                                if cards_[5][i]==2:
                                    for j in (1, 5):
                                        if cards_[j][i] != 0:
                                            post1.append(i * 4 + j)
                                            left.remove(i * 4 + j)
                                            cards_[j][i] = 0
                                    break
                            for i in range(2,15):
                                if cards_[5][i]==2:
                                    for j in (1, 5):
                                        if cards_[j][i] != 0:
                                            post1.append(i * 4 + j)
                                            left.remove(i * 4 + j)
                                            cards_[j][i] = 0
                                    break
                        #有一对
                        else:
                            op=2
                            for i in range(2,15):
                                if cards_[5][i]==2:
                                    for j in (1, 5):
                                        if cards_[j][i] != 0:
                                            post1.append(i * 4 + j)
                                            left.remove(i * 4 + j)
                                            cards_[j][i] = 0
                                    break
                    else:
                        op=1
                        k=0
                        for i in range(15,2):
                            for j in range(1,5):
                                if cards_[j][i]!=0:
                                    post1.append(i * 4 + j)
                                    left.remove(i * 4 + j)
                                    cards_[j][i] = 0
                                    k=k+1
                                if k==5:
                                    break
                            if k ==5:
                                break








pai = []
for t in range(13):
    num = input()
    pai.append(num)
cards = getBucket(pai)
cards = CardVal(cards)
post=[]
flag = isSpecial()
if flag == 1:
    postAll()
else:
    judge1()
    judge2()
    postThree()
