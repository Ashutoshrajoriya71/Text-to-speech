import pyttsx3

text_speech = pyttsx3.init()

answer = input("Copy your text here to convert in voice: ")

text_speech.say(answer)
text_speech.runAndWait()


