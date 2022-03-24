import argparse
from webcam_utils import realtime_emotions
from prediction_utils import prediction_path
from collections import Counter
from face_recognize import faceDetectStatus
from smileseyedetect import start_video_capturing
import cv2
from RecordConversation import recordUserVoices
from PlayConversation import playUserRecordedAudio

import  speech_recognition as sr
import pyttsx3
import re
import webbrowser

# for running realtime emotion detection
def run_realtime_emotion():
   lt =  realtime_emotions()
   return lt

# to run emotion detection on image saved on disk
def run_detection_path(path):
    prediction_path(path)


def main():
    rslt = faceDetectStatus()
    print('Result iS ',rslt)
    if len(rslt) == 0:
        print("Authentication Failed")
        exit(0)
    else:
        if rslt[0] == 'True':
            print('User Authenitcated Success')
            VIDEO_CAPTURE = cv2.VideoCapture(0)
            start_video_capturing(VIDEO_CAPTURE)
        else:
            print("User Authentication Failed")
            exit(0)

    parser = argparse.ArgumentParser()
    parser.add_argument("func_name", type=str,
                        help="Select a function to run. <emo_realtime> or <emo_path>")
    parser.add_argument("--path", default="saved_images/1.jpg", type=str,
                        help="Specify the complete path where the image is saved.")
    # parse the args
    args = parser.parse_args()

    #print('****ARGS: ' + str(args))

    if args.func_name == "emo_realtime":
       lt = run_realtime_emotion()
       return lt
    elif args.func_name == "emo_path":
       lt = run_detection_path(args.path)
       return lt
    else:
        print("Usage: python main.py <function name>")

'''
#This code will give you the list of microphoine devices
import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    '''
if __name__ == '__main__':

   lt =  main()
   engine = pyttsx3.init()

   engine.say("Conversation Recording Stared.. please Make sailence for audio recording")
   engine.runAndWait()
   recordUserVoices()
   playUserRecordedAudio()
   engine.say("Thanking You for bare with us.....")
   engine.runAndWait()

   '''
   r = sr.Recognizer()
   with sr.Microphone(device_index = 0) as  source:
       print("Say Something")
       audio = r.listen(source)
       print("TIME OVER, THANX ")
   try:
       x = r.recognize_google(audio)
       engine = pyttsx3.init()
       print("TEXT:", x)
       engine.say(x)
       engine.runAndWait()
       term = 'yes'
       words = x.split()

       if term in words:
           print("Python Project")
           engine.say('This is ML Project')
           engine.runAndWait()
           webbrowser.open("notepad.exe", "testurl.py")
           #webbrowser.open_new("https://www.youtube.com/watch?v=DeB5N_bH7E8")
       elif x == 'no':
           print("This is ML Project")
       else:
           print("command not found")
   except:
       pass;'''

   print("This is LT Object ",lt)

   c = Counter(lt)

   m = c.most_common(7)
   print("most common",m)
   for x in m:
       #print('Katti Expressions ',x[0])
       if x[0]=='Happy':
           print("Your feeling of great happiness and pleasure that lifts up the spirit")
           engine.say('Your feeling of great happiness and pleasure that lifts up the spirit')
       elif x[0]=='Sad':
           print("Your may be regret,disappointment for something...!")
           engine.say('Your may be regret,disappointment for something...!')
       elif x[0] == 'Neutral':
           print("It may be caused by a lack of emotion, depression, boredom or slight confusion, such as when someone refers to something which the listener does not understand")
           engine.say('It may be caused by a lack of emotion, depression, boredom or slight confusion, such as when someone refers to something which the listener does not understand')
       elif x[0] == 'Angry':
           print("your worrying about somthing (or) mad about something and not going to take it anymore")
           engine.say('your worrying about somthing (or) mad about something and not going to take it anymore')
       elif x[0] == 'Disgusted':
           print("you’re struggling with a situation, but carrying on through your frustration.")
           engine.say('you’re struggling with a situation, but carrying on through your frustration.')
       elif x[0] == 'Fearful':
           print("your thinking about a thing or person that can harm you. ")
           engine.say('your thinking about a thing or person that can harm you. ')
       else:
           print("your somthing unexcepted shock")
           engine.say('your somthing unexcepted shock')
       engine.runAndWait()


