import enum
from hashlib import new
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
from pytube import Playlist
import shutil
import os 
import glob



#Functions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

#def download_mp4():
    #get user path
    #get_link = link_field.get()
    #get selected path
   # user_path = path_label.cget("text")
   # screen.title('Downloading...')
    #Download Video
   # mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
   # vid_clip = VideoFileClip(mp4_video)
   # vid_clip.close()
    #move file to selected directory
    #shutil.move(mp4_video, user_path)
   # screen.title('Download Complete! Download Another File...')



def download_mp3():
    # get user path 
    get_link = link_field.get()
    user_path = path_label.cget('text')
    screen.title('Downloading....')

    #Download Audio
    mp3_audio = YouTube(get_link).streams.get_highest_resolution().download(output_path=user_path) 
    




    # save & rename file 
    base, ext = os.path.splitext(mp3_audio)
    new_file = base + '.m4a'
    os.rename(mp3_audio, new_file)
   # shutil.move(output, user_path)
    screen.title('Mp3 Download Complete!! Download Another File...')


def download_playlist_mp3():

    # get user path 
    get_link = link_field.get()
    user_path = path_label.cget('text')
    screen.title('Downloading....')

    # Download Playlist
    playlist = Playlist(get_link)
    PlayListLinks = playlist.video_urls
    N = len(PlayListLinks)
    
    # for loop
    for i,get_link in enumerate(PlayListLinks):
        d_audio = YouTube(get_link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=user_path)
        base, ext = os.path.splitext(d_audio)
        new_file = base + '.m4a'
        os.rename(d_audio, new_file)
        
           
    screen.title('Playlist Download Complete!')


# dimensions and title of the app 
screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='JAH.png')

#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=80, font=('Arial', 15) ) # input box
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_path)

#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label) 
canvas.create_window(250, 220, window=link_field) # input box widget 

#Download btns
#download_Mp4_btn = Button(screen, text="mp4 Download",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_mp4)
download_Mp3_btn = Button(screen, text="mp3 Download",bg='purple', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_mp3)
download_Playlist_btn = Button(screen, text="Playlist Download",bg='cyan', padx='22', pady='5',font=('Arial', 15), fg='black', command=download_playlist_mp3)

#add to canvas
canvas.create_window(250, 390, window=download_Mp3_btn)
canvas.create_window(250, 450, window=download_Playlist_btn)

#canvas.create_window(250, 550, window=download_Mp4_btn)

screen.mainloop()