from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
###################csv######################
import csv 

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file :
        fw = csv.writer(file) #fw - file write
        fw.writerow(datalist) #datalist = ['pen','pencil','erser']

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file :
        fr = csv.reader(file) #fw - file reader
        data = list(fr)
    return data
###################csv######################

GUI = Tk()
GUI.title('โปรแรกมบันทึกข้อมูล')
GUI.geometry('800x400')

# B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
# B1.pack(ipadx=20,ipady=20)

# def Button2():
#     text = 'ตอนนีมีเงินในบัญชี 300 บาท'
#     messagebox.showinfo('เงินในบัญชี',text)

# FB1 = Frame(GUI) #คล้ายกระดาน
# FB1.place(x=100,y=300)
# B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
# B2.pack(ipadx=20,ipady=20,padx=30,pady=30)
#B2.place(x=50,y=200)

###################SETION RIGHT######################
LF1 = ttk.LabelFrame(GUI,text='กรอกข้อมูลที่ต้องการเข้าไป')
LF1.place(x=300,y=100)

v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน GUI 
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana new',25))
E1.pack(pady=20,padx=20)

from datetime import datetime

def SaveData() :
    t =datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] #[เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง CSV 
    v_data.set('') #เคลียร์ข้อมูลที่อยูในช่องกรอก


B4 = ttk.Button(LF1,text='บันทึกข้อมูล',command=SaveData)
B4.pack(ipadx=20,ipady=20)

GUI.mainloop()



