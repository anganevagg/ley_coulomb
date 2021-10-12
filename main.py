import math

def distancia(v1, v2, R):
	r = []
	for i in range(R):
		r.append(0.0)
	for i in range(0, R):
		r[i] = v2[i] - v1[i]
	return r

def sumaVector(v1, v2, R):
	r = []
	for i in range(R):
		r.append(0.0)
	for i in range(R):
		r[i] = v2[i] + v1[i]
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
		r[i].append(distancia(posiciones[i], posiciones[j], R))

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


for i in range(n):
	print(f"Fuerzas que ejerce la carga {i+1} ", F[i])

Fn = []
for i in range(n):
	sum = []
	for j in range(R):
		sum.append(0.0)
	for j in range(len(F)):
		if i==j:
			continue
		elif i<j:
			sum = sumaVector(sum, F[i][i], R)
		else:
			sum = sumaVector(sum, F[i][i-1], R)
		Fn.append(sum)

for i in range(n):
	print(f"Fuerza neta en la carga {i+1}", Fn[i])
