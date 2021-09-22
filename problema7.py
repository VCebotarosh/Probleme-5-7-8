venit=[123,12345,15233,2618,1893,12,1895]
zile=["Luni","Marti","Miercuri","Joi", "Vineri", "Sambata", "Duminica"]
venit_saptamanal=sum(venit)
print(f"Venitul saptamanal al intreprinderii este {venit_saptamanal}")
medie=venit_saptamanal/len(venit)
print(f"Media venitului zilnic este {round(medie,3)}")
maxim=max(venit)
for i in range(len(venit)):
    if venit[i]==maxim:
        print(f"Venitul cel mai mare este in ziua de {zile[i]}")
minim=min(venit)
for i in range(len(venit)):
    if venit[i]==minim:
        print(f"Venitul cel mai mic este in ziua de {zile[i]}")