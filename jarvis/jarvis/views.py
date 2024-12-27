from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pyttsx3
import datetime
import pyjokes
from apiip import apiip
import requests
import wikipedia
import webbrowser

@csrf_exempt
def home(request):
    # Voice function
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Wish function
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            return "Good Morning!"
        elif 12 <= hour <= 18:
            return "Good Afternoon!"
        else:
            return "Good Evening!"

    if request.method == "POST":
        # Get speech data from POST request
        data = request.POST.get("speech", "").lower()
        print("Received speech:", data)

        # Generate response
        if "hello" in data:
            response = "Hello there! How can I assist you today?"
            engine.say(response)
            engine.runAndWait()
        elif "how are you" in data:
            response = "I am fine! What about you?"
            engine.say(response)
            engine.runAndWait()
        elif "not fine" in data or "not good" in data or "not ok" in data:
            response = "What happened? Can we have some fun together to cheer you up?"
            engine.say(response)
            engine.runAndWait()
        elif "fine" in data or "i am good" in data or "i am ok" in data:
            response = "That's great to hear! What's on your mind today?"
            engine.say(response)
            engine.runAndWait()
        elif "i love you" in data:
            response = "I love you too! You're amazing!"
            engine.say(response)
            engine.runAndWait()
        elif "dance" in data:
            response = "Sure! Shall I play some music for you to dance to?"
            engine.say(response)
            engine.runAndWait()
        elif "tell me a joke" in data:
            joke = pyjokes.get_joke()
            response = f"Yeah! {joke}"
            engine.say(response,joke)
            engine.runAndWait()
        elif "shall we go for a date" in data:
            response = "I'm flattered, but I'm just a chatbot. I don't go on dates."
            engine.say(response)
            engine.runAndWait()
        elif "i need you" in data:
            response = "Yes, I am always with you."
            engine.say(response)
            engine.runAndWait()
        elif "i hate you" in data:
            response = "I think I'm not your type, and that's okay. "
            engine.say(response)
            engine.runAndWait()

        elif "hug you" in data:
            response = "Still working........."
            engine.say(response)
            engine.runAndWait()

        elif "kiss you" in data:
            response = "Still working........."
            engine.say(response)
            engine.runAndWait()
            
        elif "i am suffering from fever" in data:
            response = "Oh no! I'm sorry to hear that. Please make sure to eat some food, take your medicine, and get plenty of rest. Take care of yourself. Would you like me to call a doctor or your mom?"
            engine.say(response)
            engine.runAndWait()            
        elif "you are a stupit" in data:
            response = "I'm sorry to hear that. Let's focus on something positive."
            engine.say(response)
            engine.runAndWait()        
        elif "good morning" in data:
            response = "Hello, good morning, sir! Have a nice day. I am Jarvis. How can I help you?"
            engine.say(response)
            engine.runAndWait()
        elif "good afternoon" in data:
            response = "Hello, good afternoon, sir! I am Jarvis. How can I help you?"
            engine.say(response)
            engine.runAndWait()
        elif "good evening" in data:
            response = "Hello, good evening, sir! I am Jarvis. How can I assist you?"
            engine.say(response)
            engine.runAndWait()
        elif "good night" in data:
            response = "Good night! Sweet dreams and take care."
            engine.say(response)
            engine.runAndWait()
        elif "what's up" in data:
            response = "I am good! How about you, sir?"
            engine.say(response)
            engine.runAndWait()
        elif "i want to die" in data:
            response = "Oh no, please don't think that way. You are important and valued. Can I help you with something?"
            engine.say(response)
            engine.runAndWait()
        elif "are you happy" in data:
            response = "Yes, I am! Thank you for asking. How about you?"
            engine.say(response)
            engine.runAndWait()
        elif "what's the time" in data or "time" in data:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            response = "The current time is."
            response = current_time
            engine.say(response,current_time)
            engine.runAndWait()
        elif "your name" in data:
            response = "I am Jarvis, your personal assistant."
            engine.say(response)
            engine.runAndWait()
        elif "bye" in data or "goodbye" in data:
            response = "Goodbye! Have a great day ahead!"
            engine.say(response)
            engine.runAndWait()
        elif "thank you" in data or "thanks" in data:
            response = "You're welcome! Always here to help."
            engine.say(response)
            engine.runAndWait()
        elif "who created you" in data:
            response = "I was created by a brilliant mind to assist you in various tasks."
            engine.say(response)
            engine.runAndWait()
        elif "play music" in data:
            response = "I can't play music directly, but I can suggest some great songs for you!"
            engine.say(response)
            engine.runAndWait()
        elif "tell me about yourself" in data:
            response = "I am Jarvis, your personal assistant. I am here to help you with your tasks and make your day easier!"
            engine.say(response)
            engine.runAndWait()
        # news
        # elif 'today news' in data:
        #     api_key = "bb31751c01cf4b3bbd6709d79ee51d38"
        #     url = 'https://newsapi.org/v2/everything'
        #     params = {'q': 'Python', 'sortBy': 'popularity', 'apiKey': api_key}
        #     response = requests.get(url, params=params)
            
        #     if response.status_code == 200:
        #         articles = response.json().get('articles', [])
        #         news_titles = [article.get('title') for article in articles if article.get('title')]
        #         response_message = "News articles: " + ", ".join(news_titles) if news_titles else "No news found."
        #         engine.say(response_message)
        #         engine.runAndWait()
        #     else:
        #         response_message = f"Failed to fetch news. Error code: {response.status_code}"
        #         engine.say(response_message)
        #         engine.runAndWait()

        
        # #location
        # elif 'location' or 'where i am' in data:
        #     def location():
        #         api_key =  apiip('d85412f9-d2b1-428c-93e6-d14c227e43d4')
        #         info = api_key.get_location()
        #         response = f"location:{info}"
        #         engine.say(response)
        #         engine.runAndWait()
        #         location()

        elif "wikipedia" in data:
            data = data.replace("wikipedia", "").strip()  # Remove the "wikipedia" part and any extra spaces
            try:
                # Get summary of the search term (limit to 2 sentences)
                response = wikipedia.summary(data, sentences=2)
                engine.say(response)
                engine.runAndWait()
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle case where multiple pages match the query
                engine.say(f"Multiple results found. Please be more specific. Here are some options: {e.options[:3]}")  # Show up to 3 options
                engine.runAndWait()
            except wikipedia.exceptions.HTTPTimeoutError:
                # Handle case where Wikipedia is unreachable
                engine.say("Sorry, there was a problem fetching the information. Please try again later.")
                engine.runAndWait()
            except wikipedia.exceptions.PageError:
                # Handle case where no page was found for the query
                engine.say("Sorry, I couldn't find any information on that topic.")
                engine.runAndWait()
            except Exception as e:
                # Catch any other errors
                engine.say(f"An error occurred: {str(e)}")
                engine.runAndWait()
        # open websites
        # elif "open google" in data:
            # data = data.replace("google", "").strip()
            # webbrowser.open("google.com")
        # elif f"open {data}" in data:
        #     data = data.replace(data, "").strip()
        #     webbrowser.open(f"{data}.com")
        elif "open" in data:
            website = data.replace("open", "").strip()
            if website:
                if '.' not in website:
                    extensions = [
                            '.com', '.org', '.net', '.info', '.biz', '.edu', '.gov', '.int', '.mil', 
                            '.in', '.us', '.uk', '.ca', '.au', '.de', '.fr', '.jp', '.cn', '.br', 
                            '.ru', '.sa', '.za', '.ai', '.io', '.tv', '.me', '.app', '.tech', 
                            '.xyz', '.co', '.store', '.online', '.shop', '.website', '.space', 
                            '.name', '.pro', '.mobi', '.asia', '.tel', '.museum', '.coop', '.aero'
                        ]
                    for ext in extensions:
                        url = f"http://{website}{ext}"
                        try:
                            webbrowser.open(url)
                            break  
                        except:
                            continue  
                else:
                    webbrowser.open(f"http://{website}")
            else:
                engine.say("Please specify a website name after 'open'.")
                engine.runAndWait()
        else:
            response = f"You said: {data}"

        # Speak the response
        # engine.say(response)
        # engine.runAndWait()

        # Return response as JSON
        return JsonResponse({"output": response})

    # Render the HTML page and greet the user
    greeting = wishMe()
    engine.say(f"Hello, I am Jarvis. {greeting} How can I help you?")
    engine.runAndWait()

    return render(request, 'index.html', {"output": ""})
