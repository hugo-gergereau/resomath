import tkinter
from tkinter import *
import tkinter as tk
from math import *


window = tk.Tk()
window.state("zoomed")
window.configure(bg='#696969')


def fenetre_verif ():
    fenetre_verif = Toplevel()
    
    fenetre_verif.configure(bg='#696969')

    oui = tk.Button(fenetre_verif, text=" OUI ! ", activebackground='red',activeforeground='white', fg= 'white' , bg='#696969',  command= fenetre_verif.destroy and window.destroy)
    oui.pack()
    non = tk.Button(fenetre_verif, text=" NON ! ", activebackground='red',activeforeground='white', fg= 'white' , bg='#696969',  command= fenetre_verif.destroy)
    non.pack()

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=window)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Quit!", command=fenetre_verif)

def multiplication ():
    multiplication = Toplevel()
    multiplication.state("zoomed")
    multiplication.configure(bg='#696969')
    def calcul (): 
    #Récupération des variables
        D=int(A.get()) 
        E=int(B.get()) 
        
 
    #Calcul 
        G=D*E
 
        chaine.configure (text = 'le resultat est ' , bg='#696969' , fg= 'white' ) 
        chaine2.configure (text = G ,bg='#696969' , fg= 'white' ) 
    txt1=Label(multiplication, fg='white' , bg='#696969', text="A:").grid(row=1, column=1) 
    txt2=Label(multiplication, fg='white' , bg='#696969', text='B:').grid(row=2, column=1) 
    
    Button(multiplication,text='Calculer', fg= 'white', bg='#696969',activebackground='#345',activeforeground='white', command=calcul).grid(row=4 , column=1) 
    Button(multiplication,text='Quitter', fg= 'white',  bg='#696969',activebackground='red',activeforeground='white', command=multiplication.destroy).grid(row=4, column=2) 
 
    A=Entry(multiplication) 
    B=Entry(multiplication) 
    chaine = Label(multiplication) 
    chaine2 = Label(multiplication)
 
    A.grid(row=1, column=2) 
    B.grid(row=2, column=2) 
    
    chaine.grid(row=5, column=2) 
    chaine2.grid(row=5, column=3)
    



def division ():
    division = Toplevel()
    division.state("zoomed")
    division.configure(bg='#696969')
    def calcul (): 
    #Récupération des variables
        D=int(A.get()) 
        E=int(B.get()) 
        
 
    #Calcul 
        G=D//E
 
        chaine.configure (text = 'le resultat est ' ,bg='#696969' , fg= 'white' ) 
        chaine2.configure (text = G ,bg='#696969' , fg= 'white' ) 
    txt1=Label(division, fg='white' , bg='#696969', text="A:").grid(row=1, column=1) 
    txt2=Label(division, fg='white' , bg='#696969', text='B:').grid(row=2, column=1) 
    
    Button(division,text='Calculer', fg= 'white', bg='#696969', activebackground='#345',activeforeground='white', command=calcul).grid(row=4 , column=1) 
    Button(division,text='Quitter',  fg= 'white', bg='#696969', activebackground='red',activeforeground='white', command=division.destroy).grid(row=4, column=2) 
 
    A=Entry(division) 
    B=Entry(division) 
    chaine = Label(division) 
    chaine2 = Label(division)
 
    A.grid(row=1, column=2) 
    B.grid(row=2, column=2) 
    
    chaine.grid(row=5, column=2) 
    chaine2.grid(row=5, column=3)




def addition ():
    addition = Toplevel()
    addition.state("zoomed")
    addition.configure(bg='#696969')
    def calcul (): 
    #Récupération des variables
        D=int(A.get()) 
        E=int(B.get()) 
        
 
    #Calcul 
        G=D+E
 
        chaine.configure (text = 'le resultat est ' ,bg='#696969' , fg= 'white' ) 
        chaine2.configure (text = G ,bg='#696969' , fg= 'white' ) 
    txt1=Label(addition, fg='white' , bg='#696969', text="A:").grid(row=1, column=1) 
    txt2=Label(addition, fg='white' , bg='#696969', text='B:').grid(row=2, column=1) 
    
    Button(addition,text='Calculer',fg= 'white',  bg='#696969', activebackground='#345',activeforeground='white', command=calcul).grid(row=4 , column=1) 
    Button(addition,text='Quitter', fg= 'white',  bg='#696969', activebackground='red',activeforeground='white', command=addition.destroy).grid(row=4, column=2) 
 
    A=Entry(addition) 
    B=Entry(addition) 
    chaine = Label(addition) 
    chaine2 = Label(addition)
 
    A.grid(row=1, column=2) 
    B.grid(row=2, column=2) 
    
    chaine.grid(row=5, column=2) 
    chaine2.grid(row=5, column=3)



