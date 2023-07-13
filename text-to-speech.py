#!/opt/homebrew/bin/python3
from gtts import gTTS
import sys

def textToSpeech():
	myText = sys.argv[1]
	language = sys.argv[2];
	myObject = gTTS(text=myText, lang=language, slow=False)
	myObject.save('hello-world.mp3')
	print('done');
	return;

textToSpeech()