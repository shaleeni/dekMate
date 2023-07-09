import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import openai
from config import apikey

engine = pyttsx3.init()
r = sr.Recognizer()

def ai(prompt):
    openai.api_key = apikey

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="prompt",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
     #todo: wrap in try catch block
    print(response["choices"][0]["text"])


def chat(convo):

def say(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
        while True:
            print("listening..")
            with sr.Microphone() as source:
                audio = r.listen(source)
            print("Got it! one moment please...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                print("You said :{}".format(value))
                return value
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
                return "Oops! Didn't catch that"
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
                return "Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
        say("hello I am your virtual assistant")
        say("what can i do for u today")
        #print("listening..")
        convo = take_command()
        say(convo)
        #opening websites
        sites = [["youtube", "https://www.youtube.com/"], ["google", "https://www.google.com/?pli=1&authuser=1"],
                 ["gmail", "https://mail.google.com/mail/u/1/?ogbl#inbox"],
                 ["leetcode", "https://leetcode.com/problemset/all/"], ["code", "https://codeforces.com/"],
                 ["netflix", "https://www.netflix.com/browse"]]
        for site in sites:
            if f"open {site[0]}".lower() in convo.lower():
                say(f"opening {site[0]} ")
                webbrowser.open(site[1])

        apps = [["brave","C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"],
                ["notes","C:/Program Files/Microsoft Office/root/Office16/ONENOTE.EXE"]]
        for app in apps:
            if f"open {app[0]}".lower() in convo.lower():
                say(f"opening {app[0]} ")
                webbrowser.open(app[1])

        if "use ai".lower() in convo.lower():
            ai(prompt=convo)

        else:
            chat(convo)
