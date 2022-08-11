# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:02:00 2022

@author: user
"""
from tkinter import *
from tkinter import filedialog
import shutil
from tkinter import ttk
from New_tab import *
from constant_gen import constant_gen

def Test():
    pass

def openFile(tab_control,TAB_LIST_CLASS):
    filepath=filedialog.askopenfilename()
    shutil.copyfile(filepath, r'const.py')
    A=New_tab(tab_control)
    TAB_LIST_CLASS[A.tab]=A
      
def deletetab(tab_control,TAB_LIST_CLASS):
    for item in tab_control.winfo_children():
        if str(item) == (tab_control.select()):
              del TAB_LIST_CLASS[item]
              item.destroy()
              return   
    
def Ask_Window(root,tab_control,TAB_LIST_CLASS):
    NW=Toplevel(root)
    NW.title('Новый рассчет')
    NW.resizable(0,0)
    Label(NW, text="Введите формулу исследуемой молекулы", font=("Arial Bold", 15)).grid(column=0, row=0)
    Title = Entry(NW,width=10)
    Title.grid(column=1, row=0)
    
    Label(NW, text="Введите число колебательных степеней свободы в исследуемой молекуле N=", font=("Arial Bold", 15)).grid(column=0, row=1)
    N = Entry(NW,width=10)
    N.grid(column=1, row=1)
    

    Label(NW, text="Укажите до какого порядка возмущения вы желаете произвести расчет", font=("Arial Bold", 15)).grid(column=0, row=2)
    M = Entry(NW,width=10)
    M.grid(column=1, row=2)

    Label(NW, text="Укажите какого формата ангармонические постоянные вы используете:", font=("Arial Bold", 15)).grid(column=0, row=3)
    A_var=StringVar()
    Radiobutton(NW,text='k',variable=A_var,value='k').grid(column=1, row=3)
    Radiobutton(NW,text='\u03C6',variable=A_var,value='fi').grid(column=2, row=3)
    Radiobutton(NW,text='a',variable=A_var,value='A').grid(column=3, row=3)

    Button(NW, text="Далее",command=lambda tab_control=tab_control, NW=NW:bild_new_tab(tab_control,NW,TAB_LIST_CLASS)).grid(column=4, row=5)
    
    def bild_new_tab(tab_control,NW,TAB_LIST_CLASS):
        title=Title.get()
        number_of_vibrational_degrees=int(N.get())
        max_indignation_step=int(M.get())
        TYPE_ANGARMONIC_CONST=A_var.get()
        constant_gen(number_of_vibrational_degrees, max_indignation_step, TYPE_ANGARMONIC_CONST,title)
        A=New_tab(tab_control)
        TAB_LIST_CLASS[A.tab]=A
        NW.destroy()
   
def save_as(tab_control,TAB_LIST_CLASS):
    
    const=None
    for item in tab_control.winfo_children():
        if str(item) == (tab_control.select()):
            const=TAB_LIST_CLASS[item]
            
    file=filedialog.asksaveasfile(mode='w',defaultextension='.py')
    
    constant_gen(const.number_of_vibrational_degrees, const.max_indignation_step, const.TYPE_ANGARMONIC_CONST,const.title)      
    RID=open('const.py','r')
    S=[i for i in RID if not('const' in i or 'ZAMENA' in i or 'DATA' in i)]# if not('ZAMENA' in i)  if not('DATA' in i)]
    RID.close()
    for i in S: file.write(i)
    
    file.write(f'const_n_dikt={const.const_n_dikt}\n')
    
    file.write(f'const_omega_dikt={const.const_omega_dikt}\n')
    
    file.write(f'const_angarmonik_dikt={const.const_angarmonik_dikt}\n')
    
    file.write(f'const_dipol_dikt={const.const_dipol_dikt}\n')
    
    file.write(f'ZAMENA={const.ZAMENA}\n')
    file.write(f"DATA_TABEL={[const.table.item(line)['values'] for line in const.table.get_children()]}\n")
    file.close