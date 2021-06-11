import pyttsx3                  #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia                #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui                #pip install pyautogui
import psutil                   #pip install psutil
import pyjokes                  #pip install pyjokes



engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 170
engine.setProperty('rate',newVoiceRate)
engine.say("hello i am Dragoon")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    
    battery = psutil.sensors_battery
    speak("Battery is at ")
    speak(battery.percent)
    
    
    
def wishme():
    speak("Welcome back! Nice to meet you")
    
    hour = datetime.datetime.now().hour
    
    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour >=12 and hour <18:
        speak("Good afternoon")
    elif hour >=18 and hour <=24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Dragoon at your service. So, How can I help you")

def inputcommand():
    query=str(input())
    return query

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print("Recognizing:")
        query = r.recognize_google(audio,'en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        
        return "None"
    
    return query


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("abc@gmail.com","123test")
    server.sendmail("abc@gmail.com",to,content)
    server.close()


def screenshot():
    img = pyautogui.screenshot
    img.save("D:\Data\project\Artificial Intelligence\ss.png")   #path where screenshot will be saved and it will be save as ss.png


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    
    wishme()
    
    while True:
       
        #query=inputcommand().lower()
        query = takeCommand().lower()
        print(query)
        
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result=wikipedia.summary(query,sentence = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                speak("Email was send Successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send")
        elif "search in chrome" in query:
            speak("What should I Search?")
            browserpath = "C:\Program Files\Mozilla Firefox\firefox.exe %s"  #insert the path of the browser 
            search = takeCommand().lower()
            #search = inputcommand().lower()
            wb.get(browserpath).open_new_tab(search + ".com")
        
        elif "logout" in query:
            os.system("shutdown - 1")
        
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        
        elif "restart" in query:
            os.system("shutdown /r /t 1")
            
        elif "play songs" in query:
            songs_dir = "D:\Songs\ENGLISH SONGS\linkin parkin"  #path of song directory
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remember that" in query:
            speak("What should i remember")
            #data= inputcommand()
            data = takeCommand()
            speak("you said me to remeber"+ data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "reminder" in query:
            remember = open("data.txt", "r")
            speak("You said me to rember that" + remember.read())
         
        elif "screenshot" in query:
            screenshot()
            speak("Done!")
            
        elif "cpu" in query:
            cpu()
        
        elif "joke" in query:
            jokes()
    
    
    
    
    
    
    
    
    
    
    
    
