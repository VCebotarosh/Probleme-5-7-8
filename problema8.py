temperatura=[2,6,8,11,13,15,14,20,22,24,25,25,25,22,30,24,21,24,25,23,10,11,12,1]
ore=["00","01","02","03", "04", "05", "06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
temp_medie=sum(temperatura)/len(temperatura)
print(f"Temperatura medie este {round(temp_medie,2)}")
maxim=max(temperatura)
print(f"Temperatura maxima este {maxim} grade")
minim=min(temperatura)
print(f"Minimul temperaturii este {minim} grade")
for i in range(len(temperatura)):
    if temperatura[i]==maxim:
        print(f"Temperatura cea mai mare este la ora {ore[i]}")

for i in range(len(temperatura)):
    if temperatura[i]==minim:
        print(f"Temperatura cea mai mica este la ora {ore[i]}")