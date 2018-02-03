#Ivica Kustura
#vjezba11 zad 6


from turtle import *
reset()
ht()
speed(0)

start = 300

for i in range(10):
    pu()
    goto(0,-start)
    pd()
    r=1.0-i*0.05
    
    
    fillcolor(r,r,r)
    begin_fill()
    
    circle(start)
    end_fill()
    start*=0.9    
    
