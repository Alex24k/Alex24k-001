#!/usr/bin/env python3
#  线性表插入
list = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, None, None]


def insert(src, index, value):
    i = len(src)-1
    while i > index:
        list[i] = list[i-1]
        i = i-1
    list[index] = value
    return src


list1 = insert(list, 7, 8)
print(list1)
