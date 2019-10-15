# -*- coding: utf-8 -*-

import re
import os
import json
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
        a = int(i/4)
        b = i % 4 + 1
        bucket[b][a] = 1
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

# 判断同花顺 判断同花个数 在判断有无联顺much个
def CardsTHS(cards_, much):
    for i in range(1, 5):
        if cards_[i][15] >= much:
            for j in range(14, much, -1):
                count = 0
                for k in range(much):
                    if cards_[i][j - k] == 1:
                        count = count + 1
                if count == much:
                    return i, j
    return 0, 0

# 判断普通牌型
def judge5(_post, _pai):
    post1 = _post
    left = _pai
    cards_ = getBucket(left)
    cards_ = CardVal(cards_)
    a, b = CardsTHS(cards_, 5)
    op = 0
    # 有同花顺
    if a != 0 and b != 0:
        for i in range(5):
            post1.append(cards_[a][b - i])
            left.remove((b - i) * 4 + a-1)
            cards_[a][b - i] = 0
        op = 9
    # 没有同花顺
    else:
        dz = 0
        st = 0
        zd = 0
        sp = 0
        th = 0
        # 得到炸弹 三条 对子 同花的个数
        for i in range(2, 15):
            if cards_[5][i] == 4:
                zd = zd + 1
            elif cards_[5][i] == 3:
                st = st + 1
            elif cards_[5][i] == 2:
                dz = dz + 1
            elif cards_[5][i] == 1:
                sp = sp + 1
        if zd != 0:
            op = 8
            for i in range(14, 1, -1):
                if cards_[5][i] == 4:
                    for j in range(1, 5):
                        post1.append(i * 4 + j-1)
                        left.remove(i * 4 + j-1)
                        cards_[j][i] = 0
                    zd = zd - 1
                    break
        elif st != 0 and dz != 0:
            for i in range(14, 1, -1):
                if cards_[5][i] == 3:
                    for j in range(1, 5):
                        if cards_[j][i] != 0:
                            post1.append(i * 4 + j-1)
                            left.remove(i * 4 + j-1)
                            cards_[j][i] = 0
                    st = st - 1
                    break
            for i in range(2, 15):
                if cards_[5][i] == 2:
                    for j in range(1, 5):
                        if cards_[j][i] != 0:
                            post1.append(i * 4 + j-1)
                            left.remove(i * 4 + j-1)
                            cards_[j][i] = 0
                    dz = dz - 1
                    break
            op = 7
        else:
            # 有同花
            for i in range(4, 0, -1):
                # 同花
                if cards_[i][15] >= 5:
                    th = th + 1
                    op = 6
                    if cards_[i][15] == 5:
                        for j in range(2, 15):
                            if cards_[i][j] != 0:
                                post1.append(j * 4 + i-1)
                                left.remove(j * 4 + i-1)
                                cards_[i][j] = 0
                                cards_[5][j]=cards_[5][j]-1
                        cards_[i][15]=0
                    else:
                        for j in range(2, 15):
                            if cards_[i][j] != 0:
                                post1.append(j * 4 + i-1)
                                left.remove(j * 4 + i-1)
                                cards_[i][j] = 0
                                break
                        k = 0
                        for j in range(2, 15):
                            if cards_[i][j] != 0 and cards_[5][j] == 1:
                                post1.append(j * 4 + i-1)
                                left.remove(j * 4 + i-1)
                                cards_[i][j] = 0
                                k = k + 1
                            if k == 4:
                                break
                        if k < 4:
                            k = 4 - k
                            for j in range(2, 15):
                                if cards_[i][j] != 0:
                                    post1.append(j * 4 + i-1)
                                    left.remove(j * 4 + i-1)
                                    cards_[i][j] = 0
                                    k = k - 1
                                if k == 0:
                                    break
                    break
            # 无同花，判断顺子
            if op == 0:
                for i in range(14, 5, -1):
                    len = 0
                    for j in range(5):
                        if cards_[5][i - j] > 0:
                            len = len + 1
                    if len == 5:
                        op = i
                        break
                # 有顺子
                if op != 0:
                    for i in range(op, op - 5, -1):
                        for j in range(1, 5):
                           if cards_[j][i] != 0:
                                post1.append(i * 4 + j-1)
                                left.remove(i * 4 + j-1)
                                cards_[j][i] = 0
                                break
                    op = 5
                # 无顺子
                else:
                    st = 0
                    dz = 0
                    sp = 0
                    for i in range(2, 15):
                        if cards_[5][i] == 3:
                            st = st + 1
                        elif cards_[5][i] == 2:
                            dz = dz + 1
                        elif cards_[5][i] == 1:
                            sp = sp + 1
                    # 有三条
                    if st > 0:
                        for i in range(14, 1, -1):
                            if cards_[5][i] == 3:
                                op = 4
                                for j in range(1, 5):
                                    if cards_[j][i] != 0:
                                        post1.append(i * 4 + j-1)
                                        left.remove(i * 4 + j-1)
                                        cards_[j][i] = 0
                                break
                    # 没有三条有对子
                    elif dz > 0:
                        # 有二对
                        if dz >= 2:
                            op = 3
                            for i in range(14, 1, -1):
                                if cards_[5][i] == 2:
                                    for j in range(1, 5):
                                        if cards_[j][i] != 0:
                                            post1.append(i * 4 + j-1)
                                            left.remove(i * 4 + j-1)
                                            cards_[j][i] = 0
                                    cards_[5][i] = 0
                                    break
                            for i in range(2, 15):
                                if cards_[5][i] == 2:
                                    for j in range(1, 5):
                                        if cards_[j][i] != 0:
                                            post1.append(i * 4 + j-1)
                                            left.remove(i * 4 + j-1)
                                            cards_[j][i] = 0
                                    cards_[5][i] = 0
                                    break
                        # 有一对
                        else:
                            op = 2
                            for i in range(2, 15):
                                if cards_[5][i] == 2:
                                    for j in range(1, 5):
                                        if cards_[j][i] != 0:
                                            post1.append(i * 4 + j - 1)
                                            left.remove(i * 4 + j - 1)
                                            cards_[j][i] = 0
                                    break
                    # 散牌
                    else:
                        op = 1
                        k=0
                        for i in range(14, 2,-1):
                            for j in range(1, 5):
                                if cards_[j][i] != 0:
                                    post1.append(i * 4 + j-1)
                                    left.remove(i * 4 + j-1)
                                    cards_[j][i] = 0
                                    k=k+1
                                    break
                            if k==1:
                                break
                        for i in range(2, 15):
                            for j in range(1, 5):
                                if cards_[j][i] != 0:
                                    post1.append(i * 4 + j-1)
                                    left.remove(i * 4 + j-1)
                                    cards_[j][i] = 0
                                    k = k + 1
                                if k == 5:
                                    break
                            if k == 5:
                                break
    return post1, left,  op


