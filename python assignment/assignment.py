import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import random
import pygame
import datetime
import time
import webbrowser
import requests

def translate_text():
    text = entry.get()  # Get the text to be translated from the entry widget
    source_lang = "en"  # Specify the source language code (e.g., "en" for English)
    target_lang = "fr"  # Specify the target language code (e.g., "fr" for French)
    api_key = "YOUR_API_KEY"  # Replace with your actual API key

    url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}"
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang
    }

    try:
        response = requests.post(url, data=payload)
        translation = response.json()["data"]["translations"][0]["translatedText"]
        messagebox.showinfo("Translation", translation)
    except requests.RequestException:
        messagebox.showerror("Error", "Translation failed. Please try again.")

entry = tk.Entry(window, width=40)
entry.pack(pady=10)

translate_button = tk.Button(window, text="Translate", command=translate_text)
translate_button.pack()

def search_web():
    search_query = entry.get()  # Get the search query from the entry widget
    search_engine = "google"  # Specify the search engine (e.g., "google" or "bing")

    if search_engine == "google":
        search_url = f"https://www.google.com/search?q={search_query}"
    elif search_engine == "bing":
        search_url = f"https://www.bing.com/search?q={search_query}"
    else:
        messagebox.showerror("Error", "Invalid search engine specified.")
        return

    webbrowser.open(search_url)


entry = tk.Entry(window, width=40)
entry.pack(pady=10)

search_engine_var = tk.StringVar()
search_engine_var.set("google")  # Set the default search engine to Google

search_engine_dropdown = tk.OptionMenu(window, search_engine_var, "google", "bing")
search_engine_dropdown.pack()

search_button = tk.Button(window, text="Search", command=search_web)
search_button.pack()



def set_alarm():
    alarm_time = entry.get()  # Get the alarm time from the entry widget
    current_time = datetime.datetime.now().strftime("%H:%M")  # Get the current time
    while current_time != alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M")
        time.sleep(1)  # Wait for 1 second

    # When the alarm time is reached, show a message box
    messagebox.showinfo("Alarm", "Alarm! It's time!")

# Example usage: set_alarm()  # Uncomment this line if you want to test the alarm immediately


entry = tk.Entry(window, width=40)
entry.pack(pady=10)

alarm_button = tk.Button(window, text="Set Alarm", command=set_alarm)
alarm_button.pack()



pygame.mixer.init()

def play_music():
    pygame.mixer.music.load("path_to_music_file.mp3")
    pygame.mixer.music.play()


music_button = tk.Button(window, text="Play Music", command=play_music)
music_button.pack()
  


def greet_user():
    greetings = ["Hello!", "Hi there!", "Greetings!"]
    return random.choice(greetings)

def answer_question(question):
    # Implement your logic here to provide answers to general knowledge questions
    if question == "What is the capital of France?":
        return "The capital of France is Paris."
    elif question == "Who invented the telephone?":
        return "Alexander Graham Bell is credited with inventing the telephone."
    else:
        return "I'm sorry, but I don't know the answer to that question."

def get_weather(location):
    # Implement your logic here to fetch weather information based on the location
    # You can use weather APIs like OpenWeatherMap, Weather Underground, etc.
    # Return the weather information as a string
    return f"The current weather in {location} is 25°C and partly cloudy."

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Sorry, I'm unable to process your request at the moment."






def speak(text):
    synthesizer = pyttsx3.init()
    synthesizer.say(text)
    synthesizer.runAndWait()


window = tk.Tk()
window.title("AI Assistant")

entry = tk.Entry(window, width=40)
entry.pack(pady=10)

def handle_button_click():
    user_question = entry.get()
    answer = answer_question(user_question)
    messagebox.showinfo("Answer", answer)

button = tk.Button(window, text="Ask", command=handle_button_click)
button.pack()

greeting = greet_user()
speak(greeting)

def handle_voice_button_click():
    user_speech = recognize_speech()
    entry.insert(tk.END, user_speech)

voice_button = tk.Button(window, text="Speak", command=handle_voice_button_click)
voice_button.pack()


window.mainloop()
