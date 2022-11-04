from tensorflow.keras.preprocessing.image import load_img
from time import sleep
from keras.models import load_model
from tensorflow.keras.utils import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
from pytesseract import Output
from tkinter import filedialog
from tkinter import *
import requests

#friday
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os 
import pyautogui
import psutil
import pyjokes
import keyboard
import mouse
import webbrowser
from pynput.mouse import Listener, Button, Controller

import pytesseract
from pytesseract import pytesseract
import PIL
from PIL import Image
import cv2
import csv
import numpy as np

from PIL import Image
from pytesseract import pytesseract
import subprocess
import sys

counter=0
tasks = []
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("SpeechRecognition")

r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 196)
engine.setProperty('volume', 2.7)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 


speak("plese give me a minute to setup sir")
install("tensorflow")
install("keras")
install("opencv-python")
install("numpy")
install("pytesseract")
install("tkintertable")
install("pyttsx3")

install("wikipedia")
install("pyautogui")
install("psutil")
install("pyjokes")
install("keyboard")
install("mouse")
install("pynput")
install("Pillow")
instructions = '''instructions(make sure to close this window):
                1.cpu
                2.time
                3.friday screenshot
                4.wikipedia (say what you want to search)
                5.open youtube
                6.on browser
                    6.1 new tab
                    6.2 on youtube
                        6.2.1 like this video
                        6.2.2 subscribe this video
                        6.2.3 captions
                7. speak text on screen
                8. click text on screen
                9. minimize
                10.show notifications
                11.open files
                12.open store
                13.open notepad
                14.open mail
                15.search system
                16.windows
                17.open google
                18.date
                19.type text
                20.thanks
                21.later
                22.send email
                23.google search
                24.logout
                25.shutdown
                26.restart
                27.playsongs
                28.remember that(to take quick note)
                29.do you remember anything(to speak notes)
                30.stopwatch
                31.close window
                32.save this
                33.copy this
                34.paste here
                35.refresh
                36.select all
                37.cut this
                38.undo
                39.redo
                40.rename
                41.show propertites
                42.delete
                43.move(to shift to next app)
                44.new folder
                45.scroll up
                46.scroll down
                47.find(to serch something on screen)
                48.open cd drive 
                49.open d drive
                50.show desktop(to minimize all windows)
                51.open this'''

if os.path.exists("haarcascade_frontalface_default.xml"):
    face_classifier = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
else:
    speak("please download this file and paste in folder where this executable is in and run again")
    wb.open("https://drive.google.com/file/d/1rzC184u3Txj-bbs05Rui4AzR1i7eEbNZ/view?usp=sharing")
if os.path.exists("model.h5"):
    classifier =load_model(r'model.h5')
else:
    speak("please download this file and paste in folder where this executable is in and run again")
    wb.open("https://drive.google.com/file/d/1ramzzIgAI75NEGMX2BZWBOAN995djit9/view?usp=sharing")

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)

i = 0
tasks = {}
l = []
while i<10:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)
    i=i+1
    label = ""
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)



        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

            prediction = classifier.predict(roi)[0]
            label=emotion_labels[prediction.argmax()]
            label_position = (x,y)
			
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        else:
            cv2.putText(frame,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    print(label)
    sleep(2)
    l.append(label)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(l)
s = ""
maxi = -1
for i in l:
    if l.count(i) >maxi:
        maxi = l.count(i)
        s = i
print(s)
cap.release()
cv2.destroyAllWindows()

#friday
Mouse = Controller()

def show_instructions():
    root = Tk()
    h = Scrollbar(root, orient = 'horizontal')
    h.pack(side = BOTTOM, fill = X)
    v = Scrollbar(root)
    v.pack(side = RIGHT, fill = Y)
    t = Text(root, width = 100, height = 20, wrap = NONE,xscrollcommand = h.set,yscrollcommand = v.set)
    for i in range(20):
        t.insert(END,instructions)
    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)
    root.mainloop()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time) 

