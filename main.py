# Copyright - Yasen Kostov, 2020
# Bratac.net
# https://github/ykostov
# 23 XI 20


import time

print ()
print ("Welcome to the Crossbill cipher. You are now in Text - Crossbill mode ")
time.sleep(2)
print ()

string = input("Type something: ")

str_new = string.replace('a', '31415', ).replace('b', '32284').replace('c', '62643').replace('d', '41971').replace('e', '69399').replace('f', '94459').replace('g', '239781').replace('h', '86283').replace('j', '48253').replace('k', '14886').replace('l', '51328').replace('m', '46955').replace('n', '58223').replace('o', '79384').replace('p', '23664').replace('q', '67982').replace('r', '42117').replace('s', '62899').replace('t', '64628').replace('u', '82974').replace('v', '37515').replace('w', '95288').replace('x', '38327').replace('y', '58979').replace('z', '92653').replace(' ', '0').replace('i', '17253')

print()
time.sleep(1)

print(str_new)
print()
