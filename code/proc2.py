from PIL import Image, ImageTk
import tkinter as tk
im = Image.open("../dataset/misc/4.1.07.tiff")
root = tk.Tk()
root.title("Test")
photo = ImageTk.PhotoImage(im)
l = tk.Label(root, image = photo )
l.pack()
l.photo = photo
root.mainloop()
