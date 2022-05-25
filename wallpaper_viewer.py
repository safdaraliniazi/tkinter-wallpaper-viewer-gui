from tkinter import *
from PIL import ImageTk, Image
import os

def nextimg():
    global counter
    img_label.config(image = image_array[counter%len(image_array)])
    root.title(image_array[counter%len(image_array)])                                     #changes application title to image number , helps to keep track of current image
    root.configure(background = colours_array[counter %len(colours_array)])               #changes bg colour everytime from colours_array
    counter = counter +1



colours_array = ['black','blue','green','red','white']
counter  = 1
root = Tk()
root.title('Wallpaper viewer')
root.iconbitmap('myicon.ico')
root.geometry('300x400')
root.configure(background='black', cursor = 'heart' ,  ) 
files = os.listdir('wallpaper')
image_array = []
for file in files:
    img = Image.open(os.path.join('wallpaper',file))
    img = img.resize((200,300))
    image_array.append(ImageTk.PhotoImage(img))

img_label  = Label(root , image = image_array[0])
img_label.pack(pady = 20)

next_btn = Button(root,text = 'Next' , bg = 'white' , fg = 'black' , width=28 ,height= 2 , command = nextimg)
next_btn.pack()
root.mainloop()