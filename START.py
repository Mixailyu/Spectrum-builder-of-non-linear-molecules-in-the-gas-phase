# -*- coding: utf-8 -*- 
"""
Created on Thu Feb 17 09:31:42 2022

@author: user
"""

from tkinter import *
import tkinter
from tkinter import ttk
from Menu_function import *
from tkinter import messagebox
from tkinter import filedialog


    
TAB_LIST_CLASS={}  
    
root=Tk()
# tkinter.ttk
root.title("Программа")
root.geometry('1220x800')
root.resizable(width=True, height=True)
root.iconbitmap('logo.ico')

#Вкладки
tab_control=ttk.Notebook(root)
tab_control.pack(expand=1, fill="both")
 
#Меню 
my_menu=Menu(root)
root.config(menu=my_menu) 
file_menu= Menu(my_menu)
my_menu.add_cascade(label="Файл",menu=file_menu)
file_menu.add_command(label="Открыть ...",command=lambda tab_control=tab_control,TAB_LIST_CLASS=TAB_LIST_CLASS:openFile(tab_control,TAB_LIST_CLASS))
file_menu.add_command(label="Создать новую вкладку ",command=lambda root=root, tab_control=tab_control, TAB_LIST_CLASS=TAB_LIST_CLASS:Ask_Window(root,tab_control,TAB_LIST_CLASS))
file_menu.add_command(label="Закрыть текущюю вкладку",command=lambda tab_control=tab_control,TAB_LIST_CLASS=TAB_LIST_CLASS: deletetab(tab_control,TAB_LIST_CLASS))
file_menu.add_command(label="Сохранить как ...",command=lambda tab_control=tab_control,TAB_LIST_CLASS=TAB_LIST_CLASS: save_as(tab_control,TAB_LIST_CLASS))
file_menu.add_command(label="Закрыть программу",command=root.destroy)

root.mainloop()