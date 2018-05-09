# -*- coding: utf-8 -*-
import os
import sys
from operator import itemgetter

import jieba
from numpy import sort
from pip._vendor import chardet

reload(sys)
sys.setdefaultencoding('utf8')
#获取文件列表（该目录下放着100份文档）


#获取文件列表
def getFilelist(argv):
    path = argv
    filelist = []
    files = os.listdir(path)
    for f in files:
        if f[0]=='.':
            pass
        else:
            filelist.append(f)
    return filelist,path

def get_rank(str1):
    os.remove('templates/result.html')
    rank = []
    dict = {}
    # (allfile, path) = getFilelist('data/segfile')
    # 读取现有文档的词语并构建词典
    # for ff in allfile:
    #     result = []
    #     fname = 'data/segfile/' + ff
    #     f = open(fname,'r+')
    #     content = f.read()
    #     result = content.split(' ')
    #     for item in result:
    #         #print item
    #         if item in dict:
    #             pass
    #         else:
    #             dict[item] = 1
    #将输入的句子分词并加入现有字典
    str_list = jieba.cut(str1, cut_all=True, HMM=True)
    str_result = []
    for seg in str_list:
        seg = ''.join(seg.split())
        if seg != '' and seg != "\n" and seg != "\n\n":
            str_result.append(seg)
    strvec = []
    for item in str_result:
        #print item
        if item in dict:
            pass
        else:
            dict[item] = 1

    # for item in strvec:
    #     print item
    # 构建每个句子的向量
    (allfile2, path2) = getFilelist('data/uploads')

    for ff in allfile2:
        fname2 = 'data/uploads/' + ff
        f2 = open(fname2, 'r+')
        content1 = f2.read()
        type2 = chardet.detect(content1)
        content = content1.decode(type2["encoding"])
        sentence = content.split('。'or'？'or'！'or' ')
        for sen in sentence:
            result = jieba.cut(sen, cut_all=True, HMM=True)
            for item in result:
                if item in dict:
                    pass
                else:
                    dict[item] = 1

    for item in dict:
        # print item + "strvec"
        if item in str_result:
            # print "strvec 1"
            strvec.append(1)
        else:
            strvec.append(0)
    for ff in allfile2:
        fname2 = 'data/uploads/' + ff
        f2 = open(fname2, 'r+')
        content1 = f2.read()
        type2 = chardet.detect(content1)
        content = content1.decode(type2["encoding"])
        sentence = content.split('。'or'？'or'！')
        for sen in sentence:
            # print sen
            result = []
            vec = []
            # print item
            seg_list = jieba.cut(sen, cut_all=True, HMM=True)
            for seg in seg_list:
                seg = ''.join(seg.split())
                if seg != '' and seg != "\n" and seg != "\n\n":
                    result.append(seg)
            # for item in result:
            #     print "result + " + item

            for item in dict:
                # print item + "vec"
                if item in result:
                    # print "vec 1"
                    vec.append(1)
                else:
                    vec.append(0)
            ans = 0
            for i in range(len(dict)):
                # print str(i) + ":---"
                # print vec[i]
                # print strvec[i]
                ans = ans + vec[i] * strvec[i]
                # print ans
            list = [ff, ans, sen]
            rank.append(list)
    #根据文档向量和输入向量的內积对文档进行排序
    ranklist = sorted(rank, key=itemgetter(1), reverse=True)
    #构建结果的页面并显示
    f = open("templates/result.html", 'w+')
    i = 1
    for list in ranklist:
        if i > 100:
            break
        # print str(list[2]) + "     " + str(list[0]) + "   " + str(list[1])
        f.write("Rank  " + str(i) + ":    " + list[2] + "   (" + list[0].rstrip('-seg.txt') + ".txt)" + "<br>")
        i = i + 1
    f.close()
    f2.close()

#获取排名
# def get_rank(str1):
#
#     (allfile, path) = getFilelist('data/segfile')
#     #读取现有文档的词语并构建词典
#     for ff in allfile:
#         result = []
#         fname = 'data/segfile/' + ff
#         f = open(fname,'r+')
#         content = f.read()
#         result = content.split(' ')
#         for item in result:
#             #print item
#             if item in dict:
#                 pass
#             else:
#                 dict[item] = 1
#     #将输入的句子分词并加入现有字典
#     str_list = jieba.cut(str1, cut_all=True, HMM=True)
#     str_result = []
#     for seg in str_list:
#         seg = ''.join(seg.split())
#         if seg != '' and seg != "\n" and seg != "\n\n":
#             str_result.append(seg)
#     strvec = []
#     for item in str_result:
#         #print item
#         if item in dict:
#             pass
#         else:
#             dict[item] = 1
#     #构建每个文档的向量
#     for item in dict:
#         if item in str_result:
#             strvec.append(1)
#         else:
#             strvec.append(0)
#     # for item in strvec:
#     #     if item == 1:
#     #         print item
#     for ff in allfile:
#         result = []
#         vec = []
#         fname = 'data/segfile/' + ff
#         f = open(fname,'r+')
#         content = f.read()
#         result = content.split(' ')
#         # for item in result:
#         #     print item
#         for item in dict:
#             if item in result:
#                 # print item
#                 vec.append(1)
#             else:
#                 vec.append(0)
#         ans = 0
#         for i in range(len(vec)):
#             # print i
#             ans = ans + vec[i]*strvec[i]
#         list = [ff,ans]
#         # print ff + str(ans);
#         rank.append(list)
#     #根据文档向量和输入向量的內积对文档进行排序
#     ranklist = sorted(rank, key=itemgetter(1), reverse=True)
#     #构建结果的页面并显示
#     f = open("templates/result.html",'w+')
#     i = 1
#     for list in ranklist:
#         # print str(list[0]) + "   " + str(list[1])
#         f.write("Rank " + str(i) + ": " + list[0].rstrip('-seg.txt') + ".txt" + "<br>")
#         i = i + 1
#     f.close()