# 同花顺 同花 顺子 三条 对子 散牌
def judge3(_post1, _post2, _pai, ty1, ty2):
    chu3=[]
    post1 = _post1
    post2 = _post2
    left = _pai
    cards_ = getBucket(left)
    cards_ = CardVal(cards_)
    st = 0
    stp = 0
    dz = 0
    dzp = 0
    sp = 0
    ty3 = 0
    for i in range(14, 1, -1):
        if cards_[5][i] == 3:
            st = st + 1
            if stp == 0:
                stp = i
        elif cards_[5][i] == 2:
            dz = dz + 1
            if dzp == 0:
                dzp = i
        elif cards_[5][i] == 1:
            sp = sp + 1
    if st > 0:
        for i in range(1, 5):
            if cards_[i][stp] != 0:
                chu3.append(i-1 + stp * 4)
                cards_[i][stp] = 0
                left.remove(i-1 + stp * 4)
        st=st-1
        cards_[5][stp]=st
        ty3 = 3
    elif dz > 0:
        for i in range(1, 5):
            if cards_[i][dzp] != 0:
                chu3.append(i-1 + dzp * 4)
                cards_[i][dzp] = 0
                left.remove(i-1 + dzp * 4)
        dz=dz-1
        cards_[5][dzp]=dz
        for i in range(2, 15):
            if cards_[5][i] != 0:
                for j in range(1, 5):
                    if cards_[j][i] != 0:
                        chu3.append(j-1 + i * 4)
                        cards_[j][i] = 0
                        left.remove(j-1 + i * 4)
                cards_[5][i]=cards_[5][i]-1
                break
        ty = 2
    # 仅剩散牌
    else:
        k = 0
        for i in range(14, 1, -1):
            if cards_[5][i] != 0:
                for j in range(1, 5):
                    if cards_[j][i] != 0:
                        chu3.append(j-1 + i * 4)
                        cards_[j][i] = 0
                        left.remove(j-1 + i * 4)
                        cards_[5][i]=cards_[5][i]-1
                        cards_[j][15]=cards_[j][15]-1
                        k=k+1
                        break
                if k==1:
                    break
        for i in range(2,15):
            if cards_[5][i] != 0:
                for j in range(1, 5):
                    if cards_[j][i] != 0 and k!=3:
                        chu3.append(j-1 + i * 4)
                        cards_[j][i] = 0
                        left.remove(j-1 + i * 4)
                        cards_[5][i]=cards_[5][i]-1
                        cards_[j][15]=cards_[j][15]-1
                        k=k+1
        ty = 1
    if ty1 == 8 or ty1 == 3:
        m = left[0]
        post1.append(m)
        del left[0]
    elif ty1 == 4 or ty1 == 2:
        m = left[0]
        post1.append(m)
        del left[0]
        m = left[0]
        post1.append(m)
        del left[0]
        if ty1==2:
            m = left[0]
            post1.append(m)
            del left[0]
    if ty2 == 8 or ty2 == 3:
        m=left[0]
        post2.append(m)
        del left[0]
    elif ty2 == 4 or ty2 == 2:
        m = left[0]
        post2.append(m)
        del left[0]
        m = left[0]
        post2.append(m)
        del left[0]
        if ty2==2:
            m = left[0]
            post2.append(m)
            del left[0]
    return post1,post2,chu3


