
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
    
'''Napišite program vjezba11_zd06.py koji crta deset koncentričnih kružnica, od kojih najveda ima radijus duljine 300 piksela, a svaka iduda ima radijus za 10% manji od prethodne. Svaka kružnica mora biti ispunjena jednom nijansom sive boje, pri čemu najveda kružnica mora biti ispunjena bijelom bojom, a svaka iduda za 5% tamnijom nijansom sive boje od prethodne.'''
