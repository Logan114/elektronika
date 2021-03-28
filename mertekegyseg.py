#mertekegyseg
def mertekegyseg():
    import si
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
    men1 = men
    me1 = 'uwu'