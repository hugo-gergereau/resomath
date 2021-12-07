from tkinter import *
import tkinter as tk
from math import *

window = tk.Tk()
window.state("zoomed")



def multiplication ():
    multiplication = Toplevel()
    multiplication.state("zoomed")
    def calcul (): 
    #Récupération des variables
        D=int(A.get()) 
        E=int(B.get()) 
        
 
    #Calcul 
        G=D*E
 
        chaine.configure (text = 'le resultat est ',G, ) 
 
    txt1=Label(multiplication, text="A:").grid(row=1, column=1) 
    txt2=Label(multiplication, text='B:').grid(row=2, column=1) 
    
    Button(multiplication,text='Calculer',command=calcul).grid(row=4 , column=1) 
    Button(multiplication,text='Quitter',command=multiplication.destroy).grid(row=4, column=2) 
 
    A=Entry(multiplication) 
    B=Entry(multiplication) 
    chaine = Label(multiplication) 
 
    A.grid(row=1, column=2) 
    B.grid(row=2, column=2) 
    
    chaine.grid(row=5, column=2) 
    








label = tk.Label(window, text="RESOMATH!",fg="red",)
label.pack()

multiplication = tk.Button(window, text="multiplication ", fg="black",command= multiplication)
multiplication.pack()












window.mainloop()

