#!/usr/bin/env python3
import sys
if len(sys.argv) > 2:
    print('Parameter Error')
else:
    try:
        n = int(sys.argv[1])
    except:
        n = -1
    if n < 0:
        print('Parameter Error')
    elif n < 3500:
        print('0.00')
    else:
        n -= 3500
        if n <= 1500:
            sum = n * 0.03
        elif n <= 4500:
            sum = n * 0.1 - 105
        elif n <= 9000:
            sum = n * 0.2 - 555
        elif n <= 35000:
            sum = n * 0.25 -1005
        elif n <= 55000:
            sum = n * 0.3 - 2755
        elif n <= 80000:
            sum = n * 0.35 - 5505
        else:
            sum = n * 0.45 - 13505
        print('{:.2f}'.format(sum, ".2f"))
