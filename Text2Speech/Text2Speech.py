from gtts import gTTS
import os

fr = open("text.txt", 'r')
text = fr.read().replace('\n', ' ')

fr.close()

language = 'en'

output = gTTS(text = text, lang = language, slow = False)

output.save('output.mp3')
