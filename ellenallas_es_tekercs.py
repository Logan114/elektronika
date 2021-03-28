#ellenállás és tekerls
import kepletek
import kepletek

omega = "Ω"
import mertekegyseg
import si
#A műveletek
    
def Zl():
    R = int(float(input("\n R=")))
    Xl = int(float(input('\n Xl=')))
    Zl = kepletek.nZl (R,Xl)
    print ( "Zl=", Zl, omega, " = ", Zl*si.kilo, "k",omega)

    

def Xl():
    F = int(float(input("\nF=")))
    L = int(float(input("\nL=")))
    Xl = kepletek.nXL(F,L)
    print ('\n','Xl=', Xl, omega, Xl/si.kilo, "k",omega, '\n')

def I():
    Ube =int(float(input('\n U Be=')))
    Zl =int(float(input('\n Zl=')))
    I = Ube/Zl
    print('\n', I, "A", I/si.mili, "mA")
    
def Url():
    R = int(float(input('\n R=')))
    Ir= int(float(input('\n Ir=')))
    Url = kepletek.nUrl(R,Ir)
    print ("\n",Url, "V")
    
def Ul():
    Xl = int(float(input('\n R=')))
    Il= int(float(input('\n Ir=')))
    Ul = kepletek.nUl(Xl,Il)
    print ("\n",Ul, "V")
    
def Ube():
    Zl =int(float(input('\n Zl=')))
    I =int(float(input('\n I=')))
    Ube = kepletek.nUbe(I, Zl)
#A futtatható résZle
muvelet = input("\n Mit szeretnél számolni? \n Zl \n Xl \n I \n Url \n Ul \n")
muv = muvelet.lower()

if muv == "z":
    Zl()
if muv == "u":
    muvelet = input("U(rl) vagy U(l) ")
    muv = muvelet.lower()
    if muv == "rl":
        Url()
    if muv == "l":
        Ul()
    if muv == "url":
        Url()
    if muv == "ul":
        Ul()
if muv == "ul":
    Ul()
if muv == "url":
    Url()
if muv == "xl":
    Xl()
if muv == "x":
    Xl()
if muv == "i":
    I()
