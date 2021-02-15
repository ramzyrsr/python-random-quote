# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:06:12 2021

@author: Zyrex
"""
import random

def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = len(quotes) - 1
  rnd = random.randint(0, last)

  print(quotes[rnd])

if __name__== "__main__":
  primary()
