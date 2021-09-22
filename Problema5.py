produs=1
suma=0
x=[1,2,-7,4,5]
y=x.copy()
for i in range(0,len(x)-2):
    suma+=x[i]
print(f"Suma primilor 3 termeni din vectorul x este {suma}")
suma_y=sum(y)
print(f"Suma elementelor din vectorul y este {suma_y}")
for elem in x:
    produs=produs*elem
print(f"Produsul elementelor din vectorul x este {produs}")
var_abs=abs(y[2])
suma_primele=x[0]+y[0]
print(f"Valoarea absoluta a variabilei a 3 in vectorul y este {var_abs}")
print(f"Suma primelor elente ale ambelor vectori este {suma_primele}")