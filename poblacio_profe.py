import io


def cerca(poblacio, sexe, edat1, edat2):
    consulta =[]
    suma = 0
    for registre in matriz:
        try:
            if (poblacio in registre[2]) and (sexe in registre[4])and (registre[3] >= edat1) and (registre[3] <= edat2):
                suma += registre[len(registre)-1]
        except:
            pass
    return f"En tal municipi {poblacio} hi ha {suma} {sexe} entre {edat1} i {edat2} anys"

# CONSEGUIR LA MATRIZ	
poblacions = io.open("Poblacio_Municipis_2021.csv",'r',encoding = 'utf-8')

matriz =  poblacions.readlines()

poblacions.close()
for pos in range(len(matriz)):
    matriz[pos] = matriz[pos].split(';')	

# PREPARAR LA MATRIZ
comptador = 0
for registre in matriz[1:]:
    if "total" not in registre[3]:
        registre[3] = int(registre[3].replace("anys","").replace("any","").replace("o més",""))
        registre[-1] = int(registre[-1])

        
#print(cerca('Badalona', 'dones', 0, 5))


    
while True:
    poblacio = input("Entra la poblacio")

    sexe = input("Entre el sexe")

    edat1 = int(input("Entre el mínim d'edat a consultar"))

    edat2 = int(input("Entre el màxim d'edat a consultar"))

    print(cerca(poblacio, sexe, edat1, edat2))


    continuar = input("Salir S").lower()

   
    if continuar == "s":
        print("Fins la propera consulta!")
        break

