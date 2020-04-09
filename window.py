from tkinter import *

class window(Frame):

	def __init__(self,master):
		
		super().__init__(master)
		self._master = master
		self.pack()
		self._place_window()

		#master.attributes("-fullscreen", True) pour mettre en full screen
		#pour mettre en full screen
		
		#self.label1 = Button(self, text = "1").grid(row = 1, column = 2)
		#self.label2 = Button(self, text = "2").grid(row = 1, column = 1)
		#pour placer les elements dans la fenetre

	def _place_window(self):
		root.geometry("%dx%d" % (self.winfo_screenwidth(), self.winfo_screenheight()))
		#taille de la fenetre

root = Tk()
root.title("window")
app = window(root)
app.mainloop()
