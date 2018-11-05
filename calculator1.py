#!/usr/bin/env python3


import sys


def income(salary):
    insurance = salary * 0.165
    tax = salary - insurance - 3500
    if tax < 0:
        i = salary - insurance
    elif tax <= 1500:
        tax = tax * 0.03 - 0
        i = salary - insurance - tax
    elif tax <= 4500:
        tax = tax * 0.10 - 105
        i = salary - insurance - tax
    elif tax <= 9000:
        tax = tax * 0.20 - 555
        i = salary - insurance - tax
    elif tax <= 35000:
        tax = tax * 0.25 - 1005
        i = salary - insurance - tax
    elif tax <= 55000:
        tax = tax * 0.30 - 2755
        i = salary - insurance - tax
    elif tax <= 80000:
        tax = tax * 0.35 - 5505
        i = salary - insurance - tax
    else:
        tax = tax * 0.45 - 13505
        i = salary - insurance - tax
    return i

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Paramter Error')
    else:
        for arg in sys.argv[1:]:
            list = arg.split(":")
            try:
                salary = int(list[1])
                if salary < 0:
                    print('Paramter Error')
                else:
                    dict = {list[0]:income(salary)}
                    for k, v in dict.items():
                        print('{}:{:.2f}'.format(k, v))
            except ValueError:
                print('Paramter Error')