def soustraction ():
    soustraction = Toplevel()
    soustraction.state("zoomed")
    soustraction.configure(bg='#696969')
    def calcul (): 
    #Récupération des variables
        D=int(A.get()) 
        E=int(B.get()) 
        
 
    #Calcul 
        G=D-E
 
        chaine.configure (text = 'le resultat est ' ,bg='#696969' , fg= 'white' ) 
        chaine2.configure (text = G ,bg='#696969' , fg= 'white' ) 
    txt1=Label(soustraction, fg='white' , bg='#696969', text="A:").grid(row=1, column=1) 
    txt2=Label(soustraction, fg='white' , bg='#696969', text='B:').grid(row=2, column=1) 
    
    Button(soustraction,text='Calculer', fg= 'white', bg='#696969', activebackground='#345',activeforeground='white', command=calcul).grid(row=4 , column=1) 
    Button(soustraction,text='Quitter', fg= 'white',  bg='#696969', activebackground='red',activeforeground='white', command=soustraction.destroy).grid(row=4, column=2) 
 
    A=Entry(soustraction) 
    B=Entry(soustraction) 
    chaine = Label(soustraction) 
    chaine2 = Label(soustraction)
 
    A.grid(row=1, column=2) 
    B.grid(row=2, column=2) 
    
    chaine.grid(row=5, column=2) 
    chaine2.grid(row=5, column=3)

def PGCD ():
    PGCD = Toplevel()
    PGCD.state("zoomed")
    PGCD.configure(bg='#696969')
    def calcul (): 
    #Récupération des variables
        D=int(A.get()) 
        E=int(B.get())
        r = ''
        if(D<E):
            D,E = E,D
        while ( D%E != 0):
            r = D % E
            D,E = E,r
        print(E)       
        
 
    #Calcul 
        
        chaine.configure (text = 'le resultat est ' , bg='#696969' , fg= 'white' ) 
        chaine2.configure (text = E ,bg='#696969' , fg= 'white' ) 
    txt1=Label(PGCD, fg='white' , bg='#696969', text="A:").grid(row=1, column=1) 
    txt2=Label(PGCD, fg='white' , bg='#696969', text='B:').grid(row=2, column=1) 
    
    Button(PGCD,text='Calculer', fg= 'white', bg='#696969',activebackground='#345',activeforeground='white', command=calcul).grid(row=4 , column=1) 
    Button(PGCD,text='Quitter', fg= 'white',  bg='#696969',activebackground='red',activeforeground='white', command=PGCD.destroy).grid(row=4, column=2) 
 
    A=Entry(PGCD) 
    B=Entry(PGCD) 
    chaine = Label(PGCD) 
    chaine2 = Label(PGCD)
 
    A.grid(row=1, column=2) 
    B.grid(row=2, column=2) 
    
    chaine.grid(row=5, column=2) 
    chaine2.grid(row=5, column=3)
    
    
def nombre_premier ():
    nombre_premier = Toplevel()
    nombre_premier.state("zoomed")
    nombre_premier.configure(bg='#696969')
    def calcul (): 
    #Récupération des variables
        D=int(A.get()) 
         
        
 
    #Calcul 
    
        

        cpt = 0
        liste1 = []
        resultat = ' '
        resultat = tk.StringVar(resultat)
        for i in range (1,D+1):
            if(D % i ==0):
                cpt = cpt + 1
                liste1.append(i)
                resultat = resultat + str(i)+' '
        if(cpt == 2):
            print("votre nombre",D,"est premier")
            chaine2.configure (text = resultat  ,bg='#696969' , fg= 'white' )
        else:
            print("votre nombre",D,"n'est pas premier")
            print("voici les diviseur de ",D," :",resultat, )
       
 
        chaine.configure (text = 'le resultat est ' ,bg='#696969' , fg= 'white' ) 
        
    txt1=Label(nombre_premier, fg='white' , bg='#696969', text="entre votre nombre :").grid(row=1, column=1) 
    
    
    Button(nombre_premier,text='Calculer', fg= 'white', bg='#696969', activebackground='#345',activeforeground='white', command=calcul).grid(row=4 , column=1) 
    Button(nombre_premier,text='Quitter', fg= 'white',  bg='#696969', activebackground='red',activeforeground='white', command=nombre_premier.destroy).grid(row=4, column=2) 
 
    A=Entry(nombre_premier) 
   
    chaine = Label(nombre_premier) 
    chaine2 = Label(nombre_premier)
 
    A.grid(row=1, column=2) 
    
    
    chaine.grid(row=5, column=2) 
    chaine2.grid(row=5, column=4)
    
    







label = tk.Label(window, text="RESOMATH!",fg="red" , bg='#696969',)
label.pack()

multiplication = tk.Button(window, text="multiplication ", activebackground='#345',activeforeground='white' , fg= 'white' , bg='#696969',command= multiplication)
multiplication.pack()

division = tk.Button(window, text="division ", activebackground='#345',activeforeground='white', fg= 'white' , bg='#696969',command= division)
division.pack()


addition = tk.Button(window, text="addition ", activebackground='#345',activeforeground='white', fg= 'white' , bg='#696969', command= addition)
addition.pack()


soustraction = tk.Button(window, text="soustraction ", activebackground='#345',activeforeground='white', fg= 'white' , bg='#696969',  command= soustraction)
soustraction.pack()

PGCD = tk.Button(window, text="PGCD ", activebackground='#345',activeforeground='white', fg= 'white' , bg='#696969',  command= PGCD)
PGCD.pack()

nombre_premier = tk.Button(window, text="ombre premiers", activebackground='#345',activeforeground='white', fg= 'white' , bg='#696969',  command= nombre_premier)
nombre_premier.pack()

quitter = tk.Button(window, text="quitter ! ", activebackground='red',activeforeground='white', fg= 'white' , bg='#696969',  command= fenetre_verif)
quitter.pack()

window.config(menu=menubar)
window.mainloop()