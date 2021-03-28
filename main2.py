#main 2.0
import si


for i in range(1, 100):
    muvelet = input("Mit szeretnél számolni? \n (E)llenállás \n (K)ondenzátor \n (E)llenallas és (T)ekercs  \n (E)llenállás és (K)ondenzátor\n \n (X) kilépés \n \n")
    muv = muvelet.lower()
    if muv == 'x':
        quit()
    if muv == "k":
        import kondenzator
    
    if muv == "e":
        import ellenallas
        
    if muv == "ek":
        import ellenallas_es_kondenzator
    if muv == 'et':
        import ellenallas_es_tekercs