#!/usr/bin/env python3

import sys

output_dict = {}

def handle_data(a):        
    a1, a2 = a.split(":")
    output_dict[a1]= a2

def print_data(a, b):
    print('ID:', a, ' Name:', b)
    
if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key, output_dict[key])