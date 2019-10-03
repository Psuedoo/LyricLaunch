import tkinter as tk
from tkinter import *
from SongHandler import *

LARGE_FONT= ("Verdana", 12)

song = "insert blah blah blah"
song = SongHandler().handle()

class LyricLaunch(tk.Tk):


    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Test")
        self.config(bg="black", width=500, height=300)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        startFrame = StartPage(container, self)
        lyricsFrame = LyricsPage(container, self)

        self.frames[StartPage] = startFrame
        self.frames[LyricsPage] = lyricsFrame

        startFrame.grid(row=0, column=0, sticky="nsew")
        lyricsFrame.grid(row=0, column=0, sticky="nsew")


        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        display_lyrics_button = tk.Button(self, text="Display Lyrics", font=LARGE_FONT, command=self.DisplayLyricsPage)
        display_lyrics_button.pack(pady=10, padx=10)
        connect_button = tk.Button(self, text="Connect To Spotify", font=LARGE_FONT, command=self.RunSongHandler)
        connect_button.pack(pady=10, padx=10)

    def RunSongHandler(self):
        song_handler.run()

    def DisplayLyricsPage(self):
        LyricLaunch.show_frame(LyricsPage)

class LyricsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = tk.Label(self, text = "Title Text", font = ("Comic", "30"), bg = "black", fg = "yellow")
        title.pack()

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side = RIGHT, fill = Y)

        lyricsText = tk.Text(self, font = ("Comic", "20"), bg = "black", fg = "yellow", pady = 10, padx = 20, yscrollcommand = scrollbar.set)
        lyricsText.pack()
        lyricsText.insert(END, SongHandler().lyrics)

        scrollbar.config(command = lyricsText.yview)




'''
        self.master = master
        master.title("LyricLaunch by Psuedo")
        # master.config(background = "black")
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.refreshLyricsButton = Button(master, text = "Refresh Lyrics")
        self.refreshLyricsButton.pack()

        self.searchSongButton = Button(master, text = "Search Current Song")
        self.searchSongButton.pack()

        self.connectButton = Button(master, text = "Connect")
        self.connectButton.pack()

    def RefreshLyrics(self):
        self.label.config(text = "Changed!")

    def StartLoop():
        root.mainloop()

'''


