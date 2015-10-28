#!usr/bin/env/python3
# coding: utf-8

import os
import argparse


def find(rash, path):
    
    print('rash:', rash)
    
    for f in os.listdir(path):
        
        if f.endswith(rash):
            
            for s, line in enumerate(open(path + "/"+ f)):
                
                    yield f, s, line
                    

def grep(gen,substr):
    for f, s ,line in gen:
        if substr in line:
            yield f, s, line


parser = argparse.ArgumentParser(description='PathRashSubstr')
parser.add_argument('path')
parser.add_argument('rash')
parser.add_argument('substr')

args = parser.parse_args()


for f, s, line in grep(find(args.rash, args.path), args.substr):
    print ("Файл", f, "строка №", s, line.strip())
