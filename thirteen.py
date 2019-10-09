# -*- coding: utf-8 -*-
import os
import sys
import itertools

cards = ['a', 'b', 'c', 'd', 'e']
num=3
combination_with_num_para = list(itertools.combinations(cards, num))
'''
CN/M组合获取
例:make_ranks({1,2,3},2), 输出{{1,2}, {2,3}, {1,3}}
例:make_ranks({1,2,3},1), 输出{{1}, {2}, {3}}
总共有10种组合方式
[('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'b', 'e'),
 ('a', 'c', 'd'), ('a', 'c', 'e'), ('a', 'd', 'e'),
 ('b', 'c', 'd'), ('b', 'c', 'e'), ('b', 'd', 'e'),
 ('c', 'd', 'e')]
'''
print(combination_with_num_para)

SINGLE = 1
ONE_DOUBLE=2
FIVE_TWO_DOUBLE=3
THREE=4
FIVE_MIXED_FLUSH_NO_A=5
FIVE_FLUSH=6
FIVE_THREE_DEOUBLE=7
FIVE_FOUR_ONE=8
FIVE_STRAIGHT_FLUSH_NO_A=9

# 单张牌比大小 𝐴 > 𝐾 > 𝑄 > 𝐽 > 10 > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2
def singleCardCompare(a, b):
    if a>b:
        return 1
    elif a==b:
        return 0
    else:
        return -1

# 比较牌面值
def singleCardCompareValSmaller(a, b):
    res = singleCardCompare(a%0x10, b%0x10)
    # a>=b
    if res >= 0:
        return false
    # a<b
    else:
        return true

'''
-- 获取花色的桶
-- 输入:get_hua_bucket({0x1, 0x02, 0x11, 0x21, 0x31, 0x32})
-- 输出:{[0] = {1, 2}, [0x10] = {3}, [0x20] = {4}, [0x30] = {5, 6}}
'''
# 2 ♦0 ♣1 ♥2 ♠3
# 3 ♦4 ♣5 ♥6 ♠7
def get_hua_bucket(cards):
    bucket=[]
    for i in range(len(cards)):
        bucket[cards[i]%4].append(cards[i]/4+1)
    return bucket




def isTHua():
    return true
def isSZi():
    return true
def isTHShun():
    return true
def isZDan():
    return true
def isHLu():
    return true

