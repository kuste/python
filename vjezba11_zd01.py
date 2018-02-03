#Ivica Kustura
#vjezba11 zad 1

from turtle import *

reset()

speed(0)

pu()

goto(-200,-200)

pd()
vrhovi='ABCD'
pensize(2)
for i in vrhovi:
    write(i, align= 'left', font=('Arial', 12,'bold'))
    fd(400)
    lt(90)


goto(200,200)
bk(400)
goto(200,-200)



pu()

mainloop()
