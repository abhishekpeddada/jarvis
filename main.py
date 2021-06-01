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
Mouse = Controller()
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

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
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        greet = "Good morning"
    elif hour>=12 and hour<=16:
        greet = "Good afternoon"
    elif hour>16 and hour<=20:
        greet = "Good evening"
    else:
        greet = "Welcome back"
    speak(greet + " sir")
    time()
    date()    
    speak("Jarvis at your sevice. How can I help you")

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
    server.login('snavneet561@gmail.com', 'singh@navneet01')

    server.sendmail('snavneet561@gmail.com', to, content)

    # to close our session from smtplib
    server.close

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\username\\Pictures\\New folder\\ss.png")#give directory of your own

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ") 
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "time" in query:
            time()
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        

        
        elif 'thanks' in query or 'thank you' in query:
            speak('I am happy I could help you')
        
        elif 'bye' in query:
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
            except Exception as e:
                print(e)
                
        elif "google search" in query:
            speak("What should I search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown chesey" in query:
            keyboard.send("alt+F4, space")
            keyboard.send("enter")
            
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir = "C:\\Users\\username\\Dropbox\\My PC (DESKTOP-4PFR0L8)\\Desktop\\audiobook\\Personal-Assistant\\Music playlist"
            songs = os.listdir(songs_dir) # return the list of songs in that directory
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remember that" in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that " + remember.read()) 
            
        elif 'timer' in query or 'stopwatch' in query:

            speak("For how many minutes?")
            timesec = takeCommand()
            timesec = timesec.replace('minutes', '')
            timesec = timesec.replace('minute', '')
            timesec = timesec.replace('for', '')
            timesec = float(timesec)
            timesec = timesec * 60
            speak(f'I will remind you in {timesec} seconds')

            time.sleep(timesec)
            speak('Your time has been finished sir')
                
                
             
        elif "jarvis screenshot" in query:
            screenshot()
            speak("Done")
        elif "cpu" in query:
            cpu()
        elif "joke cheppu" in query:
            joke()
        elif "offline" in query:
            quit()
        elif "close window" in query:
            speak("closing sir")
            keyboard.send("alt+F4, space")
        elif "save" in query:
            speak("saving sir")
            keyboard.send("ctrl+s")
        elif "clone" in query:
            speak("copying sir")
            keyboard.send("ctrl+c")
        elif "paste" in query:
            speak("sure")
            keyboard.send("ctrl+v")
        elif "refresh" in query:
            speak("sure sir")
            keyboard.send("F5")
        elif "select all" in query:
            speak("sure")
            keyboard.send("ctrl+a")
        elif "cut" in query:
            speak("ok sir")
            keyboard.send("ctrl+x")
        elif "undo" in query:
            speak("ok sir")
            keyboard.send("ctrl+z")
        elif "redo" in query:
            speak("ok sir")
            keyboard.send("ctrl+y")
        elif "maximize" in query:
            speak("sure sir")
            keyboard.send("F11")
        elif "rename" in query:
            speak("ok sir")
            keyboard.send("F2")
        elif "show properties" in query:
            speak("just a minute")
            keyboard.send("alt+enter")
        elif "delete" in query:
            speak("deleting sir")
            keyboard.send("ctrl+d")
        elif "move" in query:
            speak("moving to next tab")
            keyboard.send("ctrl+tab")
        elif "new folder" in query:
            speak("ok sir")
            keyboard.send("ctrl+shift+n")
        elif "scroll up" in query:
            mouse.wheel(10)
        elif "scroll down" in query:
            mouse.wheel(-10)
        elif "search" in query:
            keyboard.send("ctrl+f")
        elif 'open cd drive' in query:
            codePath = r"C:"
            os.startfile(codePath)
        elif 'open d drive' in query:
            codePath = r"D:"
            os.startfile(codePath)
        elif "show desktop" in query:
            keyboard.send("windows+d")
        elif "open this" in query:
            Mouse.click(Button.left,2)
       
    
    
    

        
            
            
            
