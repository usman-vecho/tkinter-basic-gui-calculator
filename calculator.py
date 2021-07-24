from math import sin as a
from tkinter import *
root=Tk()
root.minsize(height='500',width='450')
root.maxsize(height='500',width='500')
operator=""
def equal():
    global operator
    sumup=str(eval(operator))
    textinput.set(sumup)
def input(numbers):
    global operator
    operator=operator+str(numbers)
    textinput.set(operator)

def clear():
    global operator
    operator=""
    textinput.set(operator)

textinput=StringVar()
root.title("calc")
textDisplay=Entry(root,font=('ariel',30,'bold'),textvariable=textinput,bd=20 , insertwidth=10 ,bg="powder blue",justify = 'right').grid(columnspan=4)
btn1=Button(root,padx=33, font=('bold',24,'bold'),command=lambda : input(1),text='1',bg="red").grid(row=1,column=0)
btn2=Button(root,padx=36,font=('bold',24,'bold'),command=lambda : input(2),text='2',bg="red").grid(row=1,column=1)
btn3=Button(root,padx=33,font=('bold',24,'bold'),command=lambda : input(3),text='3',bg="red").grid(row=1,column=2)
btn4=Button(root,padx=33,font=('bold',24,'bold'),command=lambda : input(4),text='4',bg="red").grid(row=2,column=0)
btn5=Button(root,padx=36,font=('bold',24,'bold'),command=lambda : input(5),text='5',bg="red").grid(row=2,column=1)
btn6=Button(root,padx=33,font=('bold',24,'bold'),command=lambda : input(6),text='6',bg="red").grid(row=2,column=2)
btn7=Button(root,padx=33,font=('bold',24,'bold'),command=lambda : input(7),text='7',bg="red").grid(row=3,column=0)
btn8=Button(root,padx=36,font=('bold',24,'bold'),command=lambda : input(8),text='8',bg="red").grid(row=3,column=1)
btn13=Button(root,padx=33,font=('bold',24,'bold'),command=lambda : input(9),text='9',bg="red").grid(row=3,column=2)
btn9=Button(root,padx=33,font=('bold',24,'bold'),command=lambda : input('+'),text='+',bg="red").grid(row=1,column=3)
btn10=Button(root,padx=33,font=('bold',28,'bold'),command=lambda : input('-'),text='-',bg="red").grid(row=2,column=3)
btn11=Button(root,padx=33,font=('bold',28,'bold'),command=lambda : input('*'),text='*',bg="red").grid(row=3,column=3)
btn12=Button(root,padx=33,font=('bold',26,'bold'),command=lambda : equal(),text='=',bg="red").grid(row=4,column=3)
btn14=Button(root,padx=38,font=('bold',24,'bold'),command=lambda : input('/'),text='/',bg="red").grid(row=4,column=1)
btn15=Button(root,padx=33,font=('bold',24,'bold'),command=lambda : input('.'),text='.',bg="red").grid(row=4,column=0)
btn16=Button(root,padx=33,font=('bold',24,'bold'),command=lambda : input(0),text='0',bg="red").grid(row=4,column=2)
btn17=Button(root,padx=20,font=('bold',26,'bold'),text='sin',bg="red").grid(row=5,column=3)
btn18=Button(root,padx=33,font=('bold',24,'bold'),command=lambda : input('('),text='(',bg="red").grid(row=5,column=0)
btn19=Button(root,padx=36,font=('bold',24,'bold'),command=lambda : input(')'),text=')',bg="red").grid(row=5,column=1)
btn18=Button(root,padx=33,font=('bold',24,'bold'),command=lambda : clear(),text='c',bg="red").grid(row=5,column=2)
root.mainloop()
