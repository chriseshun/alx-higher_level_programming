#!/usr/bin/python3

for i in range(10):
    for u in range(i + 1, 10):
        print("{:d}{:d}".format(i, u),
              end=", " if i < 8 or u < 9 else "\n")
