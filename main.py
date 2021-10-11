import math

def sumaVector(v1, v2):
    r = [0.0, 0.0]
    for i in range(1,3):
        r[i-1] = v2[i] - v1[i]
    return r

n = int(input("Ingresa el número de cargas a evaluar: "))
R = int(input("Ingresa el número de dimensiones a evaluar: "))
cargas=[]
k=9e9
for i in range(0, n):
    cargas.append([])
    cargas[i].append(float(input(f"Ingresa q para la carga {i+1}: ")))
    cargas[i].append(float(input(f"Ingresa x para la carga {i+1}: ")))
    cargas[i].append(float(input(f"Ingresa y para la carga {i+1}: ")))

print("cargas ",cargas)

r = []

for i in range(n):
    for j in range(n):
        r.append(sumaVector(cargas[i], cargas[j]))

print("vectores r", r)

rn = []

for i in range(1, n+1):
    c=r[i]
    rn.append(math.sqrt((c[0]**2+c[1]**2)))
print("distancias", rn)

F=[]

for i in range(len(r)):
    F.append([0.0, 0.0])
    for j in range(0,2):
        qr=cargas[i][0]*cargas[j][0]
        F[i][j]=rn[j]*(((k*qr)/rn[i]**2)*r[i][j])

print(F)