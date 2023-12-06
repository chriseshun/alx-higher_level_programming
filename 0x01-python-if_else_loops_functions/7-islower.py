#!/usr/bin/python3

def islower(c):

    return ord('a') <= ord(c) <= ord('z')


character = ['a', 'H', 'A', '3', 'g']


for char in character:

    if islower(char):
        print("{} is lower".format(char))
    else:
        print("{} is upper".format(char))
