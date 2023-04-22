from tkinter import *
from tkinter.ttk import Label
from tkinter import messagebox

firstNumber=SecondNumber=operator=Temp=None

#Taking the input from the buttons
def expression(b):
    temp=label['text']
    label['text']=label['text']+str(b)
    if labelUpper['text']=="Error":
        labelUpper['text']=str(b)
    else:
        labelUpper['text']+=str(b)

#Clearing the label text 
def clear():
    label['text']=""
    labelUpper['text']=""

def solve(op):
    global firstNumber,operator
    firstNumber=label['text']
    label['text']=""
    operator=op
    labelUpper['text']+=op

def showResult():
    global firstNumber,SecondNumber,operator
    if operator=='+':
        label['text']=str(int(label['text'])+int(firstNumber))
        labelUpper['text']=label['text']

    elif operator=='-':
        label['text']=str(int(firstNumber)-int(label['text']))
        labelUpper['text']=label['text']

    elif operator=='*':
        label['text']=str(int(label['text'])*int(firstNumber))
        labelUpper['text']=label['text']

    elif operator=='/' and label['text']=='0':
        firstNumber=SecondNumber=operator=None
        label['text']=''
        labelUpper['text']="Error"

    else:
        label['text']=str(int(firstNumber)//int(label['text']))
        labelUpper['text']=label['text']

# Root Window
root=Tk()
root.title("Calculator")
root.geometry("400x370")
root.resizable(False,FALSE)
root.configure(background='black')


# Label Widget
labelUpper = Label(root, text='',background='black',foreground='white')
labelUpper.grid(row=0,column=0,pady=(15,15),padx=(8,8),columnspan=5,sticky='e')
labelUpper.config(font=('verdana',16,'bold'))

label = Label(root, text='',background='black',foreground='white')
label.grid(row=1,column=0,pady=(15,15),columnspan=5)
label.config(font=('verdana',14,'bold'))

# Button Widgets
btn7=Button(root,text='7',background="#00a65a",fg='white',width=7,height=2,command=lambda : expression(7))
btn7.grid(row=2,column=0)
btn7.config(font=('verdana',14,'bold'))

btn8=Button(root,text='8',background="#00a65a",fg='white',width=7,height=2,command=lambda : expression(8))
btn8.grid(row=2,column=1)
btn8.config(font=('verdana',14,'bold'))

btn9=Button(root,text='9',background="#00a65a",fg='white',width=7,height=2,command=lambda : expression(9))
btn9.grid(row=2,column=2)
btn9.config(font=('verdana',14,'bold'))

btnDiv=Button(root,text='/',background="#f96d00",fg='white',width=7,height=2,command=lambda : solve('/'))
btnDiv.grid(row=2,column=3)
btnDiv.config(font=('verdana',14,'bold'))

btn4=Button(root,text='4',background="#00a65a",fg='white',width=7,height=2,command=lambda : expression(4))
btn4.grid(row=3,column=0)
btn4.config(font=('verdana',14,'bold'))

btn5=Button(root,text='5',background="#00a65a",fg='white',width=7,height=2,command=lambda : expression(5))
btn5.grid(row=3,column=1)
btn5.config(font=('verdana',14,'bold'))

btn6=Button(root,text='6',background="#00a65a",fg='white',width=7,height=2,command=lambda : expression(6))
btn6.grid(row=3,column=2)
btn6.config(font=('verdana',14,'bold'))

btnMul=Button(root,text='*',background="#f96d00",fg='white',width=7,height=2,command=lambda : solve('*'))
btnMul.grid(row=3,column=3)
btnMul.config(font=('verdana',14,'bold'))

btn1=Button(root,text='1',background="#00a65a",fg='white',width=7,height=2,command=lambda : expression(1))
btn1.grid(row=4,column=0)
btn1.config(font=('verdana',14,'bold'))

btn2=Button(root,text='2',background="#00a65a",fg='white',width=7,height=2,command=lambda : expression(2))
btn2.grid(row=4,column=1)
btn2.config(font=('verdana',14,'bold'))

btn3=Button(root,text='3',background="#00a65a",fg='white',width=7,height=2,command=lambda : expression(3))
btn3.grid(row=4,column=2)
btn3.config(font=('verdana',14,'bold'))

btnSub=Button(root,text='-',background="#f96d00",fg='white',width=7,height=2,command=lambda : solve('-'))
btnSub.grid(row=4,column=3)
btnSub.config(font=('verdana',14,'bold'))

btnC=Button(root,text='C',background="#155263",fg='white',width=7,height=2,command=lambda :clear())
btnC.grid(row=5,column=0)
btnC.config(font=('verdana',14,'bold'))

btn0=Button(root,text='0',background="#00a65a",fg='white',width=7,height=2,command=lambda : expression(0))
btn0.grid(row=5,column=1)
btn0.config(font=('verdana',14,'bold'))

btnEqual=Button(root,text='=',background="#ffc93c",fg='black',width=7,height=2,command=lambda : showResult())
btnEqual.grid(row=5,column=2)
btnEqual.config(font=('verdana',14,'bold'))

btnAdd=Button(root,text='+',background="#f96d00",fg='white',width=7,height=2,command=lambda : solve('+'))
btnAdd.grid(row=5,column=3)
btnAdd.config(font=('verdana',14,'bold'))


#mainloop 
root.mainloop()