#kepletek
pi = 6.28318530718
import math
nXc = lambda f,c,: 1/(pi*f*c)
nC = lambda c,f,Xc: 1/(pi*f*Xc)
nF = lambda c,Xc: 1/(pi*c*Xc)
nZ = lambda R,Xc: math.sqrt(R ** 2 + Xc ** 2)
nUr = lambda R,Ir: (R*Ir)
nUc = lambda Xc,Ic: (Xc*Ic)
nUbe = lambda R,Z: (R*Z)
#terkercshez
nXL = lambda f,l,: 1/(pi*f*l)
nL = lambda l,f,Xl: 1/(pi*f*Xl)
nlF = lambda l,Xl: 1/(pi*l*Xl)
nZl = lambda R,XL: math.sqrt(R ** 2 + XL ** 2)
nUrl = lambda L,Ir:  (L*Ir)
nUl = lambda XL,Il:  (XL*Il)
nUBeL = lambda R, ZL: (R/ZL)