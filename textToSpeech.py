from time import sleep

from playsound import playsound
from gtts import gTTS
import os


def speech(text):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("welcome.mp3")
    sleep(5)
    playsound("welcome.mp3")


if __name__ == '__main__':
    # et,af,
    # print(gtts.lang.tts_langs())
    tts = gTTS("ps ps ps ps ps.... ps ps ps ps ", lang="en")
    tts.save("test.mp3")
    playsound("test.mp3")
