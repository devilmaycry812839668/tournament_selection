#!/usr/bin/env python
#encoding:UTF-8

###列表比较 算子 CMP
### 第一位元素升序， 第二位元素降序
def mycmp(left, right):
    #left 位于列表左的元素， right列表右侧的元素
    a=left[1]
    b=right[1]

    if a[0]>b[0]:
        return 1
    elif a[0]<b[0]:
        return -1
    elif a[1]<b[1]:
        return 1
    elif a[1]>b[1]:
        return -1
    else:
        return 0

if __name__=="__main__":
    data=[(0, (0, 1)), (1, (1, 0)), (2, (1, 1))]
    data.sort(cmp=mycmp)
    print data