def zhuanCards(chu):
    chui=[]
    z=0
    h=0#print(" ".join('%s' %id for id in list1))
    for i in range(len(chu)):
        z=int(chu[i]/4)
        h=int(chu[i]%4+1)
        if h==4:
            chui.insert(0,"$")
        elif h==3:
            chui.insert(0,"&")
        elif h==2:
            chui.insert(0,"*")
        elif h==1:
            chui.insert(0,"#")
        if z<11 :        #2-10
            chui.insert(1,z)
        elif z==11:
            chui.insert(1,"J")
        elif z==12:
            chui.insert(1,"Q")
        elif z==13:
            chui.insert(1,"K")
        elif z==14:
            chui.insert(1,"A")
        iii="".join('%s' %id for id in chui)
        chu[i]=iii
        chui.pop(1)
        chui.pop(0)
    return chu


def divide_cards(client):
    client=" ".join('%s' %id for id in client)
    pai=[]
    m=0
    j=0
    for i in client:
        if i=="#":
            m=0
        elif i=="*":
            m=1
        elif i=="&":
            m=2
        elif i =="$":
            m=3
        elif i!=" "and i != "1":
            if i=="A":
                j=14
            elif i=="J":
                j=11
            elif i=="Q":
                j=12
            elif i=="K":
                j=13
            elif i=="0":
                j=10
            elif i=="9":
                j=9
            elif i=="8":
                j=8
            elif i=="7":
                j=7
            elif i=="6":
                j=6
            elif i=="5":
                j=5
            elif i=="4":
                j=4
            elif i=="3":
                j=3
            elif i=="2":
                j=2
            pai.append(m+j*4)

    chu1 = []
    chu2 = []
    chu3 = []
    chu1, pai, op1 = judge5(chu1, pai)
    chu2, pai, op2 = judge5(chu2, pai)
    chu1,chu2,chu3 = judge3(chu1, chu2, pai, op1, op2)
    chu1=zhuanCards(chu1)
    chu2=zhuanCards(chu2)
    chu3=zhuanCards(chu3)
    chu=[]
    for i in chu1:
        chu.append(i)
    for i in chu2:
        chu.append(i)
    for i in chu3:
        chu.append(i)
    return chu
#client="*8 #7 $10 &6 $8 #Q *J &A &7 $4 &J &3 $6"
#print(divide_cards(client))
