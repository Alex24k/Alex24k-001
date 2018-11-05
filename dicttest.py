#!/usr/bin/env python3
import sys
for arg in sys.argv[1:]:
    str1 = str(arg)
    list = str1.split(':')
    print('ID:{} Name:{}'.format(list[0],list[1]))
