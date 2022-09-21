# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 22:22:26 2022

@author: juanr_axzldpc
"""

from tkinter import *
import re
class aplicacion():
    def __init__(self):
        self.raiz=Tk()
        self.raiz.geometry('600x400')
        self.raiz.resizable(width=False,height=False)
        self.raiz.title('Expresiones Regulares')
        label=Label(self.raiz,text="Validacion de IPs")
        label.pack(side=TOP)

        self.textos=Frame(self.raiz)
        self.textos.pack(side=TOP)
        self.frameDeAbajo=Frame(self.raiz)
        self.frameDeAbajo.pack(side=BOTTOM)
        
        self.t1=Entry(self.textos,width=40)
        self.t1.grid(row=0,column=0,padx=10,pady=10)
        
        self.t2=Entry(self.textos,width=40)
        self.t2.grid(row=1,column=0)
        
        self.t3=Entry(self.textos,width=40)
        self.t3.grid(row=2,column=0)
         
        self.t4=Entry(self.textos,width=40)
        self.t4.grid(row=3,column=0)
        
        self.b1=Button(self.textos,text='Validar',command=lambda:self.validar(1))
        self.b1.grid(row=0,column=1,padx=10,pady=10)
        
        self.b2=Button(self.textos,text='Validar',command=lambda:self.validar(1))
        self.b2.grid(row=1,column=1,padx=10,pady=10)
        
        self.b3=Button(self.textos,text='Validar',command=lambda:self.validar(1))
        self.b3.grid(row=2,column=1,padx=10,pady=10)
        
        self.b4=Button(self.textos,text='Validar',command=lambda:self.validar(1))
        self.b4.grid(row=3,column=1,padx=10,pady=10)
        
        self.l1=Label(self.textos,text='...')
        self.l1.grid(row=0,column=2)
        self.l2=Label(self.textos,text='...')
        self.l2.grid(row=1,column=2)
        self.l3=Label(self.textos,text='...')
        self.l3.grid(row=2,column=2)
        self.l4=Label(self.textos,text='...')
        self.l4.grid(row=3,column=2)
        
        self.bsalir=Button(self.frameDeAbajo,text='Salir',command=self.raiz.destroy)
        self.bsalir.pack(side=LEFT)
        self.blimpiar=Button(self.frameDeAbajo,text='Limpiar',command=self.limpiar)
        self.blimpiar.pack(side=LEFT)
        
        self.raiz.mainloop()
        
    def limpiar(self):
        self.t1.delete(first=0,last='end')
        self.l1.config(fg='black',text="...")
        self.t2.delete(first=0,last='end')
        self.l2.config(fg='black',text="...")
        self.t3.delete(first=0,last='end')
        self.l3.config(fg='black',text="...")
        self.t4.delete(first=0,last='end')
        self.l4.config(fg='black',text="...")
        
    def validar(self,numero):
        if(numero==1):
            txtAValidar=self.t1.get()
            txtAValidar2=self.t2.get()
            txtAValidar3=self.t3.get()
            txtAValidar4=self.t4.get()
            a=re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$",txtAValidar)
            b=re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$",txtAValidar2)
            c=re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$",txtAValidar3)
            d=re.search("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$",txtAValidar4)
            
            e=re.search("^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$",txtAValidar)
            f=re.search("^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$",txtAValidar2)
            g=re.search("^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$",txtAValidar3)
            h=re.search("^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$",txtAValidar4)
            
            if(a):
                self.l1.config(fg="green",text='IPv4 valida')
                
            elif(b):
                self.l2.config(fg="green",text='IPv4 valida')

            elif(c):
                self.l3.config(fg="green",text='IPv4 valida')
                
            elif(d):
                self.l4.config(fg="green",text='IPv4 valida')
                
            elif(e):
                self.l1.config(fg="blue",text='IPv6 valida')

            elif(f):
                self.l2.config(fg="blue",text='IPv6 valida')
                
            elif(g):
                self.l3.config(fg="blue",text='IPv6 valida')
                
            elif(h):
                self.l4.config(fg="blue",text='IPv6 valida')
                
            else:
               self.l1.config(fg="red",text='IP Invalida')
               self.l2.config(fg="red",text='IP Invalida') 
               self.l3.config(fg="red",text='IP Invalida') 
               self.l4.config(fg="red",text='IP Invalida') 
            
app=aplicacion()