#kondenzátor
replus = lambda a,b: a*b/ (a+b)
import si

def parhuzamos_kondenzator():
    mertekegys = input("\n Milyen mértékegységgel dolgozol \n (m)ikro (n)ano (p)ico(s)emmi ")
    mertekegyseg = mertekegys.lower()
    if mertekegyseg == "p":
        me = si.pico
        men = "pF"
        
    if mertekegyseg == "m":
        me = si.mikro
        men = "mF"
            
    if mertekegyseg == "n":
        me = si.nano
        men = "nF"
                
    if mertekegyseg == "s":
        me = si.semmi
        men = "F"
                    
    c1= int(float(input('\nC1=')))
    c2= int(float(input('\nC2=')))
    c3= int(float(input('\nC3=')))
    c4= int(float(input('\nC4=')))
    c12 = replus(c1,c2)
    c123 = replus (c12,c3)
    Ce = replus(c123,c4)
    me1=Ce*me
    print ("\n parhuzamban=",Ce, "\n",me1, men)
    print ("\n sorban", c123,"\n", c123*me, men)
    
parhuzamos_kondenzator()