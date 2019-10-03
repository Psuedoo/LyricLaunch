from Song import *
import lyricsgenius
import tkinter
import information
from tkinter import *

main = tkinter.Tk()

main.configure(background = "black")

genius = lyricsgenius.Genius(information.GENIUS_ACCESS_TOKEN)

songName = "Black and Yellow"
artist = ["Wiz"]
titleText = (f"{songName} by {artist[0]}")

searchResults = genius.search_song(songName, artist=artist[0])

lyrics = searchResults.lyrics

scrollbar = Scrollbar(main)
scrollbar.pack(side = RIGHT, fill = Y)

title = Label(main, text = titleText, font = ("Comic", "30"), bg = "black", fg = "yellow")
title.pack()

lyricsText = Text(main, font = ("Comic", "20"), bg = "black", fg = "yellow", pady = 10, padx = 20, yscrollcommand = scrollbar.set)
lyricsText.pack()
lyricsText.insert(END, lyrics)

scrollbar.config(command = lyricsText.yview)

main.mainloop()
