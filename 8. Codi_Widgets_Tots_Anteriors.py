import tkinter as tk

class Valor:
    def __init__(self):
        self.value = 0
    def getvalue(self):
        return self.value
     

def gui(valor):
    tria.value = valor

def Cubs(cadena):
    cadena = cadena.split(',')
    llista = [int(element) for element in cadena]
    suma = 0
    for element in llista:
        suma += element ** 3
    return suma

def Quadrats(cadena):
    cadena = cadena.split(',')
    llista = [int(element) for element in cadena]
    suma = 0
    for element in llista:
        suma += element ** 2
    return suma

def Allista(cadena):
    return cadena.split()

def majuscules(cadena):
    return cadena.upper()


def executa():
    if tria.value == 1:
        labelresultat.config(text = majuscules(entry1.get()))    
        text1.insert(tk.END, f"{majuscules(entry1.get())}\n") 
        listbox1.insert(tk.END, f"{majuscules(entry1.get())}\n")
    elif tria.value == 2:
        labelresultat.config(text = Allista(entry1.get()))    
        text1.insert(tk.END, f"{Allista(entry1.get())}\n") 
        listbox1.insert(tk.END, f"{Allista(entry1.get())}\n")

    elif tria.value == 3:
        labelresultat.config(text = Quadrats(entry1.get()))    
        text1.insert(tk.END, f"{Quadrats(entry1.get())}\n") 
        listbox1.insert(tk.END, f"{Quadrats(entry1.get())}\n")

    elif tria.value == 4:
        labelresultat.config(text = Cubs(entry1.get()))    
        text1.insert(tk.END, f"{Cubs(entry1.get())}\n") 
        listbox1.insert(tk.END, f"{Cubs(entry1.get())}\n")

def neteja():
    labelresultat.config(text = "")
    entry1.delete(0,tk.END)
    text1.delete('1.0', tk.END)
    listbox1.delete(0, tk.END)


tria = Valor()

# inicializador de root
root = tk.Tk()
amplada = root.winfo_screenwidth()
alcada = root.winfo_screenheight()
strink = '{}x{}'.format(amplada,alcada)
root.geometry(strink)
root.attributes('-fullscreen',True)

# inicializador Frame
frame1 = tk.Frame(root,bg='orange')
frame1.place(x=0, y=0, width = amplada, height = alcada)





#Definicio de Widget Text Label
labeltext1 = tk.Label(frame1, text = "Exemple Text", bg = frame1.cget('bg'))
labeltext1.place( x = 2.5 * amplada//10, y = 1.5*alcada//10, anchor = tk.CENTER)

#Definicio de Widget Text
text1 = tk.Text(frame1)
text1.place( x = 2.5 * amplada//10, y = 4*alcada//10, width= 3*amplada//10, height= 4*alcada//10, anchor = tk.CENTER) 






#Definicio de Widget Listbox Label
labellistbox1 = tk.Label(frame1, text = "Exemple Listbox", bg = frame1.cget('bg'))
labellistbox1.place( x = 7.5 * amplada//10, y = 1.5*alcada//10, anchor = tk.CENTER) 


#Definicio de Widget Listbox
listbox1 = tk.Listbox(frame1)
listbox1.place( x = 7.5 * amplada//10, y = 4*alcada//10, width= 3*amplada//10, height= 4*alcada//10, anchor = tk.CENTER)






#Definicio de Widget Entry Label
labelentry1 = tk.Label(frame1, text = "Exemple Entry", bg = frame1.cget('bg'))
labelentry1.place(x = 5 * amplada//10, y = 6.5 * alcada // 10, anchor = tk.CENTER)

#Definicio de Widget Entry
entry1 = tk.Entry(frame1)
entry1.place( x = 5 * amplada//10, y = 7.5 * alcada // 10, width= 8 * amplada // 10, height= 0.5 * alcada // 10, anchor = tk.CENTER) 





#Definicio de Widget Button Label
labelboto1 = tk.Label(frame1, text = "Exemple Botó", bg = frame1.cget('bg'))
labelboto1.place( x = 5 * amplada//10, y = 8 * alcada // 10, anchor = tk.CENTER)

#Definicio de Widget Button
boto1 = tk.Button(frame1, text = "Resultat", command = executa)
boto1.place(  x = 5 * amplada//10, y = 9 * alcada // 10, width= 1 * amplada // 10, height= 0.5 * alcada // 10, anchor = tk.CENTER)





#Definicio de Widget Label Resultat
labelresultat = tk.Label(frame1, text = "Es mostrarà el resultat", bg = frame1.cget('bg'))
labelresultat.place( x = 5 * amplada//10, y = 1 * alcada // 10, anchor = tk.CENTER)


#Definicio de Widget Button
boto2 = tk.Button(frame1, text = "Neteja Widgets", command = neteja)
boto2.place(  x = 4 * amplada//10, y = 9 * alcada // 10, width= 1 * amplada // 10, height= 0.5 * alcada // 10, anchor = tk.CENTER)


#Definicio de Menu
barramenu =tk.Menu(root)
menuarxiu= tk.Menu(barramenu, tearoff=0)
menuarxiu.add_command(label="Exercici Majúscules", command=lambda : gui(1))
menuarxiu.add_command(label="Exercici a Llista", command=lambda : gui(2))
menuarxiu.add_command(label="Suma Quadrats", command=lambda : gui(3))
menuarxiu.add_command(label="Suma Cubs", command=lambda : gui(4))
barramenu.add_cascade(label="Tria Exercici", menu=menuarxiu)
'''
menuedicio = tk.Menu(barramenu, tearoff=0)
menuedicio.add_command(label="Retalla", command=hello)
menuedicio.add_command(label="Copia", command=hello)
menuedicio.add_command(label="Enganxa", command=hello)
barramenu.add_cascade(label="Edita", menu=menuedicio)
menuajuda = tk.Menu(barramenu, tearoff=0)
menuajuda.add_command(label="About", command=hello)
barramenu.add_cascade(label="Ajuda", menu=menuajuda)
'''
root.config(menu=barramenu)


# mantenedor de root
root.mainloop()
