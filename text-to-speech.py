#!/opt/homebrew/bin/python3
from gtts import gTTS
import sys

def textToSpeech():
	myText = sys.argv[1]
	language = sys.argv[2]
	if not myText or not language:
		print("Sorry please pass the text and language options")
		return
	myObject = gTTS(text=myText, lang=language, slow=False)
	myObject.save('text-to-speech.mp3')
	print('done');
	return;

textToSpeech()