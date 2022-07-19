import tkinter as tk


def executa():
    labelresultat.config(text = entry1.get())    
    text1.insert(tk.END, f"{entry1.get()}\n") 
    listbox1.insert(tk.END, f"{entry1.get()}\n")

def neteja():
    labelresultat.config(text = "")
    entry1.delete(0,tk.END)
    text1.delete('1.0', tk.END)
    listbox1.delete(0, tk.END)


    
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
labelresultat = tk.Label(frame1, text = "Es mostrarà el resultat", bg = frame1
                         .cget('bg'))
labelresultat.place( x = 5 * amplada//10, y = 1 * alcada // 10, anchor = tk.CENTER)


#Definicio de Widget Button
boto2 = tk.Button(frame1, text = "Neteja Widgets", command = neteja)
boto2.place(  x = 4 * amplada//10, y = 9 * alcada // 10, width= 1 * amplada // 10, height= 0.5 * alcada // 10, anchor = tk.CENTER)





# mantenedor de root
root.mainloop()
