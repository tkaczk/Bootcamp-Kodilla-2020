# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:21:26 2020

@author: tkacz
"""

items= [
        ['456_Longneck', 100000, 1000, 99], 
        ['454_Bier', 25000, 1000, 180], 
        ['155_Bordeaux', 50000, 1000, 150]
]

cost = [(item[1]*item[3])/1000 for item in items]

print(cost)