def convertMonth(month):
    if(month == 1):
        return "January"
    elif(month == 2):
        return "February"
    elif(month == 3):
        return "March"
    elif(month == 4):
        return "April"
    elif(month == 5):
        return "May"
    elif(month == 6):
        return "June"
    elif(month == 7):
        return "July"
    elif(month == 8):
        return "August"
    elif(month == 9):
        return "September"
    elif(month == 10):
        return  "October"
    elif(month == 11):
        return "November"
    elif(month == 12):
        return "December"




def date():
    year = str(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    month = convertMonth(month)
    speak("The current date is")
    speak(day+month+year)

def wishMe():
    if s=="Neutral":
        speak("friday at your sevice sir")
    elif s == "Happy":
        speak("you are in happy mood is there any reason sir")
        data = takeCommand()
        
        remember = open("happy.txt", "w")
        remember.write(data)
        remember.close()
        if "nothing" in data:
            speak("ok sir")
        else:
            speak("so the reason is " + data)
            speak("wow sir share this happy news with every one")
    else:
        speak("you are not in good mood what happed sir")
        data = takeCommand()
        remember = open("sad.txt", "w")
        remember.write(data)
        remember.close()
        if "nothing" in data:
            speak("ok sir")
        else:
            speak("so the reason is " + data)
            speak("dont worry sir it is just a bad day not bad life!")

def takeCommand():
    try: 
        with sr.Microphone() as source: # input coming from the micrphone which is the source
            print("Listening..")
            r.adjust_for_ambient_noise(source, duration=0.2) # wait for 0.5 second and then start listening audio
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(query)
    except Exception as e:
        print("unable to understand say that again...")
        print(e)
        
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) # as gmail usually uses 587 port

    # for checking the connection with gmail
    server.ehlo()
    server.starttls()

    # then we login to our account
    server.login('your mail', 'your password')

    server.sendmail('your mail', to, content)

    # to close our session from smtplib
    server.close

