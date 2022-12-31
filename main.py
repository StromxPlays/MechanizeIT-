import pywin
import pyautogui
import wmi
import winsound
import subprocess
import webbrowser
import pywin32_system32
import win10toast
import openpyxl
import tkinter as tk
from tkinter import *
from gtts import gTTS
import time
import datetime
import os

root = Tk()
root.geometry("1280x720")
root.minsize(1280, 720)

# Varibles
vscode_path = "D:/Microsoft VS Code/Code.exe"
photoshop_path = "D:/PhotoShopp/Photoshop CC/Photoshop.exe"



# Icon

ICON = tk.PhotoImage(file="assests/bg.png")
root.iconphoto(False, ICON)

# Main Function To Check

def respond_to_command():
    input_data = text_area.get()
    if "open google" in input_data:
        text_area.delete(0, END)
        webbrowser.open("https://www.google.com/")

    elif "open vs code" in input_data:
        text_area.delete(0, END)
        subprocess.call(vscode_path)   

    elif "open photoshop" in input_data:
        text_area.delete(0, END)
        subprocess.call(photoshop_path)   

    elif "click every 2 two seconds" in input_data:
        while True:
            clicks = pyautogui.click()
            time.sleep(2)
            if clicks > 10:
                break

    elif "open YouTube" in input_data:
        webbrowser.open("https://www.youtube.com/")
        text_area.delete(0, END)

    elif "create a new folder" in input_data:
        os.makedirs("D:/New Folder")
        text_area.delete(0, END)

    else:
        text_area.delete(0, END)   

# Function for text to speech

def text_to_speech():
    text_for_speech = text_area.get()
    language = "en"
    myobj = gTTS(text=text_for_speech, lang=language, slow=False)
    myobj.save("audio1.wav")
    winsound.PlaySound("audio1.wav", winsound.SND_FILENAME)
# Background
bgimg = tk.PhotoImage(file = "assests/bg.png")

# Show image using label
label1 = Label( root, image = bgimg)
label1.place(x = 0,y = 0)

# Task Widget
text_data = StringVar()
text_area = Entry(root, width=33, textvariable=text_data, borderwidth=4, foreground="black", font="lucida 17 bold", fg="dark green", background="white")
text_area.pack(padx=10, pady=24, anchor="w", ipady=3)

# Btn To Respond to the command written
btn = Button(root, width=31, text="Give Command", font="lucida 17 bold", border=4, foreground="black", fg="dark green", bg="white", command=respond_to_command)
btn.pack(padx=10, pady=70, anchor="w")

# Btn To Text To Speech
btn = Button(root, width=31,text="Text To Speech", font="lucida 17 bold", border=4, foreground="black", fg="red", bg="white", command=text_to_speech)
btn.pack(padx=10, pady=80, anchor="w")

root.title("MechanizeIT")
root.mainloop()
