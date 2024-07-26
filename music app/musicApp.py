import tkinter as tk
from tkinter import filedialog
from pygame import mixer

mixer.init()

def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        mixer.music.load(file_path)
        mixer.music.play()

def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

root = tk.Tk()
root.title("Simple Music App")
root.geometry("300x200")

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=10)

unpause_button = tk.Button(root, text="Unpause", command=unpause_music)
unpause_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=10)

root.mainloop()