def screenshot():
    img = pyautogui.screenshot()
    if not os.path.exists("C:\\Saved Pictures"):
        os.mkdir("C:\\Saved Pictures")
    ss_dir = "C:\\Saved Pictures"
    if os.path.exists(ss_dir):
        img.save("C:\\Saved Pictures\\ss.png")#give directory of your own
    else:
        os.mkdir(ss_dir)

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ") 
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())
def click_on_text(click_text):
    pytesseract_path = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    if not os.path.exists(pytesseract_path):
        speak("sorry sir tesseract ocr is not installed. have look on this website")
        wb.open("https://www.youtube.com/watch?v=DG5D8A3zi4o")
    else:
        pytesseract.tesseract_cmd = pytesseract_path
        img1 = screenshot()
        img = cv2.imread("C:\\Saved Pictures\\ss.png")
        image_data = pytesseract.image_to_data(img, output_type=Output.DICT)
        print(image_data['text'])
        for i, word in enumerate(image_data['text']):
            if word != '':
                x,y,w,h = image_data['left'][i],image_data['top'][i],image_data['width'][i],image_data['height'][i]
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                cv2.putText(img,word,(x,y-16),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                if click_text in word.lower():
                    pyautogui.click((x+w),(y+h))


def text_on_screen():
    pytesseract_path = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    if not os.path.exists(pytesseract_path):
        speak("sorry sir tesseract ocr is not installed. watch this video to know how to install")
        wb.open("https://www.youtube.com/watch?v=DG5D8A3zi4o")
    else:
        path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        path_to_image = pyautogui.screenshot()
        pytesseract.tesseract_cmd = path_to_tesseract
        screenshot()
        new_img = "C:\\Saved Pictures\\ss.png"
        text = (pytesseract.image_to_string(new_img)).lower()
        speak(text)
def kill_task(kill,l):
    for i in l:
        if kill in i:
            os.system("taskkill /im "+i)


if __name__ == "__main__":
    wishMe()
    speak("say show instructions to know what i can do")
    while True:
        query = takeCommand().lower()
        if "time" in query:
            time()
            counter = 0
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            counter = 0
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            counter = 0
        elif 'new tab' in query:
            cords = pyautogui.locateCenterOnScreen('C:\\Users\\abhis\\Downloads\\Emotion_Detection_CNN-main\\pics\\newtab.png')
            pyautogui.click(cords)
            counter = 0
        elif 'subscribe' in query:
            cords = pyautogui.locateCenterOnScreen('C:\\Users\\abhis\\Downloads\\Emotion_Detection_CNN-main\\pics\\subscribe.png')
            pyautogui.click(cords)
            counter = 0
        elif 'like' in query:
            cords = pyautogui.locateCenterOnScreen('C:\\Users\\abhis\\Downloads\\Emotion_Detection_CNN-main\\pics\\like.png')
            pyautogui.click(cords)
            counter = 0
        elif 'dislike' in query:
            cords = pyautogui.locateCenterOnScreen('C:\\Users\\abhis\\Downloads\\Emotion_Detection_CNN-main\\pics\\dislike.png')
            pyautogui.click(cords)
            counter = 0
        elif 'captions' in query:
            cords = pyautogui.locateCenterOnScreen('C:\\Users\\abhis\\Downloads\\Emotion_Detection_CNN-main\\pics\\captions.png')
            pyautogui.click(cords)
            counter = 0
        elif 'speak text' in query:
            text_on_screen()
            counter = 0
        elif 'notifications' in query:
            pyautogui.click(1873,1046)
            counter = 0
        elif 'sublime' in query:
            npath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(npath)
        elif 'open command prompt' in query:
            npath = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(npath)
        elif 'files' in query:
            keyboard.send('windows+E')
        elif 'mail' in query:
            pyautogui.click(891,1056)
            counter = 0
        elif 'notepad' in query:
            pyautogui.click(655,1068)
            counter = 0
        elif 'search system' in query:
            pyautogui.click(245,1056)
            counter = 0
        elif 'windows' in query:
            pyautogui.click(27,1045)
            counter = 0 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
            counter = 0
        elif "date" in query:
            date()
            counter = 0
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
            counter = 0
        elif 'type text' in query:
            speak('what shoud i type?')
            cmd = takeCommand()
            pyautogui.write(cmd)
            counter = 0
        elif 'show instructions' in query:
            show_instructions()
            counter = 0

        

        
        elif 'thanks' in query or 'thank you' in query:
            speak('I am happy I could help you')
            counter = 0
        
        elif 'later' in query:
            speak('Bye sir, see you next time')
            quit()
        
        elif "send email" in query:
            try:
                speak("What message should I send?")
                content = takeCommand()
                speak("Please tell the email ID of the receiver")
                to = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!!")
                counter = 0
                
            except Exception as e:
                print(e)
                
        elif "google search" in query:
            speak("What should I search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
            counter = 0
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s")
            counter = 0
        elif 'decrease volume' in query:
            os.system("C:\\Users\\abhis\\Downloads\\Emotion_Detection_CNN-main\\scripts\\nircmd.exe changesysvolume -13107")
            counter = 0
        elif 'increase volume' in query:
            os.system("C:\\Users\\abhis\\Downloads\\Emotion_Detection_CNN-main\\scripts\\nircmd.exe changesysvolume 13107")
        elif 'mute' in query:
            os.system("C:\\Users\\abhis\\Downloads\\Emotion_Detection_CNN-main\\scripts\\nircmd.exe mutesysvolume 2")
            counter = 0
        elif 'unmute' in query:
            os.system("C:\\Users\\abhis\\Downloads\\Emotion_Detection_CNN-main\\scripts\\nircmd.exe mutesysvolume 2")
            counter = 0
        elif 'show running apps' in query:
            for proc in psutil.process_iter():
                try:
                    processName = proc.name()
                    processID = proc.pid
                    tasks[processName] = processID
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            l = sorted(tasks)
            print("--------------------------------------------Running Tasks---------------------------------------------------------------")
            for i in l:
                print(i,tasks[i])
            counter = 0
        elif 'kill task' in query:
            for i in l:
                print(i)
            speak("which program you want to kill")
            kill = takeCommand()
            kill_task(kill,l)
            counter = 0
        elif "restart" in query:
            os.system("shutdown /r /t 1")
            counter = 0
        elif "play songs" in query:
            speak("select folder where songs are located")
            root = Tk()
            root.withdraw()
            songs_dir = filedialog.askdirectory()
            songs = os.listdir(songs_dir) # return the list of songs in that directory
            os.startfile(os.path.join(songs_dir, songs[0]))
            counter = 0
        elif "remember that" in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
            counter = 0
        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that " + remember.read()) 
            counter = 0
        elif "hide files" in query:
            os.system("attrib +h /s /d")
            counter=0
        elif "make files visible" in query:
            os.system("attrib -h /s /d")
            counter = 0
            
        elif 'timer' in query or 'stopwatch' in query:

            speak("For how many minutes?")
            timesec = takeCommand()
            timesec = timesec.replace('minutes', '')
            timesec = timesec.replace('minute', '')
            timesec = timesec.replace('for', '')
            timesec = float(timesec)
            timesec = timesec * 60
            speak(f'I will remind you in {timesec} seconds')

            sleep(timesec)
            speak('Your time has been finished sir')
            counter = 0
                
                
             
        elif "friday screenshot" in query:
            screenshot()
            speak("Done")
            counter = 0
        elif "cpu" in query:
            cpu()
            counter = 0
        elif "joke" in query:
            joke()
            counter = 0
        elif "offline" in query:
            quit()
            counter = 0
        elif "close window" in query:
            speak("closing sir")
            keyboard.send("alt+F4, space")
            counter = 0
        elif "save" in query:
            speak("saving sir")
            keyboard.send("ctrl+s")
            counter = 0
        elif "copy" in query:
            speak("copying sir")
            keyboard.send("ctrl+c")
            counter = 0
            
        elif "paste" in query:
            speak("sure")
            keyboard.send("ctrl+v")
            counter = 0
        elif "refresh" in query:
            speak("sure sir")
            keyboard.send("F5")
            counter = 0
        elif "select all" in query:
            speak("sure")
            keyboard.send("ctrl+a")
            counter = 0
        elif "cut" in query:
            speak("ok sir")
            keyboard.send("ctrl+x")
            counter = 0
        elif "undo" in query:
            speak("ok sir")
            keyboard.send("ctrl+z")
            counter = 0
        elif "redo" in query:
            speak("ok sir")
            keyboard.send("ctrl+y")
            counter = 0
        elif "rename" in query:
            speak("ok sir")
            keyboard.send("F2")
            counter = 0
        elif "show properties" in query:
            speak("just a minute")
            keyboard.send("alt+enter")
            counter = 0
        elif "delete" in query:
            speak("deleting sir")
            keyboard.send("ctrl+d")
            counter = 0
        elif "move" in query:
            speak("moving to next tab")
            keyboard.send("ctrl+tab")
            counter = 0
        elif "new folder" in query:
            speak("ok sir")
            keyboard.send("ctrl+shift+n")
            counter = 0
        elif "scroll up" in query:
            mouse.wheel(10)
            counter = 0
        elif "scroll down" in query:
            mouse.wheel(-10)
            counter = 0
        elif "find" in query:
            keyboard.send("ctrl+f")
        elif 'cd drive' in query:
            codePath = r"C:"
            os.startfile(codePath)
            counter = 0
        elif 'd drive' in query:
            codePath = r"D:"
            os.startfile(codePath)
            counter = 0
        elif "show desktop" in query:
            keyboard.send("windows+d")
            counter = 0
        elif "open on this" in query:
            Mouse.click(Button.left,2)
            counter = 0
        elif 'click' in query:
            speak('on what text you want me to click')
            click_text = takeCommand()
            click_on_text(click_text) 
            counter = 0
        counter+=1
        print(counter)
        if counter>30:
            speak("say something sir")
            counter = 0
