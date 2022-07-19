import tkinter as tk
import matplotlib.pyplot as plt
import io

from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox

#FUNCIONES DEL MODULO

def insertaimatge():
    '''
    Función no propia, que inserta un fichero de imagen en pantalla
    '''
    image = Image.open('marcos.png')
    photo = ImageTk.PhotoImage(image.resize((196, 196), Image.ANTIALIAS))

    label = tk.Label(image=photo, bg='green')
    label.image = photo
    label.place( x = 5 * amplada//10, y = 5 * alcada // 10, anchor = tk.CENTER)

def grafic(resultado):
    '''
    Función no propia que crea un fichero gráfico con los resultados de la selección de datos 
    '''

   #PARAMETRES GENERALS DE LA FIGURA
    SMALL_SIZE = 15
    MEDIUM_SIZE = 15
    BIGGER_SIZE = 15
    plt.rc('font', size=SMALL_SIZE)         # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)    # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)   # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)   # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)   # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)   # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title

   #PARAMETRES DELS SUBGRAFICS

#    fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,15))
    fig, (ax1) = plt.subplots(1,figsize=(15,15))
#    fig.suptitle('Demografia')
    fig.suptitle(combo_poblacion.get())

    fig.tight_layout(pad=10.0) 
   
   # DIAGRAMA DE COLUMNES
    dades = resultado
    ind=range(len(dades))
    width = 0.35
    rects1 = ax1.bar(ind, dades, width, color='r')
    ax1.set_ylabel('Habitants')
    ax1.set_xticks(ind)
    ax1.yaxis.set_major_locator(plt.NullLocator())
    ax1.set_xticklabels(tupla)
    ax1.set_yticklabels([])
    for rect in rects1:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2., height,'%d' % int(height),ha='center', va='bottom')
    ax1.spines['right'].set_visible(False) 
    ax1.spines['left'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    nombreFichero = 'marcos.png'
    plt.savefig('marcos.png'.format({var_poblacion}), bbox_inches='tight')
    plt.close(fig)

def captura_combos():
    '''
    Captura los valores seleccionados en los combos y los asigna a variables.
    Controla errores en la selección de datos
    Recoge el valor devuelto por la consulta al fichero,
    crea el fichero con el gráfico (función grafic) y lo presenta en pantalla (función insertaimatge)
    '''
    var_provincia = combo_provincia.get()
    var_poblacion = combo_poblacion.get()
    var_sexo = combo_sexo.get()
    var_desde = combo_edad_desde.get()
    var_hasta = combo_edad_hasta.get()

    if var_hasta < var_desde:
       messagebox.showinfo(
       message=f"{var_desde} no puede ser mayor que {var_hasta}",
       title="Error"
       )

    sexo = []
    for elemento in llista_registres:
        if elemento[2] == var_poblacion:
            if elemento[4] == 'homes' and convertir_edad_dato(elemento[3]) == var_desde:
                sexo.append(int(elemento[7]))
            elif elemento[4] == 'dones' and convertir_edad_dato(elemento[3]) == var_desde:
                sexo.append(int(elemento[7]))
            elif elemento[4] == 'total' and convertir_edad_dato(elemento[3]) == var_desde:
                sexo.append(int(elemento[7]))
            else:
                pass

    print(sexo)
 
    resultado = sexo

    '''    
    for registro in llista_registres:
        if var_poblacion == registro[2] and var_sexo == registro[4] and var_desde == convertir_edad_dato(registro[3]):
            resultado = int(registro[7])
    '''
    grafic(resultado)
    insertaimatge()
        
def convertir_edad_dato(dato):
    '''
    Función que limpia todo texto del campo 'edat' en el registro seleccionado de del fichero
    y devuelve el valor entero del registro seleccionado
    Devuelve el valor de la columna edad como un string
    '''
    valor = ""
    if not dato.isalpha():
            valor = dato.replace("anys","").replace("any","").replace(" ","").replace("omés","")
    return valor


def convertir_edad(nueva_lista):
    '''
    Función que limpia todo texto del campo 'edat' del fichero y devuelve una lista
    con los valores enteros de la columna edat
    '''
    new_registre = []
    for registre in nueva_lista:
        if not registre.isalpha():
            new_registre.append(int(registre.replace("anys","").replace("any","").replace(" ","").replace("omés","")))
    return new_registre

def neteja():  #de momento no funciona
    '''
    Función que deja en blanco todos los combo
    '''
    combo_provincia.delete(0,tk.END)
    combo_poblacion.delete(0,tk.END) 
    combo_sexo.delete(0,tk.END) 
    combo_edad_desde.delete(0,tk.END) 
    combo_edad_hasta.delete(0,tk.END) 

#DECLARACION DE VARIABLES GLOBALES DEL MODULO
resultado = []           #Toma el valor devuelto por la consulta hecha con la selección de los combos        
var_provincia =""       #Recoge el valor seleccionado en el combo combo_provincia
var_poblacion =""       #Recoge el valor seleccionado en el combo combo_poblacion
var_sexo =""            #Recoge el valor seleccionado en el combo combo_sexo
var_desde =""           #Recoge el valor seleccionado en el combo combo_edad_desde
var_hasta =""           #Recoge el valor seleccionado en el combo combo_edad_hasta

tupla = ('homes','dones','total')

#LECTURA DEL FICHERO ORIGEN DE LOS DATOS
poblacions = io.open("Poblacio_Municipis_2021.csv","r", encoding = 'UTF-8')
llista_registres = poblacions.readlines()

#CONVERSION DE LA CADENA CON LOS DATOS IMPORTADOS EN UNA LISTA
for pos in range(len(llista_registres)):
    llista_registres[pos] = llista_registres[pos].split(';')

poblacions.close()

# ASIGNACIONES DE VALORES PARA LOS COMBO
#   1. combo_provincia

set_provincias = list(set([element[1][:2] for element in llista_registres]))

dict_provincias = {}

for provincia in set_provincias:

    if provincia == '08':
        dict_provincias[provincia] = 'Barcelona'
    elif provincia == '17':
        dict_provincias[provincia] = 'Girona'
    elif provincia == '25':
        dict_provincias[provincia] = 'Lleida'
    elif provincia == '43':
        dict_provincias[provincia] = 'Tarragona'

#   2. combo_poblacion
    
set_poblaciones = list(set([element[2] for element in llista_registres]))

#   3. combo_sexo

set_sexo = list(set([element[4] for element in llista_registres])) 

#   4. combo_edad_desde y combo_edad_hasta
set_edad = convertir_edad(list(set([element[3] for element in llista_registres])))

# DIBUJO DE LA PANTALLA
root = tk.Tk()
amplada = root.winfo_screenwidth()
alcada = root.winfo_screenheight()
strink = '{}x{}'.format(amplada,alcada)
root.geometry(strink)
root.attributes('-fullscreen',True)

frame1 = tk.Frame(root,bg='light grey')
frame1.place(x=10, y=10, width =  9.9 * amplada // 10 , height = 9.9 * alcada // 10)

#DIBUJO DE LOS WIDGETS
label_titulo = tk.Label(frame1, text = "Población Municipios Catalunya 2021", font = ("Arial", 25), bg = frame1.cget('bg'), fg="black")
label_titulo.place( x = 5 * amplada // 10, y = 0.3 * alcada // 10 , anchor = tk.CENTER)

label_combo_provincia = tk.Label(frame1, text = "Provincia", font = ("Arial", 12), bg = frame1.cget('bg'), fg="black")
label_combo_provincia.place(x = amplada // 10, y = 0.9 * alcada // 10, anchor = 'w')

combo_provincia = ttk.Combobox(frame1, state="readonly", values = sorted(dict_provincias.values()))
combo_provincia.place(x = amplada // 10, y = alcada // 10)

label_combo_poblacion = tk.Label(frame1, text = "Poblacion", font = ("Arial", 12), bg = frame1.cget('bg'), fg="black")
label_combo_poblacion.place(x = 2 * amplada // 10, y = 0.9 * alcada // 10, anchor = 'w')

combo_poblacion = ttk.Combobox(frame1, state="readonly", values = sorted(set_poblaciones))
combo_poblacion.place(x = 2 * amplada // 10, y = alcada // 10)

label_combo_sexo = tk.Label(frame1, text = "Sexo", font = ("Arial", 12), bg = frame1.cget('bg'), fg="black")
label_combo_sexo.place(x = 3 * amplada // 10, y = 0.9 * alcada // 10, anchor = 'w')

combo_sexo = ttk.Combobox(frame1, state="readonly", values = sorted(set_sexo))
combo_sexo.place(x= 3 * amplada // 10, y =  alcada // 10)

label_combo_edad_desde = tk.Label(frame1, text = "Entre", font = ("Arial", 12), bg = frame1.cget('bg'), fg="black")
label_combo_edad_desde.place(x = 4 * amplada // 10, y = 0.9 * alcada // 10, anchor = 'w')

combo_edad_desde = ttk.Combobox(frame1, state="readonly", values = sorted(set_edad))
combo_edad_desde.place(x= 4 * amplada // 10, y = alcada // 10)

label_combo_edad_hasta = tk.Label(frame1, text = "Y", font = ("Arial", 12), bg = frame1.cget('bg'), fg="black")
label_combo_edad_hasta.place(x = 5 * amplada // 10, y = 0.9 * alcada // 10, anchor = 'w')

combo_edad_hasta = ttk.Combobox(frame1, state="readonly", values = sorted(set_edad))
combo_edad_hasta.place(x= 5 * amplada // 10, y =  alcada // 10)

boton_salir = tk.Button(frame1, text = "Salir", font = ('Arial', 12),command = root.destroy)
boton_salir.place(x = 3.5 * amplada//10, y = 4.5 * alcada // 10, width = amplada // 20, height = alcada // 20, anchor = tk.CENTER)

boton_ejecutar = tk.Button(frame1, text = "Ejecutar", font = ('Arial', 12),command = captura_combos)
boton_ejecutar.place(x =2.5 * amplada//10, y = 4.5 * alcada // 10, width = amplada // 20, height = alcada // 20, anchor = tk.CENTER)

boton_refrescar = tk.Button(frame1, text = "Nueva consulta", font = ('Arial', 8),command = neteja)
boton_refrescar.place(x = 3 * amplada//10, y = 4.5 * alcada // 10, width = amplada // 20, height = alcada // 20, anchor = tk.CENTER)

root.mainloop()

