#!/usr/bin/env python3

result = 0
start = 1
end = 100

def compute(start, result):
    while start <= end:
        result += start
        start += 1
    print(result)

if __name__ == '__main__':
    compute(start, result)

#!/usr/bin/env python3
result = 0
start = 1
end = 100

def compute1():
    global result 
    global start
    while start <= end:
        result += start
        start += 1
    print(result)

if __name__ == '__main__':
    compute1()