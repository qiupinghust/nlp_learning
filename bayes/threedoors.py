# -*- coding: utf-8 -*-
"""
bayes公式
"""

#coding:utf-8
from random import sample,randint
mylist = ["goat","car","goat"]

def stay(choice):
    data = sample(mylist, 3)
    if data[choice]=="car":
        return "win"
    else:
        return "false"

def change(choice):
    data = sample(mylist, 3)
    choose = data[choice]
    data.remove(choose)
    data.remove("goat")
    if data==["car"]:
        return "win"
    else:
        return "false"

if __name__=='__main__':
    stay_count = 0
    stay_win = 0
    change_count = 0 
    change_win = 0

    s = 0
    while s<=1000000:
        s = s + 1
        choice = randint(0,2)
        change_flag = randint(0,1)
        if change_flag==0:
            stay_count = stay_count + 1
            if stay(choice)=="win":
                stay_win = stay_win + 1
        else:
            change_count = change_count + 1
            if change(choice)=="win":
                change_win = change_win + 1
    stay =  stay_win/stay_count    
    change = change_win/change_count       
    print("不换的概率是:%f" %stay )  
    print("换的概率是:%f" % change)        