#-*- coding:utf-8 -*-
from __future__ import print_function
import sys
from time import time
import random

#----------------------------------------------
#Autoras:
#Silvia del Carmen Montero Vega
#Maria Robles del Blanco
#---------------------------------------------


dic={}
numarcadas=0
estadopartida=0
matriz=[]
dicmayus={"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25, "@":26, "#":27, "$":28, "%":29, "&":30}
dicminus={"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25, "=":26, "+":27, "-":28, ":":29, "/":30}
filas=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z", "@", "#", "$", "%", "&"]
columnas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","=","+","-",":","/"]
tiempo_inicial=time()





#Funcion que crea el tablero(una matriz)
def mineMap(fil, col,matriz):
	
	
	for i in range(fil):
		i=["[]"]*col
		matriz.append(i)

	
#Funcion que coloca minas de forma aleatoria y almacena las coordenadas donde se encuentra cada mina en la lista aquihaymina.
#El segundo while de la funcion sirve para procurar que no haya dos minas almacenadas en una misma posicion, pasando la lista a un set y nuevamente a una lista 
#(para evitar repeticiones en la lista) y creando las minas que faltan para alcanzar el numero de minas para cada nivel.
def colocarminas(matriz,col,fil,minas):
	contador=1
	contador2=1
	aquihaymina=[]
	while contador<=minas:
		i=random.randint(0,col-1)
		j=random.randint(0,fil-1)
		contador=contador+1
		aquihaymina.append((i,j))
	aquihaymina=list(set(aquihaymina))
	while len(aquihaymina)!=minas:
		for x in range(minas-len(aquihaymina)):
			i=random.randint(0,col-1)
			j=random.randint(0,fil-1)
			aquihaymina.append((i,j))
		aquihaymina=list(set(aquihaymina))

		

	return aquihaymina


#Funcion que comprueba si una posicion concreta se encuentra en el tablero
def estaeneltablero(matriz,fil,col,i,j):
	esta=False
	if (i >= 0 and i < fil) and (j >= 0 and j < col):
		esta=True
	return esta

#Funcion que calcula automaticamente las n de cada celda que tiene una mina cerca
def ponernumeros(matriz,fil,col,aquihaymina,dic):
	#Crearemos mediante dos bucles for un diccionario que almacene la posicion de la matriz con su n correspondiente (que al principio sera 0) 
	#e iremos aumentando el n cada vez que sea pertinente
	for i in range(fil):
		for j in range(col):
			dic[(i,j)]=0



	for a in range(fil):
		if a%2==0:
			for b in range(col):
			
				if (a,b) in aquihaymina:
					x1=estaeneltablero(matriz,fil,col,a,b-1)
					if x1==True and (a,b-1) not in aquihaymina: 
						dic[(a,b-1)]=dic[(a,b-1)]+1

					x2=estaeneltablero(matriz,fil,col,a,b+1)
					if x2==True and (a,b+1) not in aquihaymina: 
						dic[(a,b+1)]=dic[(a,b+1)]+1

					x3=estaeneltablero(matriz,fil,col,a-1,b)
					if x3==True and (a-1,b) not in aquihaymina: 
						dic[(a-1,b)]=dic[(a-1,b)]+1

					x4=estaeneltablero(matriz,fil,col,a-1,b+1)
					if x4==True and (a-1,b+1) not in aquihaymina: 
						dic[(a-1,b+1)]=dic[(a-1,b+1)]+1

					x5=estaeneltablero(matriz,fil,col,a+1,b)
					if x5==True and (a+1,b) not in aquihaymina: 
						dic[(a+1,b)]=dic[(a+1,b)]+1

					x6=estaeneltablero(matriz,fil,col,a+1,b+1)
					if x6==True and (a+1,b+1) not in aquihaymina: 
						dic[(a+1,b+1)]=dic[(a+1,b+1)]+1

		else:
			for b in range(col):
					
				if (a,b) in aquihaymina:
					x1=estaeneltablero(matriz,fil,col,a,b-1)
					if x1==True and (a,b-1) not in aquihaymina: 
						dic[(a,b-1)]=dic[(a,b-1)]+1

					x2=estaeneltablero(matriz,fil,col,a,b+1)
					if x2==True and (a,b+1) not in aquihaymina: 
						dic[(a,b+1)]=dic[(a,b+1)]+1

					x3=estaeneltablero(matriz,fil,col,a-1,b-1)
					if x3==True and (a-1,b-1) not in aquihaymina: 
						dic[(a-1,b-1)]=dic[(a-1,b-1)]+1

					x4=estaeneltablero(matriz,fil,col,a-1,b)
					if x4==True and (a-1,b) not in aquihaymina: 
						dic[(a-1,b)]=dic[(a-1,b)]+1

					x5=estaeneltablero(matriz,fil,col,a+1,b-1)
					if x5==True and (a+1,b-1) not in aquihaymina: 
						dic[(a+1,b-1)]=dic[(a+1,b-1)]+1

					x6=estaeneltablero(matriz,fil,col,a+1,b)
					if x6==True and (a+1,b) not in aquihaymina: 
						dic[(a+1,b)]=dic[(a+1,b)]+1


#Algoritmo de llenado por difusion, abre las celdas que rodean a una celda particular (en el caso de que se solicite abrir una celda ya abierta)
def floodFill(matriz,fil,col,dic,i,j):
	x1=estaeneltablero(matriz,fil,col,i,j-1)
	if matriz[i][j-1]!="X" and x1==True:
		if dic[(i,j-1)]>0:
			matriz[i][j-1]=dic[(i,j-1)]
		elif dic[(i,j-1)]==0:
			matriz[i][j-1]=" "
		elif dic[(i,j-1)]<0:
			matriz[(i,j-1)]="?"

	x2=estaeneltablero(matriz,fil,col,i,j+1)
	if matriz[i][j+1]!="X" and x2==True:
		if dic[(i,j+1)]>0:
			matriz[i][j+1]=dic[(i,j+1)]
		elif dic[(i,j+1)]==0:
			matriz[i][j+1]=" "
		elif dic[(i,j+1)]<0:
			matriz[(i,j+1)]="?"

	if i%2==0:
		x3=estaeneltablero(matriz,fil,col,i-1,j)
		if matriz[i-1][j]!="X" and x3==True:
			if dic[(i-1,j)]>0:
				matriz[i-1][j]=dic[(i-1,j)]
			elif dic[(i-1,j)]==0:
				matriz[i-1][j]=" "
			elif dic[(i-1,j)]<0:
				matriz[(i-1,j)]="?"

		x4=estaeneltablero(matriz,fil,col,i-1,j+1)
		if matriz[i-1][j+1]!="X" and x4==True:
			if dic[(i-1,j+1)]>0:
				matriz[i-1][j+1]=dic[(i-1,j+1)]
			elif dic[(i-1,j+1)]==0:
				matriz[i-1][j+1]=" "
			elif dic[(i-1,j+1)]<0:
				matriz[(i-1,j+1)]="?"

		x5=estaeneltablero(matriz,fil,col,i+1,j)
		if matriz[i+1][j]!="X" and x5==True:
			if dic[(i+1,j)]>0:
				matriz[i+1][j]=dic[(i+1,j)]
			elif dic[(i+1,j)]==0:
				matriz[i+1][j]=" "
			elif dic[(i+1,j)]<0:
				matriz[(i+1,j)]="?"

		x6=estaeneltablero(matriz,fil,col,i+1,j+1)
		if matriz[i+1][j+1]!="X" and x6==True:
			if dic[(i+1,j+1)]>0:
				matriz[i+1][j+1]=dic[(i+1,j+1)]
			elif dic[(i+1,j+1)]==0:
				matriz[i+1][j+1]=" "
			elif dic[(i+1,j+1)]<0:
				matriz[(i+1,j+1)]="?"

	else:
		x3=estaeneltablero(matriz,fil,col,i-1,j-1)
		if matriz[i-1][j-1]!="X" and x3==True:
			if dic[(i-1,j-1)]>0:
				matriz[i-1][j-1]=dic[(i-1,j-1)]
			elif dic[(i-1,j-1)]==0:
				matriz[i-1][j-1]=" "
			elif dic[(i-1,j-1)]<0:
				matriz[(i-1,j-1)]="?"

		x4=estaeneltablero(matriz,fil,col,i-1,j)
		if matriz[i-1][j]!="X" and x4==True:
			if dic[(i-1,j)]>0:
				matriz[i-1][j]=dic[(i-1,j)]
			elif dic[(i-1,j)]==0:
				matriz[i-1][j]=" "
			elif dic[(i-1,j)]<0:
				matriz[(i-1,j)]="?"


		x5=estaeneltablero(matriz,fil,col,i+1,j-1)
		if matriz[i+1][j-1]!="X" and x5==True:
			if dic[(i+1,j-1)]>0:
				matriz[i+1][j-1]=dic[(i+1,j-1)]
			elif dic[(i+1,j-1)]==0:
				matriz[i+1][j-1]=" "
			elif dic[(i+1,j-1)]<0:
				matriz[(i+1,j-1)]="?"


		x6=estaeneltablero(matriz,fil,col,i+1,j)
		if matriz[i+1][j]!="X" and x6==True:
			if dic[(i+1,j)]>0:
				matriz[i+1][j]=dic[(i+1,j)]
			elif dic[(i+1,j)]==0:
				matriz[i+1][j]=" "
			elif dic[(i+1,j)]<0:
				matriz[(i+1,j)]="?"


#Funcion que sirve para que el jugador introduzca la jugadas y que asegura que sean de la longitud correcta
def IntroducirJugadas():
	print ("Indique celda y accion (! Marcar, * Abrir): ")
	stringjugada=raw_input()

	if len(stringjugada)%3 !=0:
		print ("ENTRADA ERRONEA.")
		print ("Indique celda y accion (! Marcar, * Abrir): ")
		stringjugada=raw_input()
		

	return stringjugada

#Funcion que corta el string introducido por el usuario para separar cada jugada
def cortacadenas(stringjugada):
	listastring=[]
	j=3
	i=0
	while j<=len(stringjugada):
		while i<len(stringjugada):
			stringprima=stringjugada[i:j]
			i+=3
			j+=3
			listastring.append(stringprima)

	return listastring

#Funcion que comienza a descartar las cadenas que sean incorrectas o que esten mal escritas
def evaluarcadenas(listastring, dicminus, dicmayus):
	listadefinitiva=[]
	for i in listastring:
		stringanalizar=i
		if (stringanalizar[2]!="*" and stringanalizar[2]!="!") or stringanalizar[0] not in dicmayus or stringanalizar[1] not in dicminus:
			print ("HAY ENTRADAS ERRONEAS")
			break
		else:
			listadefinitiva.append(stringanalizar)

	return listadefinitiva


#Funcion que cambia las celdas del tablero en funcion de cada jugada introducida por el usuario
def cambiarCeldas(matriz,listadefinitiva, aquihaymina, fil, col, minas, dic):
	global numarcadas
	global estadopartida
	for i in listadefinitiva:
		stringanalizar=i
		j=dicmayus[stringanalizar[0]]
		k=dicminus[stringanalizar[1]]
		if stringanalizar[2]=="*" and (j,k) in aquihaymina: #Si destapas una celda con una mina
			print ("HAS PERDIDO")
			estadopartida=2
			break
		elif stringanalizar[2]=="*" and matriz[j][k]==dic[(j,k)]: #Si intentas abrir una celda ya abierta y con una mina cerca
			print("CELDA YA ABIERTA. NO SE PUEDEN ABRIR LAS CELDAS VECINAS POR NUMERO INSUFICIENTE DE MARCAS")
			break
		elif stringanalizar[2]=="*" and (matriz[j][k]==" " or matriz[j][k]=="?"): #Si intentas abrir una celda ya abierta en la que n<=0
			floodFill(matriz,fil,col,dic,j,k)
		elif stringanalizar[2]=="*" and matriz[j][k]=="X": #Si intentas abrir una celda ya marcada. Se produce un error.
			print ("NO SE PUEDE ABRIR UNA CELDA MARCADA")
			break
		elif stringanalizar[2]=="*" and dic[(j,k)]>0: #Abre una celda en la que n>0
			matriz[j][k]=dic[(j,k)]
		elif stringanalizar[2]=="*" and dic[(j,k)]==0: #Abre una celda en la que n=0
			matriz[j][k]=" "
		elif stringanalizar[2]=="*" and dic[(j,k)]<0: #Abre una celda en la que n<0
			matriz[j][k]="?"
		elif stringanalizar[2]=="!" and (matriz[j][k]==" " or matriz[j][k]==dic[(j,k)] or matriz[j][k]=="?"): #Si intentas marcar una celda ya abierta
			print ("NO PUEDES MARCAR UNA CELDA YA ABIERTA")
			break
		elif stringanalizar[2]=="!" and matriz[j][k]=="X": #Desmarcar una celda
			matriz[j][k]="[]"
			numarcadas = numarcadas-1
		elif stringanalizar[2]=="!" and matriz[j][k]!="X" and numarcadas+1 > minas: #Si intentas marcar mas celdas que minas
			print ("NO SE PUEDEN MARCAR MAS CELDAS QUE MINAS")
			break
		elif stringanalizar[2]=="!" and matriz[j][k]=="[]": #Marcar una celda
			matriz[j][k]="X"
			numarcadas = numarcadas+1

			#Recalculamos la n

			if (j,k) in aquihaymina:
				if j%2==0:
					x1=estaeneltablero(matriz,fil,col,j,k-1)
					if x1==True and (j,k-1) not in aquihaymina: 
						dic[(j,k-1)]=dic[(j,k-1)]-1

					x2=estaeneltablero(matriz,fil,col,j,k+1)
					if x2==True and (j,k+1) not in aquihaymina: 
						dic[(j,k+1)]=dic[(j,k+1)]-1

					x3=estaeneltablero(matriz,fil,col,j-1,k)
					if x3==True and (j-1,k) not in aquihaymina: 
						dic[(j-1,k)]=dic[(j-1,k)]-1

					x4=estaeneltablero(matriz,fil,col,j-1,k+1)
					if x4==True and (j-1,k+1) not in aquihaymina: 
						dic[(j-1,k+1)]=dic[(j-1,k+1)]-1

					x5=estaeneltablero(matriz,fil,col,j+1,k)
					if x5==True and (j+1,k) not in aquihaymina: 
						dic[(j+1,k)]=dic[(j+1,k)]-1

					x6=estaeneltablero(matriz,fil,col,j+1,k+1)
					if x6==True and (j+1,k+1) not in aquihaymina: 
						dic[(j+1,k+1)]=dic[(j+1,k+1)]-1

				else:
					x1=estaeneltablero(matriz,fil,col,j,k-1)
					if x1==True and (j,k-1) not in aquihaymina: 
						dic[(j,k-1)]=dic[(j,k-1)]-1

					x2=estaeneltablero(matriz,fil,col,j,k+1)
					if x2==True and (j,k+1) not in aquihaymina: 
						dic[(j,k+1)]=dic[(j,k+1)]-1

					x3=estaeneltablero(matriz,fil,col,j-1,k-1)
					if x3==True and (j-1,k-1) not in aquihaymina: 
						dic[(j-1,k-1)]=dic[(j-1,k-1)]-1

					x4=estaeneltablero(matriz,fil,col,j-1,k)
					if x4==True and (j-1,k) not in aquihaymina: 
						dic[(j-1,k)]=dic[(j-1,k)]-1

					x5=estaeneltablero(matriz,fil,col,j+1,k-1)
					if x5==True and (j+1,k-1) not in aquihaymina: 
						dic[(j+1,k-1)]=dic[(j+1,k-1)]-1

					x6=estaeneltablero(matriz,fil,col,j+1,k)
					if x6==True and (j+1,k) not in aquihaymina: 
						dic[(j+1,k)]=dic[(j+1,k)]-1

	return matriz

#Funcion para comprobar si el jugador ha ganado
def heGanado(matriz, minas,fil,col):
	global estadopartida
	global numarcadas
	if estadopartida!=2:
		for i in range(fil):
			for j in range(col):
				if numarcadas==minas and matriz[i][j]=="X" or matriz[i][j]==" ":
					estadopartida=1
				else:
					estadopartida=0




#Funcion que actualiza el tablero en funcion del estado de la partida (si se ha ganado o perdido)
def estadoJuego(matriz, aquihaymina,fil,col):
	global estadopartida

	if estadopartida==2:
		for i in range(fil):
			for j in range(col):
				if matriz[i][j]=="X" and (i,j) not in aquihaymina:
					matriz[i][j]="#"
				elif matriz[i][j]!="X" and (i, j) in aquihaymina:
					matriz[i][j]="*"
				elif matriz[i][j]=="X" and (i, j) in aquihaymina:
					matriz[i][j]="X"
				else:
					matriz[i][j]=" "
	elif estadopartida==1:
		print("¡HAS GANADO!")
		for i in range(fil):
			for j in range(col):
				if matriz[i][j]=="X" and (i,j) not in aquihaymina:
					matriz[i][j]="#"
				elif matriz[i][j]!="X" and (i, j) in aquihaymina:
					matriz[i][j]="*"
				elif matriz[i][j]=="X" and (i, j) in aquihaymina:
					matriz[i][j]="X"
				else:
					matriz[i][j]=" "
		
		
	else:
		pass

#Imprime el tablero, con el tiempo y las celdas marcadas
def printMap(matriz,fil,col,filas,columnas):
	global numarcadas
	tiempo_final=time()
	tiempo_global=tiempo_final-tiempo_inicial
	print("CELDAS MARCADAS: ", end="")
	print(numarcadas, end="   ")
	print("||", end="   ")
	print("TIEMPO: ", end="")
	print(tiempo_global)

	print("   ", end="")
	for a in range(col):
		print("  "+str(columnas[a]), end="   ")
	print(" ")

	for i in range(fil):
		if i%2==0:
			print (filas[i]+"   "+str(matriz[i]))
		else:
			print (filas[i]+" "+str(matriz[i]))


bandera=False

while bandera==False:
	print (" ")
	print ("BUSCAMINAS")
	print ("------------------------------------")

	print ("1. Principiante (9x9, 10 minas)")
	print ("2. Intermedio (16x16, 40 minas)")
	print ("3. Experto (16x30, 99 minas)")
	print ("4. Leer de fichero")
	print ("5. Salir")


	print("Introduzca la opcion deseada: ")
	stringopcion=int(raw_input())
	if stringopcion<1 or stringopcion>6:
		print("Opcion no valida. Introduzca otra: ")
		stringopcion=int(raw_input())

	if stringopcion==1:
 		fil=9
 		col=9
 		minas=10
	elif stringopcion==2:
 		fil=16
 		col=16
 		minas=40
	elif stringopcion==3:
 		fil=16
 		col=30
 		minas=99
	elif stringopcion==4:
 		#Para leer los datos del fichero, los convertimos a una lista y vamos separando los datos y localizando las coordenadas de las minas
 		print ("Introduzca el nombre del fichero con el tablero a representar: ")
		nombre_fichero=raw_input()
		fich = open(nombre_fichero, 'r')
		lins = fich.read().split('\n')
		fich.close()
		stringfilcol=lins[0]
		fil=int(stringfilcol[0:1])
		col=int(stringfilcol[2:3])
		aquihaymina=[]
		lins.pop(0)
		cuentafilas=-1
		for a in lins:
			analizando=a
			cuentafilas=cuentafilas+1
			cuentacolumnas=-1
 			for b in analizando:
 				cuentacolumnas=cuentacolumnas+1
 				if b=="*":
 					aquihaymina.append((cuentafilas,cuentacolumnas))
 		minas=len(aquihaymina)
	elif stringopcion==5:
 		sys.exit()
		
	if stringopcion==1 or stringopcion==2 or stringopcion==3:
		mineMap(fil,col,matriz)
		printMap(matriz,fil,col,filas,columnas)
		aquihaymina=colocarminas(matriz,col,fil,minas)
		
		ponernumeros(matriz,fil,col,aquihaymina,dic)


		while estadopartida==0: #La partida continua mientras el jugador no haya ganado o perdido
			stringjugada=IntroducirJugadas()
			listastring=cortacadenas(stringjugada)
			listadefinitiva=evaluarcadenas(listastring,dicminus,dicmayus)
			matriz=cambiarCeldas(matriz,listadefinitiva,aquihaymina,fil,col,minas,dic)
			heGanado(matriz,minas,fil,col)
			estadoJuego(matriz,aquihaymina,fil,col)
			printMap(matriz,fil,col,filas,columnas)


	elif stringopcion==4:
		#La estructura de la opcion 4 del tablero es distinta ya que las minas no hay que generarlas aleatoriamente, la lista aquihaymina te la proporciona el fichero
		mineMap(fil,col,matriz)
		printMap(matriz,fil,col,filas,columnas)
		
		ponernumeros(matriz,fil,col,aquihaymina,dic)

		while estadopartida==0:
			stringjugada=IntroducirJugadas()
			listastring=cortacadenas(stringjugada)
			listadefinitiva=evaluarcadenas(listastring,dicminus,dicmayus)
			matriz=cambiarCeldas(matriz,listadefinitiva,aquihaymina,fil,col,minas,dic)
			heGanado(matriz,minas,fil,col)
			estadoJuego(matriz,aquihaymina,fil,col)
			printMap(matriz,fil,col,filas,columnas)


	








