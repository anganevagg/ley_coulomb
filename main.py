import math

def sumaVector(v1, v2, r):
	r = []
	for i in range(R):
		r.append(0.0)
	for i in range(0, R):
		r[i] = v2[i] - v1[i]
	return r

n = int(input("Ingresa el número de cargas a evaluar: "))
R = int(input("Ingresa el número de dimensiones a evaluar: "))
cargas=[]
posiciones=[]
K=9e9
for i in range(0, n):
	cargas.append(float(input(f"Ingresa q para la carga {i+1}: ")))
	posiciones.append([])
	for j in range(0, R):
		posiciones[i].append(float(input(f"Ingresa R{j+1} para la carga {i+1}: ")))

print("cargas ", cargas)
print("posiciones", posiciones)
r = []

for i in range(n):
	r.append([])
	for j in range(n):
		if j==i:
			continue
		r[i].append(sumaVector(posiciones[i], posiciones[j], R))

print("vectores r", r)

rn = []

for i in range(len(r)):
	rn.append([])
	for j in range(len(r[i])):
		c=r[i][j]
		sum = 0.0
		for k in range(R):
			sum+=(c[k]**2)
		rn[i].append(math.sqrt(sum))
print("distancias rn", rn)

qr=[]
for i in range(n):
	qr.append([])
	for j in range(n):
		if(i==j):
			continue
		qr[i].append(cargas[i]*cargas[j])

F=[]

for i in range(n):
	F.append([])
	for j in range(len(r[i])):
		F[i].append([])
		for k in range(len(r[i][j])):
			F[i][j].append(r[i][j][k]*(((K*qr[i][j])/(rn[i][j]**2))*(1/rn[i][j])))

print("Fuerzas que ejerce cada carga F ", F)
