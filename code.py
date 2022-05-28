from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import filedialog
from turtle import bgcolor, color
from PIL import Image, ImageTk
from setuptools import Command
from PIL import ImageFont
from PIL import ImageDraw



root = Tk()
root.geometry('700x700')
root.config(bg='#A9CDD5')

imag= PhotoImage(file = 'C:\\Users\\user\\python files\\ala.png')
root.iconphoto(False, imag)

t=Text(root, height=5, width=4)
l=Label(root,text = '#Select a file to use other commands', background='#D2E6FF', borderwidth=3)
l.config(font=('Courier', 10))
l.grid(row=1, column=1)


class Open:
    def open_file():
        global filepath
        filepath = filedialog.askopenfilename(initialdir='C:\\Users\\user\\python files', title='Open file')
        photo = Image.open(filepath)

    click_btn= PhotoImage(file='C:\\Users\\user\\Desktop\\final project\\image3.png')
    my_lbl = Label(text = "Click to the button to open file", image=click_btn)    
    global open_button
    open_button = Button(root,image=click_btn, text = '1. SELECT FILE',compound = BOTTOM, command=open_file,
            borderwidth=5, height=90, width=90)
    open_button.grid(row=1, column=2,ipadx=10, ipady=10, sticky='nsew')



class Grayscale:
    def grey():
        my_pic= Image.open(filepath)
        bw_image = my_pic.convert('L')
        bw_image.show() 
        bw_image.save('image.png')

    
    click_gray = PhotoImage(file='C:\\Users\\user\\Desktop\\final project\\bl.png')
    my_lbl3 = Label(text = "lknlk", image=click_gray)
    global gray_button
    gray_button = Button(root, text= "GRAYSCALE", compound =BOTTOM, image = click_gray, command = grey, borderwidth=5, height=85, width=85)
    gray_button.grid(row=3, column=2, sticky='nsew')



class Watermark:
    def add_watermark():
        im = Image.open(filepath)
        w, h = im.size
        color = 'black'
        draw = ImageDraw.Draw(im)
        text = "AlaToo"
        font = ImageFont.truetype('arial', (w+h)//22)
        textwidth, textheight = draw.textsize(text, font)
        # calculate the x,y coordinates of the text
        margin = 20
        x = w - textwidth - margin
        y = h - textheight - margin
        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font, fill='#FA05B0', stroke_fill='purple', bgcolor = 'grey')
        im.show()
        im.save('with_watermark.png')

    click_wtm = PhotoImage(file= 'C:\\Users\\user\\Desktop\\final project\\water.png')
    my_lbl1 = Label(text = "Click to the button to add watermark", image=click_wtm )
    my_lbl1.config(text="You added watermark")
    global watermark_button
    watermark_button = Button(root, text = 'ADD WATERMARK',compound = BOTTOM, image = click_wtm, command=add_watermark, borderwidth=5,height=85, width=85)
    watermark_button.grid(row=2, column=2, sticky='nsew')



class Resize:
    def resized():
        my_pic= Image.open(filepath) 
        resized = my_pic.resize((int(my_box1.get()),int(my_box.get())), Image.Resampling.LANCZOS)  
        new_pic = ImageTk.PhotoImage(resized)
        
        label1 = Label(image=new_pic)
        label1.image = new_pic
        label1.grid(row=20, column=2)

    def get_width():
        try:
            int(my_box1.get())
            answer1.config(text="Available value!", bg='#A9CDD5')
        except ValueError:
            print("Width can be only Number")

    def get_height():
        try:
            int(my_box.get())
            answer2.config(text="Available value!", bg='#A9CDD5')
        except ValueError:
            print("Height can be only Number")

    click_crop = PhotoImage(file='C:\\Users\\user\\Desktop\\final project\\crop.png')
    my_lbl2 = Label(text = "Click to crop", image=click_crop )
    global crop_button
    crop_button = Button(root, text = 'CROP', compound=BOTTOM,image=click_crop, command=resized, borderwidth=5,height=85, width=85)
    crop_button.grid(row=13, column=2, sticky='nsew', ipadx=10, ipady=10)

    global my_box1
    my_box1 = Entry(root, bg='#A6BFFF')
    my_box1.grid(row=5, column=2)
    global my_button
    my_button = Button(root, text="Enter the width to crop", command=get_width)
    my_button.grid(row=6, column=2, sticky='nsew')

    global answer1
    answer1 = Label(root, text='', bg='#A9CDD5')
    answer1.grid(row=7, column=2,sticky='nsew' )

    global my_box
    my_box = Entry(root, bg='#A6BFFF')
    my_box.grid(row=10, column=2)
    global my_button2
    my_button2 = Button(root, text="Enter the height to crop", command=get_height)
    my_button2.grid(row=11, column=2, sticky='nsew')
    
    global answer2
    answer2 = Label(root, text='', bg='#A9CDD5')
    answer2.grid(row=12,  column=2, sticky='nsew')


click_quit = PhotoImage(file='C:\\Users\\user\\Desktop\\final project\\quit.png')
my_lbl2 = Label(text = "Click to quit", image=click_quit )
button_quit = Button(root, text = 'QUIT',compound = BOTTOM, image = click_quit, command=root.destroy, borderwidth=5, height=85, width=85)
button_quit.grid(row=14, column=2, sticky='nsew')



button_list =[open_button, watermark_button, gray_button, crop_button, my_button, my_button2]

row_number = 0
for button in button_list:
    Grid.rowconfigure(root, row_number, weight=1)
    row_number+=1
    
column_number=0
for button in button_list:
    Grid.columnconfigure(root, column_number, weight=1)
    column_number+=1


root.mainloop()




