from gtts import gTTS               #pip install gTTs
from playsound import playsound     #pip install playsound
from tkinter import *               #pip install tkinter

root = Tk()
root.geometry('400x400')
root.title('Text to Speech')

Label(root, text = 'Text to Speech', font='arial 30 bold').pack()
Label(root, text ='Enter Text', font ='arial 20 bold').pack()

Msg = StringVar()

entry_field = Entry(root, textvariable =Msg, width ='50')
entry_field.place(x=20, y=120, width='350', height='40')

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('python.mp3')
    playsound('python.mp3')

def Exit():
    root.destroy()

Button(root, text = "Play", font = 'arial 15 bold', command = Text_to_speech, bg = 'green', width =4).place(x=120, y=180)
Button(root, text = 'Exit', font = 'arial 15 bold', command = Exit, bg = 'red').place(x=200, y=180)

root.mainloop()
