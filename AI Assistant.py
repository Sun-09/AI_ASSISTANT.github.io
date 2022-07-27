# WELCOME TO AI ASSISTANT.THIS IS BASICALLY A PROJECT WHICH WILL TAKE YOUR VOICE AS INPUT AND GIVE OUTPUT AS YOUR COMMAND.INTERNET CONNECTION REQUIRED.

from ast import Try, keyword
from datetime import datetime
from email.mime import audio
from multiprocessing.context import SpawnProcess
from turtle import write
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import random
import pyjokes
import time
from pyautogui import click
import keyboard


engine = pyttsx3.init('sapi5')     
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):           #For speak Function Helena Can Speak🤔😱🤩
    engine.say(audio)
    engine.runAndWait()

def wishMe():               #wishMe Commands Wishes You😍😘
    hour = int(datetime.now().hour)
    if hour>=0 :
        if hour>=6:
            if hour>=11:
                if hour>=18:
                    if hour>=21:
                        speak("Good Night")
                    else:
                        speak("GOOD Evening")
                else:
                    speak("Good Noon")
            else:
                speak("Good Morning")
        else:
            speak("Don't Disturb me at Midnight")
    else:
        speak("IT's Another Universe")
    speak("Hello I am Your AI Friend MY Name is Helena How can I help You?")

def takeCommand():             #takeCommand Function takes User Voice Input 😀😀😱

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.5
        r.energy_threshold = 1200        #pause_thresold is a function.you can see the function's coding and edit it by ctrl+click.
                                     # !!!!!!   Don't Manipulate it without Understanding.Helena will be angry with you. 😡😡😡😡😡 !!!!
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: ",query)
    except Exception as e:
        print("Say it again please.....")
        return "None"
    return query

def user_mannual():       # DON'T KNOW HOW TO GIVE INSTRUCTION SAY "USER MANUAL" 🔥💥🐵🙈
    if 'user manual' in query:
        speak('''Welcome to user manual of AI Assistant.py. to know anything from wikipedia just say that thing wikipedia. I want to give you example to know aboutGravity, say
         gravity wikipedia To open youtube just say  open Youtube  To open Google say  Open Google  To open the Whatsapp say  Open Whatsapp  To open gmail, youtube music, facebook follow same same vocal syntax.
         To play music in your system just say  play music  I will play a music for you in your system  To play a music on youtube just say
          Play on Youtube. To propose me say, I love you  But I will not recomend you to do so. To Know about myself just say  Tell me about Yourself  I will tell you about me,my origin.
            I will tell you jokes if you speak. joke So,The tutorial ends here. I will add some extra features very soon.Good bye''')
    else:
        speak("Let's speak ")

def speak_print(value):     #This function speak and print output
    speak(value)
    print(value, '😀😀😍😘')

def youtube_search():       # SEARCH ANYTHING IN YOUTUBE BY VOICE 🎻🎸🎶🎵
    search=speak('What Do You want to search?')
    material=takeCommand().lower()
    webbrowser.open('youtube.com')
    time.sleep(6)
    click(x=939, y=119)
    keyboard.write(material)
    keyboard.press('enter')
    time.sleep(2)
    click(x=759, y=460)
    time.sleep(8)
    doll=takeCommand().lower()
    if 'stop the add' in doll:
     click(x=1243, y=732)   
    keyboard.press('f')
    exit()



def camera():             #TAKES PHOTO 📷📸🌋
    click(x=111, y=1061)
    keyboard.write('camera')
    keyboard.press('enter')
    speak('Camera has been opened. Take a fantastic position and say click photo')
    time.sleep(5)
    while True:
        cam=takeCommand().lower()
        if 'click photo' in cam:   
            click(x=1867, y=530)
            speak('Your photo has been taken and now i am go to the folder what it is saved')
            codePath = r"C:\\Users\\PRADYOT\\Pictures\\Camera Roll"
            os.startfile(codePath)
            break


def search_movie():       #Just Give Movie Name It will show where you can get the movie 🎬🎥🎦😊😊
    speak('Say movie name ')
    movie=takeCommand().lower()
    webbrowser.open('www.justwatch.com')
    time.sleep(5)
    click(x=1423, y=145)
    keyboard.write(movie)
    time.sleep(3)
    keyboard.press('enter')

