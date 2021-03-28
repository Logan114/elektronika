#ellenállás és kondenzátor
import kepletek

omega = "Ω"
import mertekegyseg
import si
#A műveletek
    
def Z():
    R = int(float(input ("\n R=")))
    Xc = int(float(input('\n Xc=')))
    Z = kepletek.nZ(R,Xc)
    print ('\n',"Z=", Z, omega, " = ", Z/si.kilo, "k",omega, "\n")

    

def Xc():
    F = int(float(input("\nF=")))
    C = int(float(input("\nC=")))
    Xc = kepletek.nXC(F,C)
    print ('\n','Xc=', Xc, omega, Xc/si.kilo, "k",omega, '\n')

def I():
    Ube =int(float(input('\n U Be=')))
    Z =int(float(input('\n Z=')))
    I = Ube/Z
    print('\n', I, "A", I/si.mili, "mA")
    
def Ur():
    R = int(float(input('\n R=')))
    Ir= int(float(input('\n Ir=')))
    Ur = kepletek.nUr(R,Ir)
    print ("\n",Ur, "V")
    
def Uc():
    Xc = int(float(input('\n R=')))
    Ic= int(float(input('\n Ir=')))
    Uc = kepletek.nUc(Xc,Ic)
    print ("\n",Uc, "V")
    
def Ube():
    Z =int(float(input('\n Z=')))
    I =int(float(input('\n I=')))
    Ube = kepletek.nUbe(I, Z)
#A futtatható része
muvelet = input("\n Mit szeretnél számolni? \n Z \n Xc \n I \n Url \n Uc \n")
muv = muvelet.lower()

if muv == "z":
    Z()
if muv == "u":
    muvelet = input("U(r)l vagy U(c)l ")
    muv = muvelet.lower()
    if muv == "r":
        Ur()
    if muv == "c":
        Uc()
    if muv == "ur":
        Ur()
    if muv == "uc":
        Uc()
if muv == "uc":
    Uc()
if muv == "url":
    Ur()
if muv == "xc":
    Xc()
if muv == "x":
    Xc()

if muv == "i":
    I()
