import tkinter as tk

calculation=""


def add_to_calculation(symbol) :
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    
    global calculation
    try:
        
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
           clear_feild()
           text_result.insert(1.0,"Error")
          
def clear_feild():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")

     
root=tk.Tk()
root.title('Runzon2024 RZ-812.A')
root.geometry("346x435")
root.resizable(0,0)
root.configure(background='dark green')
text_result=tk.Text(root,height='1', width='15', font=("Algerian",'18'),background="grey" ,fg="black")
text_result.grid(columnspan='5')

btn_1=tk.Button(root,text='1',command=lambda:add_to_calculation(1),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_1.grid(row=2,column=1)
btn_2=tk.Button(root,text='2',command=lambda:add_to_calculation(2),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_2.grid(row=2,column=2)
btn_3=tk.Button(root,text='3',command=lambda:add_to_calculation(3),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_3.grid(row=2,column=3)
btn_4=tk.Button(root,text='4',command=lambda:add_to_calculation(4),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_4.grid(row=3,column=1)
btn_5=tk.Button(root,text='5',command=lambda:add_to_calculation(5),font=("Times New Romans",'18'),width=2,background="white",fg="black")
btn_5.grid(row=3,column=2)
btn_6=tk.Button(root,text='6',command=lambda:add_to_calculation(6),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_6.grid(row=3,column=3)
btn_7=tk.Button(root,text='7',command=lambda:add_to_calculation(7),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_7.grid(row=4,column=1)
btn_8=tk.Button(root,text='8',command=lambda:add_to_calculation(8),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_8.grid(row=4,column=2)
btn_9=tk.Button(root,text='9',command=lambda:add_to_calculation(9),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_9.grid(row=4,column=3)
btn_0=tk.Button(root,text='0',command=lambda:add_to_calculation(0),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_0.grid(row=5,column=2)
btn_plus=tk.Button(root,text='+',command=lambda:add_to_calculation("+"),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_plus.grid(row=2,column=4)          
btn_minus=tk.Button(root,text='-',command=lambda:add_to_calculation("-"),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_minus.grid(row=3,column=4)
btn_multiplication=tk.Button(root,text='*',command=lambda:add_to_calculation("*"),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_multiplication.grid(row=4,column=4)
btn_division=tk.Button(root,text='/',command=lambda:add_to_calculation("/"),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_division.grid(row=5,column=4)
btn_open=tk.Button(root,text='(',command=lambda:add_to_calculation("("),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_open.grid(row=5,column=1)
btn_close=tk.Button(root,text=')',command=lambda:add_to_calculation(")"),font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_close.grid(row=5,column=3)
btn_equals=tk.Button(root,text='=',command=evaluate_calculation,font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_equals.grid(row=6,column=4)
btn_clear=tk.Button(root,text='AC',command=clear_feild,font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_clear.grid(row=6,column=1)
btn_C=tk.Button(root,text='C',command=clear_feild,font=("Times New Romans",'18'),width=2,background="white" ,fg="black")
btn_C.grid(row=6,column=2)
btn_percent=tk.Button(root,text='%',command=lambda:add_to_calculation("%"),font=("Times New Romans",'18'),width=2,background="white",fg="black")
btn_percent.grid(row=6,column=3)
root.mainloop()    