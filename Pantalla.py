import tkinter as tk

def validar_dni(lista):
    for cadena in lista:
        if not cadena.isalpha() and not cadena.isdigit() and cadena[0:-1].isdigit() and cadena[-1].isalpha():
            listbox2.insert(tk.END, cadena)





def divisor(numero):
    
    divisor = 1

    while divisor <= numero:
        if numero % divisor == 0:
            listbox3.insert(tk.END,divisor)
        divisor += 1
    
def neteja():
    listbox2.delete(0,tk.END)    
    

# inicializador de root
root = tk.Tk()
amplada = root.winfo_screenwidth()
alcada = root.winfo_screenheight()
strink = '{}x{}'.format(amplada,alcada)
root.geometry(strink)
root.attributes('-fullscreen',True)

#EJERCICIO 1
frame1 = tk.Frame(root,bg='orange')
frame1.place(x=0, y=0, width = 5 * amplada // 10, height = 5 * alcada // 10)


#Definicio de Widget Text Label
labeltext1 = tk.Label(frame1, text = "EJERCICIO 1", font = ("Arial", 25), bg = frame1.cget('bg'))
labeltext1.place( x = 2.5 * amplada // 10, y = 0.5 * alcada // 10, anchor = tk.CENTER)

#Definicio de Widget Listbox
listbox1 = tk.Listbox(frame1,font = ("Arial", 15),bg = 'grey')
listbox1.place( x = 1.5 * amplada//10, y = 3*alcada//10, width = amplada // 10, height = alcada // 5, anchor = tk.CENTER)
cadena = "38206257K asdgf 38106382M 1203535 77885975V theend 2b3n V6568776"
lista= cadena.split()
for elemento in lista:
    listbox1.insert(tk.END,elemento)


listbox2 = tk.Listbox(frame1,font = ("Arial", 15))
listbox2.place( x = 3.5 * amplada//10, y = 3*alcada//10, width = amplada // 10, height = alcada // 5, anchor = tk.CENTER)
#lista2 = 
#listbox2.insert(tk.END,lista2)
#Definicio de Widget Button

boto1 = tk.Button(frame1, text = "Ejecutar", font = ('Arial', 12),command = lambda : validar_dni(lista))
boto1.place(  x = 1.5 * amplada//10, y = 4.5 * alcada // 10, width = amplada // 20, height = alcada // 20, anchor = tk.CENTER)


boto2 = tk.Button(frame1, text = "Limpiar", font = ('Arial', 12), command = neteja)
boto2.place(  x = 3.5 * amplada//10, y = 4.5 * alcada // 10, width = amplada // 20, height = alcada // 20, anchor = tk.CENTER)



frame2 = tk.Frame(root,bg='blue')
frame2.place(x= 5 * amplada // 10, y=0, width = 5 * amplada // 10, height = 5 * alcada // 10)


labeltext2 = tk.Label(frame2, text = "EJERCICIO 2", font = ("Arial", 25), bg = frame2.cget('bg'))
labeltext2.place( x = 2.5 * amplada // 10, y = 0.5 * alcada // 10, anchor = tk.CENTER)



#Definicio de Widget Entry
entry1 = tk.Entry(frame2)

entry1.place( x = 1.5 * amplada//10, y = 3 * alcada//10, width= 2*amplada//10, height= 0.5 * alcada//10, anchor = tk.CENTER) 

'''
text1 = tk.Text(frame2)
text1.place( x = 1.5 * amplada//10, y = 3 * alcada//10, width= 2*amplada//10, height= 0.5 * alcada//10, anchor = tk.CENTER) 
'''

labeltext3 = tk.Label(frame2, text = "DIVISORES", font = ("Arial", 18), bg = frame2.cget('bg'))
labeltext3.place( x = 3.5 * amplada // 10, y = 2.8 * alcada // 10, anchor = tk.CENTER)

listbox3 = tk.Listbox(frame2,font = ("Arial", 15))
listbox3.place( x = 3.5 * amplada//10, y = 3*alcada//10, width = amplada // 10, height = alcada // 5, anchor = tk.CENTER)

#Definicio de Widget Button



boto3 = tk.Button(frame2, text = "Ejecutar", font = ('Arial', 12),command = lambda : divisor(int(entry1.get())))
boto3.place(  x = 1.5 * amplada//10, y = 4.5 * alcada // 10, width = amplada // 20, height = alcada // 20, anchor = tk.CENTER)

boto4 = tk.Button(frame2, text = "Limpiar", font = ('Arial', 12), command = neteja)
boto4.place(x = 3.5 * amplada//10, y = 4.5 * alcada // 10, width = amplada // 20, height = alcada // 20, anchor = tk.CENTER)

'''

frame3 = tk.Frame(root,bg='red')
frame3.place(x=0, y= 5 * alcada // 10, width = 5 * amplada // 10, height = 5 * alcada // 10)


frame4 = tk.Frame(root,bg='green')
frame4.place(x= alcada, y=5 * alcada// 10, width = 5 * amplada // 10, height = 5 * alcada // 10)

'''



root.mainloop()

'''
#Ejercicio 1
cadena = "38206257K asdgf 38106382M 1203535 77885975V theend 2b3n V6568776"
lista= cadena.split()
print(lista)


lista2= []
for cadena in lista:
    if not cadena.isalpha() and not cadena.isdigit() and cadena[0:-1].isdigit() and cadena[-1].isalpha():
        lista2.append(cadena)
print(lista2)
'''












'''
#Ejercicio 2
try:
    numero = int(input(""))

    divisor = 1
    resultado = []

    while divisor <= numero:
        if numero % divisor == 0:
            resultado.append(divisor)
        divisor += 1
    print(resultado)   	
except:
    print("eso no es numero")






#labeltext1.place( x = 2.5 * amplada//10, y = 1.5*alcada//10, anchor = tk.CENTER)
'''
