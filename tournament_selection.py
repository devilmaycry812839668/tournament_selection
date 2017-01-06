#!/usr/bin/env python
#encoding:UTF-8
import random
import numpy as np
from mycmp import mycmp

"""
        锦标赛方式选择, 选择出个体编号
        indicateValueDict {个体索引号：(Value1, Value2), } 
        key为索引号，从0开始。value为元组,一般不超过两个元素。

        indicateValueMatrix 矩阵
        [[个体索引号, Value1, Value2], ]

        selectNum  需要选择出的个体个数
        elementNum=2 默认为二元竞赛选择

        接口:
        tournament_selection(indicateValue, selectNum)
"""
def tournament_selection_Dict(indicateValueDict, selectNum, elementNum=2):
    #个体索引列表
    indicateList=range(len(indicateValueDict)) 
    #选择出的个体序号 列表
    remainIndicateList=[]

    #构建列表  [(索引号，(Value1, Value2)), ]
    indicateValueList=indicateValueDict.items()

    #对列表排序, 排序规则按个人需求定制,修改mycmp即可
    for i in xrange(selectNum):
        tempList=random.sample(indicateValueList, elementNum)
        tempList.sort(cmp=mycmp)

        bestIndicate=tempList[0][0]
        remainIndicateList.append(bestIndicate)
    ###返回选择的索引列表
    return remainIndicateList


def tournament_selection_Matrix(indicateValueMatrix, selectNum, elementNum=2):
    #个体索引列表
    indicateList=range(indicateValueMatrix.shape[0]) 
    #选择出的个体序号 列表
    remainIndicateList=[]

    for i in xrange(selectNum):
        tempList=random.sample(indicateList, elementNum)
        tempMatrix=indicateValueMatrix[tempList, ]

        tempMatrixToList=tempMatrix.tolist()
        tempMatrixToList=[(k[0], k[1:])for k in tempMatrixToList]
        tempMatrixToList.sort(mycmp)
        
        remainIndicateList.append(tempMatrixToList[0][0])
    return remainIndicateList


def tournament_selection_Dict2(indicateValueDict, selectNum, elementNum=2):
    #个体索引列表
    indicateList=range(len(indicateValueDict)) 
    #选择出的个体序号 列表
    remainIndicateList=[]

    #构建列表  [(索引号，(Value1, Value2)), ]
    indicateValueList=indicateValueDict.items()

    #对列表排序, 排序规则按个人需求定制,修改mycmp即可
    indicateValueList.sort(cmp=mycmp)

    for i in xrange(selectNum):
        tempList=[]
        tempList.extend(random.sample(indicateList, elementNum))
        bestIndicate=indicateValueList[min(tempList)][0]
        remainIndicateList.append(bestIndicate)
    ###返回选择的索引列表
    return remainIndicateList

def tournament_selection(indicateValue, selectNum, elementNum=2):
    if type(indicateValue)==dict:
        return tournament_selection_Dict(indicateValue, selectNum, elementNum)
    if type(indicateValue)==np.matrix:
        return tournament_selection_Matrix(indicateValue, selectNum, elementNum)


if __name__=="__main__":
    xN=20
    yN=3
    selectNum=10
    indicateValueDict={0:[1,2.1], 1:[1,2.2], 2:[1,2.3], 3:[1,2.4], 4:[1,2.5], 5:[1,2.6], 6:[1,2.7], 7:[1,2.8], 8:[1,2.9], 9:[1,3.0], 10:[0,2.1], 11:[0,2.2], 12:[0,2.3], 13:[0,2.4], 14:[0,2.5], 15:[0,2.6], 16:[0,2.7], 17:[0,2.8], 18:[0,2.9], 19:[0,3.0]}
    random.seed(0)
    print tournament_selection(indicateValueDict, selectNum)
    print '-'*50
    random.seed(0)
    print tournament_selection_Dict2(indicateValueDict, selectNum)
    print '-'*50
    indicateValueMatrix=np.matrix([[0, 1, 2.1], [1, 1, 2.2], [2, 1, 2.3], [3, 1, 2.4], [4, 1, 2.5], [5, 1, 2.6], [6, 1, 2.7], [7, 1, 2.8], [8, 1, 2.9], [9, 1, 3.0], [10, 0, 2.1], [11, 0, 2.2], [12, 0, 2.3], [13, 0, 2.4], [14, 0, 2.5], [15, 0, 2.6], [16, 0, 2.7], [17, 0, 2.8], [18, 0, 2.9], [19, 0, 3.0]])
    random.seed(0)
    print tournament_selection(indicateValueMatrix, selectNum)


