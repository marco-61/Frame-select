# Test classe frameSelect

from tkinter import *
import tkinter.font
from frameSelect import frameSelect

def bt():
    a=fs.aFrame() # frame attuale
    t=fs.nFrame()    # frame totali
    print('Frame = ',a) #### Stampa su console il numero del frame in uso ####
    if a+1 < t:  # se esiste un altro frame
        fs.visible_off() # rendi invisibile il primo
        a+=1
        fs.select(a) # posizionati su  successivo
        fs.visible_on() # visualizzalo
    else:
        fs.visible_off() # se non ci sono altri frame rendi invisibile l'attuale
        fs.select(0) # ritorna al primo frame
        fs.visible_on()

        
root=Tk()
fs=frameSelect('pack') # usa pack come manager
fnt= tkinter.font.Font(size='13')
root.geometry('300x300')
img0=PhotoImage(file='bip.gif')
img1=PhotoImage(file='bsd.gif')
img2=PhotoImage(file='linux3.gif')
##### Frame 0 ######
frame=Frame(root)
l=Label(frame,text="Label sul Frame 0",bg="yellow",relief=GROOVE,font=fnt).pack()
l1=Label(frame,image=img0,relief=GROOVE).pack()
b=Button(frame,text="Bottone su frame 0",bg='green',relief=SUNKEN,font=fnt,command=bt).pack()
fs.append(frame)
###### Frame 1 #####
frame=Frame(root)
Label(frame,text="Label sul Frame 1",bg="yellow",relief=GROOVE,font=fnt).pack()
l1=Label(frame,image=img1,relief=GROOVE).pack()
b=Button(frame,text="Bottone su Frame 1",bg='red',relief=SUNKEN,font=fnt,command=bt).pack()
fs.append(frame)
###### Frame 2  #####
frame=Frame(root)
l=Label(frame,text="Label sul Frame 2",bg="red",relief=GROOVE,font=fnt).pack()
l1=Label(frame,image=img2,relief=GROOVE).pack()
b=Button(frame,text="Bottone su Frame 2",bg='blue',relief=SUNKEN,font=fnt,command=bt).pack()
fs.append(frame)
#### start ####
fs.select(0) # inizia con il frame 0
fs.visible_on()

root.mainloop()
