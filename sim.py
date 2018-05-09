# -*- coding: utf-8 -*-
import math
import sys

import jieba

reload(sys)
sys.setdefaultencoding('utf8')

# 对文档进行分词处理
# def fenci2(str1,str2):
#     # dict.clear()
#     # 对文档进行分词处理，采用默认模式
#     seg_list1 = jieba.cut(str1, cut_all=True)
#     seg_list2 = jieba.cut(str2,cut_all=True)
#
#     # 对空格，换行符进行处理
#     # result1.clear()
#
#     for seg in seg_list1:
#         seg = ''.join(seg.split())
#         if seg != '' and seg != "\n" and seg != "\n\n":
#             result1.append(seg)
#
#     for item in result1:
#         # print item + " 1"
#         if item in dict:
#             dict[item] = dict[item] + 1
#         else:
#             dict[item] = 1
#
#     # result2.clear()
#     for seg in seg_list2:
#         seg = ''.join(seg.split())
#         if seg != '' and seg != "\n" and seg != "\n\n":
#             result2.append(seg)
#
#     for item in result2:
#         # print item + " 2"
#         if item in dict:
#             dict[item] = dict[item] + 1
#         else:
#             dict[item] = 1

#构建两个句子的词汇向量
# def get_vector():
#     vec1.clear()
#     vec2.clear()
#     for item in dict:
#         if item in result1:
#             vec1.append(dict[item])
#         else:
#             vec1.append(0)
#     for item in dict:
#         if item in result2:
#             vec2.append(dict[item])
#         else:
#             vec2.append(0)


#计算点积
def cal_product(vec1,vec2):
    res = 0
    for i in range(vec1.__len__()):
        res = res + vec1[i] * vec2[i]
    return res

#计算jaccard值
def cal_jaccard(dict,result1,result2):
    ans = 0
    union = len(dict)
    intersection = 0

    for item in dict:
        if item in result1 and item in result2:
            intersection = intersection + 1

    ans = (1.0*intersection)/union
    return ans

#计算余弦值
def cal_cos(vec1,vec2):
    up = 0
    down1 = 0
    down2 = 0
    for i in range(len(vec1)):
        up = up + vec1[i] * vec2[i]
        down1 = down1 + vec1[i] * vec1[i]
    for i in range(len(vec2)):
        down2 = down2 + vec2[i] * vec2[i]
    down = math.sqrt(down1) * math.sqrt(down2)
    ans = up/down
    return ans

#总函数
def solve(str1,str2):

    vec1 = []
    vec2 = []
    result1 = []
    result2 = []
    dict = {}

    seg_list1 = jieba.cut(str1, cut_all=True)
    seg_list2 = jieba.cut(str2, cut_all=True)

    # 对空格，换行符进行处理
    # result1.clear()

    for seg in seg_list1:
        seg = ''.join(seg.split())
        if seg != '' and seg != "\n" and seg != "\n\n":
            result1.append(seg)

    for item in result1:
        # print item + " 1"
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1

    # result2.clear()
    for seg in seg_list2:
        seg = ''.join(seg.split())
        if seg != '' and seg != "\n" and seg != "\n\n":
            result2.append(seg)

    for item in result2:
        # print item + " 2"
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1

    for item in dict:
        if item in result1:
            vec1.append(1)
        else:
            vec1.append(0)
    for item in dict:
        if item in result2:
            vec2.append(1)
        else:
            vec2.append(0)

    ans1 = cal_product(vec1,vec2)
    ans2 = cal_cos(vec1,vec2)
    ans3 = cal_jaccard(dict,result1,result2)
    return ans1,ans2,ans3
