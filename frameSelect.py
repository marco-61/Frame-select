"""
Classe     : frameSelect.py
Scopo      : Classe per gestire la visualizzazione dei frame in tkinter
Versione   : 1.0
Autore     : Marco Salvati
Data       : 2019-03-01
Revisione   : --
"""

from tkinter import *
class frameSelect:
    def __init__(self,Layout):
        if isinstance(Layout,str):
            m={"PACK":1,"GRID":2,"PLACE":3}
            lu=Layout.upper()
            if lu in m:
                self.__Layout=m[lu]
            else:
                self.__Layout=1
        elif isinstance(Layout,int):        
            if Layout >=1 and  Layout<=3: # Valori accettati 1=Pack 2= Grid 3=Place
                self.__Layout=Layout  # Layout Manager
            else: # altrimenti default pack
                self.__Layout=1
        self.__stack=[]       # Frame Stack
        self.__fap=-1          # Frame attive Pointer
        self.__visible=False  # Indica se il frame attuale è visibile
        
    def append(self,frame):
        self.__stack.append(frame)
        self.__fap+=1
        
    def nFrame(self):         # Ritorna il numero di frames inseriti
        return len(self.__stack)
    
    def aFrame(self):         # Attuale frame
        return self.__fap
    
    def select(self,n):       # Seleziona un frame
        if n <0:
           self.__fap=0
        elif n>=len(self.__stack):
           self.__fap=len(self.__stack)-1
        else:
            self.__fap=n 
    def visible_on(self):
        if self.__visible==False:
            self.__visible=True
            if self.__Layout==1:
                self.__stack[self.__fap].pack()
            elif self.__Layout==2:
                self.__stack[self.__fap].grid()
            else:
                self.__stack[self.__fap].place()
            
    def visible_off(self):
        if self.__visible==True:
            self.__visible=False
            if self.__Layout==1:
                self.__stack[self.__fap].pack_forget()
            elif self.__Layout==2:
                self.__stack[self.__fap].grid_forget()
            else:
                self.__stack[self.__fap].place_forget()
                
    def status(self):         # Ritorna la visibilità del frame corrente
        return self.__visible
    
    def fReturn(self): # ritorna il frame attuale
        return self.__stack[self.__fap]
    
