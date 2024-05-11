class Rabbit:
  __age = 0
  def __init__(self):
    Rabbit.__age += 1
  @classmethod
  def printage(self):
    self.__age = 9
    print(self.__age)

r1 = Rabbit()
r2 = Rabbit()
r3 = Rabbit()
print(r1.printage())


import tkinter as tk           # tkinter
import tkinter.messagebox as tkm
root = tk.Tk()                  # 창 만들기
root.title("tkinter test")      # 창의 머리말
root.geometry("400x200+400+200")  # 창의 크기/위지 (_x_+_+_, x크기 x y크기 + x위치 + y위치)
root.resizable(width=False,height=True)   # 창크기 변경 가능여부

lbl = tk.Label(root,text="Hello world",font="맑은고딕",fg="green",bg="red") # Label
lbl.pack()

def myBtn():
  tkm.showinfo("message box","Button이 클릭되었습니다.")

btn = tk.Button(root,text="button click",command=myBtn)
btn.pack()

def mychkbtn():
  tkm.showinfo("message box","chkbutton : " + str(var1.get()) + "," + str(var2.get()) + "," + str(var3.get()))
var1,var2,var3 = tk.IntVar(), tk.IntVar(), tk.IntVar()   # 위젯과 연결된 정수형 변수 선언
chkbtn1 = tk.Checkbutton(root,text="사과",variable=var1, command=mychkbtn)
chkbtn2 = tk.Checkbutton(root,text="포도",variable=var2, command=mychkbtn)
chkbtn3 = tk.Checkbutton(root,text="귤",variable=var3, command=mychkbtn)
chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()

def myrdobtn():
  tkm.showinfo("message box","rdobutton : " + str(myvar.get()))
myvar = tk.IntVar()   # 위젯과 연결된 정수형 변수 선언
rdobtn1 = tk.Radiobutton(root,text="현대",variable=myvar,value=1, command=myrdobtn)
rdobtn2 = tk.Radiobutton(root,text="기아",variable=myvar,value=2, command=myrdobtn)
rdobtn3 = tk.Radiobutton(root,text="르노",variable=myvar,value=3, command=myrdobtn)
rdobtn1.pack()
rdobtn2.pack()
rdobtn3.pack()

#rdobtn = tk.Radiobutton(root,test="사과")
#rdobtn.pack()

root.mainloop()