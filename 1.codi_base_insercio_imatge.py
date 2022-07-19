import tkinter as tk
import random
from PIL import ImageTk, Image




def insertaimatge():
      image = Image.open("forest.png")
      photo = ImageTk.PhotoImage(image.resize((196, 196), Image.ANTIALIAS))

      label = tk.Label(image=photo, bg='green')
      label.image = photo
      label.place( x = 5 * amplada//10, y = 5 * alcada // 10, anchor = tk.CENTER)





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




#Definicio de Widget Button Label
labelboto1 = tk.Label(frame1, text = "Exemple Botó", bg = frame1.cget('bg'))
labelboto1.place( x = 5 * amplada//10, y = 8 * alcada // 10, anchor = tk.CENTER)




#Definicio de Widget Button
boto1 = tk.Button(frame1, text = "Resultat", command = insertaimatge)
boto1.place(  x = 5 * amplada//10, y = 9 * alcada // 10, width= 1 * amplada // 10, height= 0.5 * alcada // 10, anchor = tk.CENTER)




# mantenedor de root
root.mainloop()
