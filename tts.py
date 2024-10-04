import gtts
import playsound
text = input("Copy your text here to convert in voice: ")
sound = gtts.gTTS(text, lang="en")

sound.save("tts.mp3")
playsound.playsound("tts.mp3")