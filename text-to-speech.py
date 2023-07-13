#!/opt/homebrew/bin/python3
from gtts import gTTS;

def textToSpeech():
	myText = "जिन्दगी छोटो छ, तर ब्रम्हान्डको आयु लामो । यो पृथिविमा मानव जातिको उत्पत्ती भएको कती नै भयो र ? भनिन्छ, यदी पृथिवी मा जिवन सुरु वएदेखी अहिले सम्म जम्मा १२ घण्टा भैदिएको भए हामी मानव जाती उत्पन्न भएको १ मिनट अगाडी । घमन्ड नगरौ ।";
	language = "ne"
	myObject = gTTS(text=myText, lang=language, slow=False)
	myObject.save('hello-world.mp3')
	print('done');
	return;

textToSpeech()