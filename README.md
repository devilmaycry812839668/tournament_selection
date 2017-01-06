本程序是遗传算法中的锦标赛选择法

输入：        
indicateValue
可以为np.matrix 也可以为dict
格式基本为 个体索引号,Value1,Value2,...
具体参见程序内部的测试用例

selectNum
保留到下一代的个体个数

elementNum=2
几元锦标赛选择方式，默认为2


输出：
     选择出个体编号, 列表


"""
        indicateValueDict {个体索引号：(Value1, Value2), } 
        key为索引号，从0开始。value为元组,一般不超过两个元素。

        indicateValueMatrix 矩阵
        [[个体索引号, Value1, Value2], ]

        selectNum  需要选择出的个体个数
        elementNum=2 默认为二元竞赛选择

        接口:
        tournament_selection(indicateValue, selectNum, elementNum=2)
"""


