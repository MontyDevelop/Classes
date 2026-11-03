import random
import tkinter as tk
from midiutil import MIDIFile
import os, sys, subprocess

def generate_notes():

    midi = MIDIFile(1)

    track = 0
    time = 0

    midi.addTrackName(track, time, "Ai_music")
    midi.addTempo(track, time, 120)


    notes = [60, 62, 64, 65, 67, 69, 71, 72] # c major scale notes

    for i in range(8):
        note = random.choice(notes)
        duration = 1
        midi.addNote(track, 0, note, time, duration, 100)
        time += 1

    with open("Ai_melody_song.mid", "wb") as file:
        midi.writeFile(file)

def play_notes():
    tone = "Ai_melody_song.mid"
    # we have to check this file existing or not?
    if not os.path.exists(tone):
        label.config(text="No music file. Generate First")
        return
    if sys.platform.startswith("win"):
        os.startfile(tone)
    elif sys.platform == "darwin":
        subprocess.run(['open',tone])
    else:
        subprocess.run(['xdg-open', tone])
    label.config(text="Playing...")




root = tk.Tk()
root.title("Midi note generator")
root.geometry("400x200")
generate_btn = tk.Button(root, text="generate notes", command=generate_notes, width=20, height=2)
generate_btn.pack(pady=10)
play_btn = tk.Button(root, text="play notes", command= play_notes, width=20, height=20)
play_btn.pack(pady=20)
label = tk.Label(root, text="")
label.place(x=125, y=55)
root.mainloop()