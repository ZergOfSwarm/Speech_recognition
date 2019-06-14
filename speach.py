import speech_recognition as sr
import os
import sys
import webbrowser # Позволяет открывать различные сайты

def talk(words):
    print(words)
    os.system("say " + words)

talk("Привет, спрости у меня что-либо!")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите, я вас слушаю!")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("Я вас не поняла!")
        zadanie = command()

    return zadanie

def makeSomthing(zadanie):
    if 'открой google' in zadanie:
        talk("Уже открываю")
        url = 'https://google.com'
        webbrowser.open(url)
    elif 'стоп'in zadanie:
        talk("Да, конечно, была рада Вам помочь!")
        sys.exit()

while True:
    makeSomthing(command())
