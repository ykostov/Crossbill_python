# Copyright - Yasen Kostov, 2020
# Bratac.net
# https://github/ykostov
# 23 XI 20


import time

print ()
print ("Welcome to the Crossbill cypher. You are now in Crossbill - Text mode ")

time.sleep(2)

a = input("Type your Crossbill: ")

a_new = a.replace('31415', 'a').replace('32284', 'b').replace('62643', 'c').replace('41971', 'd').replace('69399', 'e').replace('94459', 'f').replace('239781', 'g').replace('86283', 'h').replace('48253', 'j').replace('14886', 'k').replace('51328', 'l').replace('46955', 'm').replace('58223', 'n').replace('79384', 'o').replace('23664', 'p').replace('67982', 'q').replace('42117', 'r').replace('62899', 's').replace('64628', 't').replace('82974', 'u').replace('37515', 'v').replace('95288', 'w').replace('38327', 'x').replace('58979', 'y').replace('92653', 'z').replace('0', ' ').replace('17253', 'i')

print ()
time.sleep(1)
print (a_new)
print()
