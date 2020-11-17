# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:10:28 2020

@author: tkacz
"""
items= [
        ['456_Longneck', 100000, 1000, 99.00], 
        ['454_Bier', 25000, 1000, 180.00], 
        ['155_Bordeaux', 50000, 1000, 150.00]
]

def get_cost():
    wares_cost = [(item[1]*item[3])/item[2] for item in items]
    print(wares_cost)
get_cost()



'''def get_items():
    ware = 'Article'
    qnt = 'Quantity'
    unit = 'Unit'
    price = 'Price'
    
    print('| {:^15}| {:^9}| {:^6}| {:^7} |' .format(ware, qnt, unit, price))
    print('-'*(17+11+8+11))
    for i in items:
        print('|', i[0],' '* (13-len(i[0])),'|', i[1], ' '*(7-len(str(i[1]))) \
,'|', i[2],' '*(4-len(str(i[2]))),'|', i[3],' '*(6-len(str(i[3]))), '|' )'''