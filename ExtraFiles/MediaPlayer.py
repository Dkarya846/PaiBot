import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
import pyglet
from tkinter import ttk
from ttkthemes import themed_tk as tk
from mutagen.mp3 import MP3
from pygame import mixer


class Media:
        def musicPlayer(self, music_player, window):
                #music_player = Tk()#tk.ThemedTk()
                #music_player.resizable(False,False)
                #music_player.geometry("480x700")
                music_player.config(bg="#163A54")
                #music_player.get_themes()                 # Returns a list of all themes that can be set
                #music_player.set_theme("radiance")         # Sets an available theme


                window.title("Audio Player")
                window.iconbitmap('PaiBot.ico')

                greet = Label(music_player,text="Music Player",bg="#163A54",fg = "White",font=("Agency FB",25))
                greet.pack(pady=15)


                path_ico=PhotoImage(file="MediaPlayer/Music.png")

                icon1 = Label(music_player,image=path_ico,bg="#163A54")
                icon1.image=path_ico
                icon1.place(x=130,y=15)

                statusbar = ttk.Label(music_player, text="Welcome  Pai_Memeber", relief=SUNKEN, anchor=W, font='Times 10 italic')
                statusbar.pack(side=BOTTOM, fill=X)

                playlist = []
                def browse_file():
                        global filename_path
                        filename_path = filedialog.askopenfilename()
                        add_to_playlist(filename_path)

                        mixer.music.queue(filename_path)


                def add_to_playlist(filename):
                        filename = os.path.basename(filename)
                        index = 0
                        playlistbox.insert(index, filename)
                        playlist.insert(index, filename_path)
                        index += 1

                mixer.init()  # initializing the mixer


                Play_list = Frame(music_player,bg="white", width=300, height=400)
                Play_list.place(x=90, y=127)


                statusbar1 =Label(music_player, text="        Song's PlaylisT         ",bg="#163A54",fg="white",font=("Agency FB",20))
                statusbar1.place(x=140,y=88)


                playlistbox = Listbox(Play_list,width=300, height=400)
                playlistbox.place(x=0,y=0)


                addBtn = Button(music_player, text="+ Add a Song", command=browse_file)
                addBtn.place(x=140,y=530)


                def del_song():
                        selected_song = playlistbox.curselection()
                        selected_song = int(selected_song[0])
                        playlistbox.delete(selected_song)
                        playlist.pop(selected_song)


                delBtn = Button(music_player, text="- Del a Song", command=del_song)
                delBtn.place(x=250,y=530)



                def play_music(self):
                        time.sleep(1)
                        selected_song = playlistbox.curselection()
                        selected_song = int(selected_song[0])
                        play_it = playlist[selected_song]
                        mixer.music.load(play_it)
                        mixer.music.play()
                        statusbar['text'] = "Playing music" + ' - ' + os.path.basename(play_it)
                        


                def stop_music():
                        mixer.music.stop()
                        statusbar['text'] = "Music Stopped"


                paused = FALSE


                def pause_music(self):
                        global paused
                        paused = TRUE
                        mixer.music.pause()
                        statusbar['text'] = "Music Paused"


                def rewind_music(self):
                        play_music()
                        statusbar['text'] = "Music Rewinded"


                def set_vol(val):
                        volume = float(val) / 100
                        mixer.music.set_volume(volume)
                        # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1


                muted = FALSE


                def mute_music(self):
                        global muted
                        if muted:  # Unmute the music
                                mixer.music.set_volume(0.7)
                                volumeBtn.configure(image=volumePhoto)
                                scale.set(70)
                                muted = FALSE
                        else:  # mute the music
                                mixer.music.set_volume(0)
                                volumeBtn.configure(image=mutePhoto)
                                scale.set(0)
                                muted = TRUE

                playPhoto = PhotoImage(file='MediaPlayer/Play.png')
                playBtn = Label(music_player, image=playPhoto,bg="white")
                playBtn.place(x=100,y=580)
                playBtn.bind("<Button-1>",play_music)


                stopPhoto = PhotoImage(file='MediaPlayer/stop.png')
                stopBtn = Label(music_player, image=stopPhoto,bg="white")
                stopBtn.place(x=200,y=580)
                stopBtn.bind("<Button-1>",stop_music)


                pausePhoto = PhotoImage(file='MediaPlayer/Pause.png')
                pauseBtn = Label(music_player, image=pausePhoto,bg="white")
                pauseBtn.place(x=300,y=580)
                pauseBtn.bind("<Button-1>",pause_music)

                # Bottom Frame for volume, rewind, mute etc.


                rewindPhoto = PhotoImage(file='MediaPlayer/rewind.png')
                rewindBtn = Label(music_player, image=rewindPhoto)
                rewindBtn.place(x=50,y=580)
                rewindBtn.bind("<Button-1>",rewind_music)

                mutePhoto = PhotoImage(file='MediaPlayer/mute.png')
                volumePhoto = PhotoImage(file='MediaPlayer/volume.png')
                volumeBtn = Button(music_player, image=volumePhoto, command=mute_music,bg="#163A54")
                volumeBtn.place(x=380,y=580)

                scale = ttk.Scale(music_player, from_=0, to=100, orient=VERTICAL, command=set_vol)
                scale.set(70)  # implement the default value of scale when music player starts
                mixer.music.set_volume(0.7)
                scale.place(x=380,y=500)
                def on_closing():
                        stop_music()
                        music_player.destroy()


                #music_player.protocol("WM_DELETE_WINDOW", on_closing)
                music_player.mainloop()
