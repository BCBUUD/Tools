#!/bin/bash/python3
from hashlib import new
from tkinter import *
from tkinter import filedialog
import imdb
import webbrowser



# Backend logic to find Movies
def movie():
    movie = link_field.get()
    ia = imdb.IMDb() # imdb api 
    results = ia.search_movie(movie) # searching...
    mv = results[0] #First result
    URL = ia.get_imdbURL(mv) #URL for first result
    imdurl = URL
    vidurlf = imdurl.replace("https://www.imdb.com/title/","https://v2.vidsrc.me/embed/")
    x = vidurlf 
    webbrowser.open(x)



# backend to find shows 
def series():
    seris = link_field.get()
    ia = imdb.IMDb()
    results = ia.search_movie(seris)
    mv = results[0] #First result
    URL = ia.get_imdbURL(mv) #URL for first result
    imdurl = URL
    seasonx = Season_Number.get()
    episodex = Episode_number.get() 
    vidurlf = imdurl.replace("https://www.imdb.com/title/","https://v2.vidsrc.me/embed/")
    x = vidurlf + seasonx + "-" + episodex 
    webbrowser.open(x)



# Front-end Design of the app 
screen = Tk()
title = screen.title('Movie Finder v1.0')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='superjah.png')

#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=40, font=('Arial', 15) ) # input box
link_label = Label(screen, text="Enter Movie or Show: ", font=('Arial', 20))

Season_Number = Entry(screen, width=10, font=('Arial', 15) ) # season input 
Season_Label = Label(screen, text='Enter Season:', font=('Arial', 15))

Episode_number = Entry(screen, width=10, font=('Arial', 15) )# episode input 
Episode_Label = Label(screen, text='Enter Ep Number:', font=('Arial', 15))


#Add widgets to window 
canvas.create_window(250, 170, window=link_label) 
canvas.create_window(250, 220, window=link_field) # input box widget 

canvas.create_window(250, 250, window=Season_Label)
canvas.create_window(250, 280, window=Season_Number)

canvas.create_window(250, 310, window=Episode_Label) # input season box
canvas.create_window(250, 340, window=Episode_number)# input episode box

# btn
MovieBtn = Button(screen, text="Find Movie",bg='Blue', padx='22', pady='5',font=('Arial', 15), fg='#fff',command=movie)
EpBtn = Button(screen, text="Find Show",bg='orange', padx='22', pady='5',font=('Arial', 15), fg='#fff',command=series)



#add to canvas
canvas.create_window(250, 390, window=MovieBtn)
canvas.create_window(250, 450, window=EpBtn)
screen.mainloop()


