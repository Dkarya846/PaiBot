import os
import threading
import time
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import pyglet
from tkinter import ttk
from ttkthemes import themed_tk as tk
from mutagen.mp3 import MP3
from pygame import mixer



class Music:
        def musicPlayer(self, music_player, window, name, city):
                bgColor = "#163A54"
                window.geometry("480x720")
                window.resizable(False, False)
                music_player.config(bg=bgColor)


                def mainPage():
                        from MainLayoutClass import MainLayout
                        #frame= Frame(window, width=480,height=720)
                        #frame.pack(fill="both", expand=True)
                        greet.place_forget()
                        icon1.place_forget()
                        statusbar.place_forget()
                        Play_list.place_forget()
                        statusbar1.place_forget()
                        playlistbox.place_forget()
                        addBtn.place_forget()
                        delBtn.place_forget()
                        playBtn.place_forget()
                        pauseBtn.place_forget()
                        stopBtn.place_forget()
                        volumeBtn.place_forget()
                        scale.place_forget()
                        backbtn.place_forget()
                        
                        mainFrame = MainLayout()
                        mainFrame.callMain(music_player, window, name, city)
        
                try:
                        music_player.config(bg="#163A54")
                        window.title("PaiBot Audio Player")
                        window.iconbitmap('PaiBot.ico')

                        greet = Label(music_player,text="Music Player",bg="#163A54",fg = "White",font=("Agency FB",25))
                        greet.place(x=180, y=15)


                        path_ico=PhotoImage(file="MediaPlayer/Music.png")

                        icon1 = Label(music_player,image=path_ico,bg="#163A54")
                        icon1.image=path_ico
                        icon1.place(x=130,y=15)

                        statusbar = Label(music_player, text="Welcome  Pai_Memeber", relief=FLAT, anchor=W, bg="#163A54", font=("Orbitron Black", 10), bd=0)
                        statusbar.place(x=0, y=700)

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


                        addBtn = Button(music_player, text="+ Add a Song", command=browse_file, relief = FLAT, bg=bgColor, activebackground=bgColor, bd=0, font=("Orbitron Black",10))
                        addBtn.place(x=100,y=530)


                        def del_song():
                                selected_song = playlistbox.curselection()
                                selected_song = int(selected_song[0])
                                playlistbox.delete(selected_song)
                                playlist.pop(selected_song)


                        delBtn = Button(music_player, text="- Delete a Song", command=del_song, relief = FLAT, bg=bgColor, activebackground=bgColor, bd=0, font=("Orbitron Black",10))
                        delBtn.place(x=250,y=530)



                        def play_music( ):
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


                        def pause_music():
                                global paused
                                paused = TRUE
                                mixer.music.pause()
                                statusbar['text'] = "Music Paused"


                        def rewind_music( ):
                                play_music()
                                statusbar['text'] = "Music Rewinded"


                        def set_vol(val):
                                volume = float(val) / 100
                                mixer.music.set_volume(volume)
                                # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1

                        global muted
                        muted = FALSE


                        def mute_music( ):
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
                        playBtn = Button(music_player, image=playPhoto, relief = FLAT, bg=bgColor, activebackground=bgColor, bd=0, command=play_music)
                        playBtn.place(x=100,y=640)
                        #playBtn.bind("<Button-1>",play_music)


                        stopPhoto = PhotoImage(file='MediaPlayer/stop.png')
                        stopBtn = Button(music_player, image=stopPhoto, relief = FLAT, bg=bgColor, activebackground=bgColor, bd=0, command=stop_music)
                        stopBtn.place(x=220,y=640)
                        #stopBtn.bind("<Button-1>",stop_music)


                        pausePhoto = PhotoImage(file='MediaPlayer/Pause.png')
                        pauseBtn = Button(music_player, image=pausePhoto, relief = FLAT, bg=bgColor, activebackground=bgColor, bd=0, command=pause_music)
                        pauseBtn.place(x=340,y=640)
                        #pauseBtn.bind("<Button-1>",pause_music)

                        # Bottom Frame for volume, rewind, mute etc.


                        
                        mutePhoto = PhotoImage(file='MediaPlayer/mute.png')
                        volumePhoto = PhotoImage(file='MediaPlayer/volume.png')
                        volumeBtn = Button(music_player, image=volumePhoto, command=mute_music, relief = FLAT, bg=bgColor, activebackground=bgColor, bd=0)
                        volumeBtn.place(x=440,y=665)

                        scale = ttk.Scale(music_player, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
                        scale.set(70)  # implement the default value of scale when music player starts
                        mixer.music.set_volume(0.7)
                        scale.place(x=200,y=600)
                        def on_closing():
                                stop_music()
                                music_player.destroy()
                except IndexError :
                        messagebox.showerror("PlayList Error","Add songs to the playlist first")
                except Exception as e:
                        messagebox.showerror("Error",str(e))
                back=PhotoImage(file="Logo/back.png")
                backbtn = Button(music_player, text="Back", image=back, font=("Yatra One",10), relief = FLAT, activebackground="#163A54", bd=0, bg="#163A54", command=mainPage)
                backbtn.image=back
                backbtn.place(x=0,y=665)
                #music_player.protocol("WM_DELETE_WINDOW", on_closing)
                music_player.mainloop()