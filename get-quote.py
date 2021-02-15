# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:06:12 2021

@author: Zyrex
"""
def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])

if __name__== "__main__":
  primary()
