import speech_recognition as sr
import pyttsx3
import csv
# Initialize the recognizer
r = sr.Recognizer()
# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()  
c=1
while (c):
    try:  
        # use the microphone as source for input.
        with sr.Microphone() as source2:  
            r.adjust_for_ambient_noise(source2, duration=0.2)
            SpeakText("what is the starting location")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            #listens for the user's input
            audio2 = r.listen(source2,phrase_time_limit=5)
            # Using google to recognize audio
            start = r.recognize_google(audio2)
            start = start.lower()
            print("Did you say ",start)
            c=0
            #SpeakText("did you say "+MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))     
    except sr.UnknownValueError:
        print("unknown error occurred")
c=1
while (c):    
    try:
        with sr.Microphone() as source2: 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            SpeakText("what is the destination location")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            #listens for the user's input
            audio2 = r.listen(source2,phrase_time_limit=5)
            # Using google to recognize audio
            dest = r.recognize_google(audio2)
            dest = dest.lower()
            print("Did you say ",dest)
            c=0
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
c=1
while (c):
    try:
        with sr.Microphone() as source2: 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            SpeakText("what is the date of travel")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            #listens for the user's input
            audio2 = r.listen(source2,phrase_time_limit=5)
            # Using google to recognize audio
            date = r.recognize_google(audio2)
            date = date.lower()
            print("Did you say ",date)
            c=0
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
c=1
while (c):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            SpeakText("what is the choice for choosing, price or duration")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            #listens for the user's input
            audio2 = r.listen(source2,phrase_time_limit=5)
            # Using google to recognize audio
            choice = r.recognize_google(audio2)
            choice = choice.lower()
            print("Did you say ",choice)
            #SpeakText(start+dest+date+choice)
            c=0
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")

header = ['source', 'destination', 'date', 'choice']
data = [start,dest,date,choice]

with open('D:\\vit\\sem6\\rpa\\jcomp\\usertravel.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerow(data)