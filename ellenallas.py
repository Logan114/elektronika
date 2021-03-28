
#ellenállás
'''
---x--x--x---
|           |
|-----x-----|
|           |
'''
replus = lambda a,b: a*b/ (a+b)
import si
    

def parhuzamos_ellenallas():
    mertekegys = input("\n Milyen mértékegységgel dolgozol \n (k)ilo (m)ikro (n)ano (s)emmi ")
    mertekegyseg = mertekegys.lower()
    
    if mertekegyseg == "k":
        me = si.kilo
        men = "kΩ"
        
    if mertekegyseg == "m":
        me = si.mikro
        men = "mΩ"
            
    if mertekegyseg == "n":
        me = si.nano
        men = "nΩ"
                
    if mertekegyseg == "s":
        me = si.semmi
        men = "Ω"

    r1= int(float(input('\nR1=')))
    r2= int(float(input('\nR2=')))
    r3= int(float(input('\nR3=')))
    r4= int(float(input('\nR4=')))
    r123 = r1+r2+r3
    r1234 = r123+r4
    Re = replus(r123,r4)
    print ("\n parhuzamban=",Re, "Ω", "\n", Re/me, men)
    print ("\n sorban", r1234,"Ω","\n", r1234/me,men)
parhuzamos_ellenallas()