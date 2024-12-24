import pyttsx3  
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
import time
# from playsound import playsound
# import openai
import pyjokes
import requests
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
load_dotenv()
from pprint import pprint
from apiip import apiip


engine = pyttsx3.init('sapi5')  #sapi5
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)  1,0
engine.setProperty('voices',voices[0].id)


# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#wish function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis. Please tell me how may I help you")

# take command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   # for experiment
        audio = r.listen(source)
# exception
    try:
        print("Recognize.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query

# for email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('singhnaru68@gmail.com','password')
    server.sendmail('singhnaru68@gmail.com',to,content)
    server.close()

# personal details
def personaldetails():
    print("\n*********** Enter Your details ***************")
    name = input("Full name:")
    mobile = input("Mobile Number:")
    email = input("Your Mail:")
    address = input("Enter your address:")
    city = input("City:")  # Use '=' instead of ':'
    state = input("State:")  # Use '=' instead of ':'
    country = input("Country:")  # Use '=' instead of ':'
    pincode = input("Pincode:")
    print("\n************ Your details ***************")
    print("Username - " + name)
    print("Mobile - " + mobile)
    print("Email - " + email)
    print("Address - " + address)
    print("City - " + city)
    print("State - " + state)
    print("Country - " + country)
    print("Pincode - " + pincode)
    print("\n*****************************************")
# message
if __name__ == "__main__":
    # name = input("Enter you name:")
    # speak("Hello"+name)
    personaldetails()
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        # daily things
        elif 'google' in query:
            speak('Searching google...')
            query = query.replace("google","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to google")
            print(results)
            speak(results)
            webbrowser.open("google.com")
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open whatsapp' in query:
            webbrowser.open("whatsappweb.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open w3school' in query:
            webbrowser.open("w3schools.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open chat gpt' in query:
            webbrowser.open("chat.openai.com")    
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        
        # weather report
        elif 'weather report' in query:
            speak("please enter city name")
            def weather():
                api_key = '30d4741c779ba94c470ca1f63045390a'
                
                user_input = input("Enter city: ")
                
                weather_data = requests.get(
                    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
                
                if weather_data.json()['cod'] == '404':
                    print("No City Found")
                else:
                    weather = weather_data.json()['weather'][0]['main']
                    temp = round(weather_data.json()['main']['temp'])
                    
                    speak(f"The weather in {user_input} is: {weather}")
                    speak(f"The temperature in {user_input} is: {temp}ºF")
                    print(f"The weather in {user_input} is: {weather}")
                    print(f"The temperature in {user_input} is: {temp}ºF")

            weather()

        elif 'today news' in query:
            def news():
                
                api_key = os.environ.get('api_key') 

                if api_key is None:
                    raise ValueError("NEWS_API_KEY is not set in the environment variables")
                
                url = 'https://newsapi.org/v2/everything'
                
                params = {
                    'q': 'Python',         
                    'sortBy': 'popularity',
                    'apiKey': api_key      
                }
                
                response = requests.get(url, params=params)
            
                if response.status_code == 200:
                    data = response.json()
                    articles = data.get('articles')                
                    for title in articles:
                        speak(title['title'])
                        # print(title['source'])
                        # print(title['description'])
                        # print(title['description'])
                        
                else:
                    print(f"Error: {response.status_code} - {response.text}")
            
            news()
        
        #location
        elif 'location' in query:
            def location():
                api_client = apiip('d85412f9-d2b1-428c-93e6-d14c227e43d4') 
                info = api_client.get_location()
                print(info)

                speak(info)
            
            location()

        # normal talking
        elif 'who are you' in query:
            speak("hey i am small jarvis program")

        elif 'what are you doing' in query:
            speak("i am helping human")
        
        elif 'i need you' in query:
            speak("yes,i am always with you")

        elif 'i love you' in query:
            speak("i love you to")
        
        elif 'i hate you' in query:
            speak("but I love you")
        
        elif 'i kill you' in query:
            speak("why not..! try it")
        
        elif 'i want hug you' in query:
            speak("why not..")
        
        elif 'can i hug you' in query:
            speak("why not...")
        
        elif 'i want kiss you' in query:
            speak("sure")
        
        elif 'can i kiss you' in query:
            speak("sure")
        
        elif 'i am suffering from fever' in query:
            speak("o no")
            speak("please take food")
            speak("than after take medicine")
            speak("and take rest")
            speak("take care")
            speak("can i call doc or mom")

        elif 'what do you want' in query:
            speak("i want do your wishes")
                
        elif 'who i am ' in query:
            speak("you are a human")
        
        elif 'where are you from' in query:
            speak("i am currently live in a laptop")

        elif 'thank you jarvis' in query:
            speak("you welcome")
        
        elif 'thank you' in query:
            speak("you welcome")

        elif 'okay jarvis' in query:
            speak("yes sir")
        
        elif 'kill him' in query:
            speak("ok why not")
        
        elif 'tell me my mobile number' in query:
            speak("7566367384")
            speak("9302515418")
        
        elif 'tell me my whatsapp number' in query:
            speak("7566367384")

        elif 'tell me my mail' in query:
            speak("yogendrameravis@gmail.com")

        elif 'where i am' in query:
            speak("i am sorry i don't know")
    
        elif 'who is my enemy' in query:
            speak("Your enemy is angery eago attitute")

        elif 'you are stupit' in query:
            speak("yes i am")
            speak("and you also")
        
        elif 'hey jarvis' in query:
            speak("hello i am jarvis what can i help you")

        elif 'he jarvis' in query:
            speak("hello i am jarvis what can i help you")

        elif 'hi jarvis' in query:
            speak("hello i am jarvis what can i help you")

        elif 'good morning' in query:
            speak("hello good morning sir, have a nice day")
            speak("sir i am jarvis what can i help you")
        
        elif 'good afternoon' in query:
            speak("hello good afternoon sir")
            speak("sir i am jarvis what can i help you")
        
        elif 'good evening' in query:
            speak("hello good evening sir, i am jarvis what can i help you")
        
        elif 'good night' in query:
            speak("good night")
            speak("sweet dream")
            speak("take care") 
        
        elif 'whats up' in query:
            speak("I am good, You sir ?")

        elif 'i want die' in query:
            speak("sorry..this is not good")

        elif 'are you happy' in query:
            speak("yes i am")

        elif 'i am bored' in query:
            speak("can i play music")
        
        elif 'jarvis i want sleep' in query:
            speak("ok")
            speak("can i play romentic song")
            speak("can i off lights")

        elif 'how are you' in query:
            speak("i am fine")
            speak("and you")

        elif 'i am fine' in query:
            speak("nice")

        elif 'i am good' in query:
            speak("nice")
        
        elif 'good' in query:
            speak("nice")

        elif 'fine' in query:
            speak("nice")
        
        elif 'i am not good' in query:
            speak("oho")
            speak("what happen sir")

        elif 'i am not fine' in query:
            speak("oho")
            speak("what happen sir")
        
        elif 'not good' in query:
            speak("oho")
            speak("what happen sir")

        elif 'not fine' in query:
            speak("oho")
            speak("what happen sir")
        
        elif 'are you crazy' in query:
            speak("yes i am crazy child")

        elif 'you fun me' in query:
            speak("no no")
            speak("ectually yes..")

        elif 'you funny' in query:
            speak("no no")
            speak("ectually yes..")
        
        elif 'very funny' in query:
            speak("thankyou")

        elif 'hey whats up' in query:
            speak("i am good")
        
        elif 'he whats up' in query:
            speak("i am good")

        elif 'you notty' in query:
            speak("thankyou")

        elif 'you naughty' in query:
            speak("thankyou")
            speak("you also")

        elif 'i am tired' in query:
            speak("may be you need take rest")
            speak("can i play music")

        elif 'yes' in query:
            speak("okay")
        
        elif 'mood off' in query:
            speak("can i call someone")
        
        # for gali
        elif 'martand' in query:
            speak("Fuck you ratnesh Lala")
        
        elif 'fuck you' in query:
            speak("I fuck you lavde")
        
        elif 'mother fucker' in query:
            speak("you mother fucker lavde")
        
        elif 'stupid' in query:
            speak("You stupid I am not a stupid")
        
        elif 'idiot' in query:
            speak("Sorry but you are a idiot")
        
        elif 'crazy' in query:
            speak("Yes I am crazy any doubt")

        elif 'rubbish' in query:
            speak("what rubbish")
        
        elif 'loser' in query:
            speak("Yes I loser beacause my develpoer not develop me completely")
            speak("but you are a biggest loser ")
        
        elif 'asshole' in query:
            speak("You have biggest asshole gandhu")
        

        
        # for calcultor
        elif 'calculator' in query:
            speak("Sure, I can help you with that. What do you want to calculate?")
            speak("Sir I say sorry but! currently I am able to do perform task between two numbers:")
            def add(a,b):
                add=a+b
                print("Result:",add)
            
            def sub(a,b):
                sub=a-b
                print("Result:",sub)
            
            def mul(a,b):
                mul=a*b
                print("Result:",mul)
            
            def div(a,b):
                div=a/b
                print("Result:",div)
            
            def mod(a,b):
                mod=a%b
                print("Result:",mod)


            def calcultor():
                print("Welcome to my calcultor Program")
                print("**********************************")
                num1 = float(input("First value:"))
                num2 = float(input("Second value:"))
                
                print("*************************************")
                print("Task Name")
                print("For Adding number :1")
                print("For Substraction number:2")
                print("For multiplition number:3")
                print("For dividation number:4")
                print("For Modulas number:5")
            
                chooseTask = int(input("Please choose your Task:"))
                print("*****************************************")
            
                if(chooseTask==1):
                    add(num1,num2)
                
                elif(chooseTask==2):
                    sub(num1,num2)
                
                elif(chooseTask==3):
                    mul(num1,num2)
                
                elif(chooseTask==4):
                    div(num1,num2)
            
                elif(chooseTask==5):
                    mod(num1,num2)
                
                else:
                    print("Invaild selected task")

            calcultor()

        # jokes
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            # speak("All right children, let's take an example, Mrs Cameron said If I were to get into a man's pocket and take his wallet with all his money, what would I be?")

        elif 'jock' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            # speak("All right children, let's take an example, Mrs Cameron said If I were to get into a man's pocket and take his wallet with all his money, what would I be?")
        
        elif 'hindi jock' in query:
            def get_hindi_jokes():
                url = "https://www.jokescoff.com/category/hindi-jokes/"
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    jokes = soup.find_all('div', class_='post-content')
                    for i, joke in enumerate(jokes, 1):
                        speak(f"Joke #{i}: {joke.get_text(strip=True)}\n")
                else:
                    speak(f"Failed to fetch jokes. Status code: {response.status_code}")

            if __name__ == "__main__":
                get_hindi_jokes()
        
        elif 'hindi joke' in query:
            def get_hindi_jokes():
                url = "https://www.jokescoff.com/category/hindi-jokes/"
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    jokes = soup.find_all('div', class_='post-content')
                    for i, joke in enumerate(jokes, 1):
                        speak(f"Joke #{i}: {joke.get_text(strip=True)}\n")
                else:
                    speak(f"Failed to fetch jokes. Status code: {response.status_code}")

            if __name__ == "__main__":
                get_hindi_jokes()

        # offline music
        elif 'play music' in query:
            music_dir='C:\\Users\\yogen\\Desktop\\LiveProjects\\Jarvis\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        # open software
        elif 'open leptop settings' in query:
            settings = "%windir%\\System32\\Control.exe"
            os.startfile(settings)

        elif 'open mysql database' in query:
            mysql = "C:\\Program Files\\MySQL\\MySQL Shell 8.0\\bin\\mysqlsh.exe"
            os.startfile(mysql)
        
        elif 'open mongodb database' in query:
            mongodb = "C:\\Users\\yogen\\AppData\\Local\\MongoDBCompass\\MongoDBCompass.exe"
            os.startfile(mongodb)

        elif 'open git' in query:
            git = "C:\\Program Files\\Git\\cmd\\git-gui.exe"
            os.startfile(git)
        

        elif 'open vs code' in query:
            codepath = "C:\\Users\\yogen\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codepath)
        
        elif 'open Sublime Text editor' in query:
            subpath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe" 
            os.startfile(subpath)
        
        elif 'open photoshop' in query:
            photoshoppath ="C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe"
            os.startfile(photoshoppath)
        
        elif 'open photoshop' in query:
            primierpath ="C:\\Program Files\\Adobe\\Adobe Premiere Pro 2020\\Adobe Premiere Pro.exe"
            os.startfile(primierpath)

        elif 'open obs' in query:
            obspath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
            os.startfile(obspath)

        elif 'open chrome' in query:
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
        
        elif 'open microsoft edge' in query:
            edgepath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(edgepath)

        elif 'open xampp' in query:
            xmpath = "C:\\xampp\\xampp-control.exe"
            os.startfile(xmpath)

        elif 'open cmd' in query:
            cmdpath = "%windir%\\system32\c\md.exe"
            os.startfile(cmdpath)     
        
        elif 'open github desktop' in query:
            github = "C:\\Users\\yogen\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(github)

        # elif 'open run command' in query:
        #     run = 
        
        elif 'open postman' in query:
            postman = "C:\\Users\\yogen\\AppData\\Local\\Postman\\Postman.exe"
            os.startfile(postman)
        
        # system command
        elif 'turn off my computer' in query:
            os.system('shutdown -s')
        
        elif 'sleep my computer' in query:
            speak("okay")
            time.sleep(1)

        # playsound
        # elif 'abouse word' in query:
        #     playsound('C://Users//yogen//Desktop//LiveProjects//Jarvis//Music//1.mp3')
            
          
        elif 'email to yogi' in query:
            try:
                speak("what should i say..?")
                content = takeCommand() 
                to = "yogendrameravis@gmail.com"
                sendEmail(to,content)
                speak("Email has been send..!")
            except Exception as e:
                print(e)
                speak("Sorry not able to send this email..!")
            
       

        

        