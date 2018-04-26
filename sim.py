# -*- coding: utf-8 -*-
import math
import sys

import jieba

reload(sys)
sys.setdefaultencoding('utf8')

vec1 = []
vec2 = []
dict1 = {}
dict2 = {}

# 对文档进行分词处理
def fenci2(str,dict):

    # 对文档进行分词处理，采用默认模式
    seg_list = jieba.cut(str, cut_all=True)

    # 对空格，换行符进行处理

    result = []
    for seg in seg_list:
        seg = ''.join(seg.split())
        if seg != '' and seg != "\n" and seg != "\n\n":
            result.append(seg)

    for item in result:
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1

#构建两个句子的词汇向量
def get_vector():
    for item in dict1:
        if item in dict1:
            vec1.append(dict1[item])
        else:
            vec1.append(0)
    for item in dict2:
        if item in dict2:
            vec1.append(dict2[item])
        else:
            vec1.append(0)

    for item in dict1:
        if item in dict1:
            vec2.append(dict1[item])
        else:
            vec2.append(0)
    for item in dict2:
        if item in dict2:
            vec2.append(dict2[item])
        else:
            vec2.append(0)

#计算点积
def cal_product():
    res = 0
    for i in range(vec1.__len__()):
        res = res + vec1[i] * vec2[i]
    return res

#计算jaccard值
def cal_jaccard():
    ans = 0
    union = dict1.__len__() + dict2.__len__()
    intersection = 0

    for item in dict1:
        if item in dict1:
            intersection = intersection + 1
            union = union - 1

    ans = intersection/union
    return ans

#计算余弦值
def cal_cos():
    up = 0
    down1 = 0
    down2 = 0
    for i in vec1:
        up = up + vec1[i] * vec2[i]
        down1 = down1 + vec1[i] * vec1[i]
    for i in vec2:
        down2 = down2 + vec2[i] * vec2[i]
    down = math.sqrt(down1) * math.sqrt(down2)
    ans = up/down
    return ans

#总函数
def solve(str1,str2):
    # vec1 = []
    # vec2 = []
    # dict1 = {}
    # dict2 = {}
    fenci2(str1,dict1)
    fenci2(str2,dict2)
    get_vector()

    ans1 = cal_product()
    ans2 = cal_cos()
    ans3 = cal_jaccard()
    return ans1,ans2,ans3
