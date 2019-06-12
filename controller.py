from gtts import gTTS
import speech_recognition as sr
import os
import subprocess
import webbrowser

pair_file = []


def setFile(file):
    global pair_file
    pair_file = file


def talk_to_me(text):
    tts = gTTS(text=text, lang='en')
    tts.save(savefile='audio/audio.mp3')
    command_line = '"E:/coding projects/python speech processing/project/fmedia/fmedia.exe" audio/audio.mp3 --background'
    os.system('taskkill /f /im fmedia.exe')
    os.system(command_line)


def command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as src:
        text = "I'm listening to you"
        talk_to_me(text)
        print(text)

        recognizer.pause_threshold = 1
        # sr.adjust_for_ambient_noise(source=src, duration=1)
        audio = recognizer.listen(src)
        text = "Handling the request"
        talk_to_me(text)
        print(text + '\n')
    try:
        request = recognizer.recognize_google(audio_data=audio)
        text = "You said: " + request
        talk_to_me(text)
        print(text)
        assistant(request)
    except sr.UnknownValueError:
        text = "Repeat it"
        talk_to_me(text)
        print(text + '\n')
        assistant(command())
    return request


def assistant(request):
    print('assistant')
    global pair_file
    for key in pair_file:
        if key.keyword in request:
            subprocess.Popen(key.path, shell=True)
