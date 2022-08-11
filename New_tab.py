# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:31:55 2022

@author: user
"""

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

from apendix import *
from collections import Counter
from importlib import reload
from math import factorial
from sympy import sqrt, prod

import matplotlib
matplotlib.use("Agg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
  

class SKROLLBAR:

    def __init__(self, fraim):
        self.canvas= Canvas(fraim)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.scrollbar=ttk.Scrollbar(fraim, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion= self.canvas.bbox("all")))
        self.work_frame = Frame(self.canvas)
        self.canvas.create_window((1,1), window=self.work_frame, anchor="nw")  
    
def batton_list_for_skrolbar(frame,DICT,ZAMENA, SIMBOL):
    r=0
    
    Subscripts_dikt_simbol_utf={0:'\u2080',1:'\u2081',2:'\u2082',3:'\u2083',4:'\u2084',5:'\u2085',6:'\u2086',7:'\u2087',8:'\u2088',9:'\u2089','omega':'\u03C9','fi':'\u03C6','-':'\u207B','A':'\u1D43','k':'k','D':'\u1D48'}
    label_list=list(DICT.keys())
    for j in range(len(label_list)):
        i=label_list[j]
        Value=StringVar(value=str(DICT[i]))
        LABEL=str(i)
        LBS=LABEL.split('_')
        UTF_numb=','.join([''.join([Subscripts_dikt_simbol_utf[int(k)] ]) for k in [VECTOR_INDEX_MAP[k] for k in LBS[1]]])#создаём нижние индексы из  iii получим 111 подстрочное
        VIM=list(dict(Counter([VECTOR_INDEX_MAP[k] for k in LBS[1]if k!='0'])).values())# создаём список в которов указывается число повторений уникальных элементов из списка VIM т.е. iijjj==[1,1,2,2,2] это [2,3]
        TEXT=Subscripts_dikt_simbol_utf[SIMBOL]+UTF_numb
        if SIMBOL=='omega':VIM=''
        if SIMBOL=="D":Z='Д'
        else:Z='CM'+'\u207B'+'\u00B9'
        Label(frame, text=Z, font=("Arial Bold", 15)).grid(column=2,row=r)
        Label(frame, text=str(DICT[i]), font=("Arial Bold", 15)).grid(column=1,row=r)
        Button(frame,text=TEXT,font=("Arial Bold", 15),width=10, command=lambda text=TEXT, key=i,r=r,Dict=DICT, tab=frame, vim=VIM,Z=Z,ZAMENA=ZAMENA,SIMBOL=SIMBOL:Window1(text,key,r,Dict,tab,vim,Z,ZAMENA,SIMBOL)).grid(column=0,row=r, pady=10,padx=10) 
        r+=1
        
def Window1(Text,key,r,DICT,tab,VIM,Z,ZAMENA,SIMBOL):
    NW=Toplevel(tab)
    NW.title(Text)
    NW.resizable(0,0)
    Value=StringVar(value=str(DICT[key]))
    Label(NW, text='Введите новое значение для '+Text, font=("Arial Bold", 15)).grid(column=1,row=0)
    Label(NW, text=Z, font=("Arial Bold", 15)).grid(column=1,row=1)
    en=Entry(NW,width=15, textvariable=Value)
    en.grid(column=0,row=1)
    Button(NW,text='OK',font=("Arial Bold", 15), command=lambda key=key,r=r,DICT=DICT,tab=tab,ZAMENA=ZAMENA,SIMBOL=SIMBOL:Window1_OK(key,r,DICT,tab,ZAMENA,SIMBOL)).grid(column=0,row=2)

    def Window1_OK(key,r,DICT,tab,ZAMENA,SIMBOL):
        N='0123456789+-*/.'
        for i in en.get():
            if not (i in N):
                messagebox.showerror("Ошибка!","Вы ввели букву или не коректный символ\n используйте символы\n0,1,2,3,4,5,6,7,8,9,+,-,*,/,.")
                break
                
        try:
            rez=eval(en.get())
            Label(tab, text=str(rez), font=("Arial Bold", 15)).grid(column=1,row=r)
            if SIMBOL=='omega' or SIMBOL=='A':
                ZAMENA[key]=rez
            if SIMBOL=='k':
                ZAMENA[key]=round(rez*2**(-sum(VIM)/2),3)
            if SIMBOL=='fi' or SIMBOL=='D': 
                ZAMENA[key]=round(rez*2**(-sum(VIM)/2),3)/prod([factorial(i) for i in VIM])
            DICT[key]=rez
            NW.destroy()
        
        except: 
            messagebox.showerror("Ошибка!","Проверьте правильность вводимых данных")

def up_table(stay1,stay2,RR,const,flag=False):
    print(flag)
    N='0123456789,'
    def dipol(st1,st2,const):
        if len([i for i in list(const.const_dipol_dikt.values()) if i!=0])==0: return 0.001
        DIPOL=RR.MEDMF(st1,st2,const.max_indignation_step)
        return DIPOL.subs(list(const.ZAMENA.items()))
    
    for i in stay1.get()+stay2.get():
        if not (i in N):
            messagebox.showerror("Ошибка!","Вы ввели букву или не коректный символ\n используйте символы\n0,1,2,3,4,5,6,7,8,9\n разделитель запятая!")
            return
            break
    if const.number_of_vibrational_degrees!=len(stay1.get().split(',')) or const.number_of_vibrational_degrees!=len(stay2.get().split(',')):
        messagebox.showerror("Ошибка!",f"Проверьте введенные вами состояния! число колебательных степеней свободы должно быть равно {const.number_of_vibrational_degrees}")
    st1=[int(i) for i in stay1.get().split(',')]
    st2=[int(i) for i in stay2.get().split(',')]
    E1=0
    E2=0
    Z=list(const.ZAMENA.items())
    if flag:
        st0=[0 for i in stay1.get().split(',')]
        Dipol={}
        result=RR.Resonance([st1,st2],list(const.ZAMENA.items()))
        Dipol[tuple(st1)]=dipol(st0,st1,const)
        Dipol[tuple(st2)]=dipol(st0,st2,const)
        for i in Dipol.keys():
            const.table.insert('', END, values=(f'{str(st0)[1:-1]} ->{str(i)[1:-1]}',f"{round(result[i],4)}",f"{round(Dipol[i],7)*1000}"))
    if flag==False:
        for i in range(const.max_indignation_step+1):
            A=RR.AE(st1,st1,i)
            B=RR.AE(st2,st2,i)
            E1+=A
            E2+=B
        delta_E=E2.subs(Z)-E1.subs(Z)
        Dipol=dipol(st1,st2,const)
        const.table.insert('', END, values=(f'{stay1.get()} ->{stay2.get()}',f"{round(delta_E,4)}",f"{round(Dipol,7)*1000}"))
    stay1.delete(0,END)
    stay2.delete(0,END)

def remove_selected(self):
    x=self.table.selection()
    for i in x:
        self.table.delete(i)
        if self.Line!=[]:
            self.Line=[j for j in self.Line if not(i in j)]
    PLOT(self)

def PLOT(self):
    f=Figure(figsize=(8,2.5), dpi=100)
    a=f.add_subplot(111)
    a.grid()
    for i in self.Line:
        print(i)
        x=[float(i[1]),float(i[1])]
        y=[0,float(i[2])**2]
        a.plot(x,y,'b')
    canvas=FigureCanvasTkAgg(f,self.fraim_plot)
    canvas.get_tk_widget().grid(row=0, column=0)           

def PLOT_all(self):
    self.Line=[[line]+self.table.item(line)['values'][1:] for line in self.table.get_children() ]
    PLOT(self)  

def PLOT_select(self):
    self.Line+=[[line]+self.table.item(line)['values'][1:] for line in self.table.selection() ]
    PLOT(self)

class New_tab:
    def __init__(self, master):
        import const as const
        import Recurrence_Relations as RR
        const=reload(const)
        self.title = const.title
        self.TYPE_ANGARMONIC_CONST=const.TYPE_ANGARMONIC_CONST
        self.const_omega_dikt=const.const_omega_dikt
        self.const_angarmonik_dikt=const.const_angarmonik_dikt
        self.const_dipol_dikt=const.const_dipol_dikt
        self.const_n_dikt=const.const_n_dikt
        self.ZAMENA=const.ZAMENA
        self.max_indignation_step=const.max_indignation_step
        self.number_of_vibrational_degrees=const.number_of_vibrational_degrees
        self.tab = ttk.Frame(master)
        self.LIST=const.DATA_TABEL
        self.Line=[]

        master.grid_columnconfigure(0,minsize=200)
        
        fraim1= Frame(self.tab, width=50,highlightbackground="red", highlightthickness=3)
        fraim1.grid(column=0, row=0)
        SB=SKROLLBAR(fraim1)
        batton_list_for_skrolbar(SB.work_frame,self.const_omega_dikt,self.ZAMENA, "omega")
        
        fraim2= Frame(self.tab, width=50,highlightbackground="blue", highlightthickness=3)
        fraim2.grid(column=1, row=0)
        SB2=SKROLLBAR(fraim2)
        batton_list_for_skrolbar(SB2.work_frame, self.const_angarmonik_dikt,self.ZAMENA, self.TYPE_ANGARMONIC_CONST)
        
        fraim3= Frame(self.tab, width=50,highlightbackground="green", highlightthickness=3)
        fraim3.grid(column=2, row=0)
        SB3=SKROLLBAR(fraim3)
        batton_list_for_skrolbar(SB3.work_frame, self.const_dipol_dikt,self.ZAMENA, 'D')
        
        fraim4= Frame(self.tab, width=100,highlightbackground="black", highlightthickness=3)
        fraim4.grid(column=0, row=1, columnspan=2,sticky="we")
        
        heads=['Переход',"Эергия", "матричный элемент (m|d|n)*1000"]
        self.table=ttk.Treeview(fraim4,show='headings')
        self.table['columns']=heads
        for header in heads:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header,anchor='center')
        scroll_pane=ttk.Scrollbar(fraim4, command=self.table.yview)
        scroll_pane.pack(side=RIGHT,fill=Y)
        self.table.configure(yscrollcommand=scroll_pane.set)
        self.table.pack(expand=YES, fill=BOTH)
        for row in self.LIST:
            self.table.insert('', END, values=row)
        
        fraim5= Frame(self.tab,highlightbackground="green", highlightthickness=3)
        fraim5.grid(column=2, row=1,rowspan=2,sticky="nswe")
        
        stay1=Entry(fraim5,width=15)
        stay1.grid(column=0,row=1)
        stay2=Entry(fraim5,width=15)
        stay2.grid(column=1,row=1)
        bt=ttk.Button(fraim5,text='старт', command=lambda st1=stay1,st2=stay2,self=self,RR=RR:up_table(st1,st2,RR,self))
        bt.grid(column=2,row=1)
        bt2=ttk.Button(fraim5,text='Удалить выделенные строки', command=lambda self=self:remove_selected(self))
        bt2.grid(column=0,row=8,columnspan=3)
        bt3=ttk.Button(fraim5,text='Построить график', command=lambda self=self:PLOT_all(self))
        bt3.grid(column=1,row=4,columnspan=3)
        bt4=ttk.Button(fraim5,text='Построить график по выделенным строкам', command=lambda self=self:PLOT_select(self))
        bt4.grid(column=1,row=5,columnspan=3)
        
        bt5=ttk.Button(fraim5,text='Резонанс', command=lambda st1=stay1,st2=stay2,self=self,RR=RR:up_table(st1,st2,RR,self,True))
        bt5.grid(column=3,row=1,columnspan=3)
        
        
        
        self.fraim_plot=Frame(self.tab,highlightbackground="green", highlightthickness=3)
        self.fraim_plot.grid(column=0, row=2,columnspan=2,sticky="we")

        
        master.add(self.tab, text="Расчет молекулы "+self.title)
    