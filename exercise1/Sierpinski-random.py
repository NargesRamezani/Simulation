import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def f1 (x,y):
    x=x/2
    y=y/2
    return(x,y)

def f2(x,y):
    x=x/2 + 0.5
    y=y/2+1
    return (x ,y)

def f3 (x ,y):
    x=x/2 +1 
    y= y/2
    return(x,y)

functions=[f1 , f2 , f3]
points=[]