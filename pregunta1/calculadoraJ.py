from tkinter import Button, Tk, Frame, Entry, END


ventana = Tk()
ventana.geometry ('258x335')#para su tamano
ventana.config(bg="white")
#ventana.iconbitmap(bitmap ='ico.ico')
ventana.resizable(0,0)
ventana.title('CALCULADORA HP')

class HoverButton(Button):
	def __inti__(self, master, **kw):
		Button.__init__(self, master=master, **kw)
		self.defaultBackground = self["background"]
		self.bind("<Ener>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self , e ):
		self ["background"] = self["activebackground"]

	def on_leave (self, e):
		self["background"] = self.defaultBackground

i=0
def obtener(dato):
	global i
	i+=1
	Resultado.insert(i,dato)

def operacion():
	global i

	ecuacion = Resultado.get()
	print("Entrar i>",i)

	print("ecuacion", ecuacion)
	
	try:
		result = str(round(eval(ecuacion),5))# funcion de python para evaluar string ("2+2"), roun para que solo aparesca5decimales
		print("Resultado",result)#para provar por consola el resultado
		Resultado.delete(0,END)
		Resultado.insert(0,result)
		longitud=len(result)
		i= longitud
	except:
		result='ERROR'
		Resultado.delete(0,END)
		Resultado.insert(0,result)
	

def borrar_uno():
	global i
	Resultado.delete(i,END)
	i=1

def borrar_todo():
	Resultado.delete(0, END)
	i=0

#Realmete ahora viene lo peludo
# es un poco de saber nmanejar lobotones

frame= Frame(ventana, bg='black', relief ="raised")
frame.grid(column=0, row=0,padx=1,pady=3)

Resultado= Entry(frame,bg='#9EF8E8', width=18,relief='groove', font= "Montserrat 16", justif='right')
Resultado.grid(column=0, row=0,columnspan=4, padx=10, pady=10)
#Resultado.place(x=20, y=60)

#para la primera fila
Button1 =HoverButton(frame, text ="1", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(1))
Button1.grid(column=0, row=1, pady=1,padx=3)

Button2 =HoverButton(frame, text ="2", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(2))
Button2.grid(column=1, row=1, pady=1,padx=1)

Button3 =HoverButton(frame, text ="3", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(3))
Button3.grid(column=2, row=1, pady=1,padx=1)

Button_suma =HoverButton(frame, text ="+", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener('+'))
Button_suma.grid(column=3, row=1, pady=2,padx=2)

#para la segunda fila

Button4 =HoverButton(frame, text ="4", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(4))
Button4.grid(column=0, row=2, pady=1,padx=3)

Button5 =HoverButton(frame, text ="5", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(5))
Button5.grid(column=1, row=2, pady=1,padx=1)

Button6 =HoverButton(frame, text ="6", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(6))
Button6.grid(column=2, row=2, pady=1,padx=1)

Button_resta =HoverButton(frame, text ="-", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener('-'))
Button_resta.grid(column=3, row=2, pady=2,padx=2)

#pra la tercera fila
Button7 =HoverButton(frame, text ="7", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(7))
Button7.grid(column=0, row=3, pady=1,padx=3)

Button8 =HoverButton(frame, text ="8", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(8))
Button8.grid(column=1, row=3, pady=1,padx=1)

Button9 =HoverButton(frame, text ="9", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(9))
Button9.grid(column=2, row=3, pady=1,padx=1)

Button_multiplica =HoverButton(frame, text ="*", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener('*'))
Button_multiplica.grid(column=3, row=3, pady=2,padx=2)
#paral la cuarta fila
Button0 =HoverButton(frame, text ="0", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(0))
Button0.grid(column=0, row=4, pady=1,padx=3)

Button5 =HoverButton(frame, text ="5", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(5))
Button5.grid(column=1, row=4, pady=1,padx=1)

Button6 =HoverButton(frame, text ="6", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener(6))
Button6.grid(column=2, row=4, pady=1,padx=1)

Button_divide =HoverButton(frame, text ="/", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:obtener('/'))
Button_divide.grid(column=3, row=4, pady=2,padx=2)

#para el igual y borrarr

Button_igual =HoverButton(frame, text ="=", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:operacion())
Button_igual.grid(column=0, row=5, pady=1,padx=1,columnspan=3)

Button_borrar =HoverButton(frame, text ="Borrar", borderwidth=2, height=2, width=5,font=('Comic sens MC',12,'bold'),relief= "raised", activebackground="aqua",bg='#999AB8', anchor="center", command=lambda:borrar_todo())
Button_borrar.grid(column=3, row=5, pady=2,padx=2,columnspan=2)
ventana.mainloop()