def google_search():       #SEARCHES IN GOOGLE 🔎🔍🔥
    search=speak('What Do You want to search?')
    material=takeCommand().lower()
    webbrowser.open('google.com')
    time.sleep(6)
    click(x=893, y=484)
    keyboard.write(material)
    time.sleep(2)
    keyboard.press('enter') 

def video_edit():
    codepay = "C:\\Program Files\\FlashIntegro\\VideoEditor\\VideoEditor.exe" 
    os.startfile(codepay) 

def logic():                     # This Function makes the Logic 😱😵🤨🧐
    if 'wikipedia' in query:
        speak("Searching Wikipedia.......")
        #query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=5)
        speak("According to Wikipedia")
        speak(results)
        print(results)
    elif 'open youtube' in query:
        speak('opening youtube for you.....')
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        speak('opening google for you.....')
        webbrowser.open("google.com")
    elif 'open music' in query:
        speak('opening youtube music for you.....')
        webbrowser.open("music.youtube.com")
    elif 'open gmail' in query:
        speak('opening gmail for you.....')
        webbrowser.open('gmail.com')
    elif 'open facebook' in query:
        speak('opening facebook for you.....')
        webbrowser.open('facebook.com')
    elif 'open whatsapp' in query:
        speak('opening whatsapp web.....')
        webbrowser.open('web.whatsapp.com')
    elif 'play music' in query:
        speak('playing a music for you')
        music_dir = 'C:\\Users\PRADYOT\\Documents\\GitHub\\Music_Library.github.io\\music'
        songs = os.listdir(music_dir)
        x=len(songs)
        c=random.randint(0,x-1)
        os.startfile(os.path.join(music_dir, songs[c]))
    elif 'play on youtube' in query:
        speak('Playing a Music for you in youtube....')
        music1=['youtu.be/1BVgpX4w0Wk','youtu.be/zC3UbTf4qrM','youtu.be/tLaJFnc93Oc','youtu.be/1--qqQrimMA','youtu.be/xWi8nDUjHGA','youtu.be/fdubeMFwuGs','youtu.be/C8kSrkz8Hz8','youtu.be/hoNb6HuNmU0','youtu.be/E4ZJxhyAaH8','youtu.be/iwhpS4ow7Zc']
        music2=['youtu.be/UiN3AY7bdBg','youtu.be/g_IHpBnpzr0','youtu.be/VOLKJJvfAbg','youtu.be/4POvT6O0ygE','youtu.be/vJQMhj6WYZA','youtu.be/USccSZnS8MQ','youtu.be/FDnbbnzeqhA','youtu.be/oH2DIGJPgoA','youtu.be/Gg6NMU4ivXM','youtu.be/6FURuLYrR_Q']
        musics=music1+music2
        y=len(musics)
        d=random.randint(0,y-1)
        webbrowser.open(musics[d])
    elif 'i love you' in query:
        speak("Love is 6th Sense which destroyes your other 5th Senses. So Don't fall on the trap.")
    elif 'about yourself' in query:
        details="I am Helena,your ai Friend, I was created on 27/06/22. You can celebrate it as my birthday. "
        speak(details)
        print(details)
    elif 'open code' in query:
        codePath=r"C:\\Users\\PRADYOT\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
        os.startfile(codePath)
    elif 'open age' in query:
            codePath = r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath)
    elif 'open photoshop' in query:
        codePath = r"C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\photoshop.exe"
        os.startfile(codePath)
    elif 'exit' in query:
        speak('Thank You for spending me with me.')
        exit()
    elif 'search in youtube' in query:
        youtube_search()
    elif 'search in google' in query:
        google_search()
    elif 'message in whatsapp' in query:
        speak('Tell me Sender name ')
        sender = takeCommand().lower()
        speak('Tell the messege you want to say ')
        messege= takeCommand().upper()
        webbrowser.open('web.whatsapp.com')
        time.sleep(25)
        click(x=181, y=203)
        keyboard.write(sender)
        keyboard.press('enter')
        time.sleep(2)
        keyboard.write(messege)
        keyboard.press('enter')
    elif 'take photo' in query:
        camera()
    elif 'search movie' in query:
        search_movie()
    elif 'user manual' in query:
        user_mannual()
    elif 'open video editor' in query:
        video_edit()
    elif 'joke' in query:
	    speak_print(pyjokes.get_joke())
   
      

if __name__ == "__main__":        # THIS is the main function 💗💖💓💞
    wishMe()
    
    i=0
    while i==0:
        query = takeCommand().lower()
        logic() 
        time.sleep(1)
        