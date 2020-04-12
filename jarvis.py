import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print('Voice :', voices[0].id)
engine.setProperty('Voice', voices[0])

intro = "I am Zara 007 speed 1gbps. Please tell me how may I help you"
list_of_command = ['open flipkart', 'YouTube', 'who are you', 'how are you', 'open google', 'time', 'play music', 'stop',]
music_dir = 'G:\\Desktop\\FILES\\WALLETS'
songs = os.listdir(music_dir)


# Method to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#Method just for wishing
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good morning')
    elif 12 <= hour < 16:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak(intro)


#Method for send email
def send_e_mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mdirshadcompany@gmail.com','password@007')
    server.sendmail('mdirshadcompany@gmail.com',to,content)
    server.close()


#Methos for play music
def play_music():
  #  music_dir = 'G:\\Desktop\\FILES\\WALLETS'
   # songs = os.listdir(music_dir)
    # print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))
    speak('Press 1 to stop')
    a = input(int('Enter a number :') )
    if a == 1:
        sys.exit()


# Method for taking audio input form user through microphone and gives string output
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 300
        r.pause_threshold = 1
       # r.dynamic_energy_ratio = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print('User said :', query)

    except Exception as e:
        #print(e)
        print('Say that again please...')
        speak('Voice was not clear please say again')
        return 'None'

    return query
'''
    except BaseException as ae:
        print('Say that again please...')
        speak('Voice was not clear please say again')
        return 'None'

    return query
'''
if __name__ == "__main__":
   # speak('Hi how are you sir hope you are fine')
    wish_me()
    while True:
         query = take_command().lower()
#Logic for executing tasks based on query

         test_query = query
         #print(test_query)
        # if test_query in query:
        #for offline communication

         if test_query in list_of_command:

            if test_query == 'time':
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                speak('Sir the time is '+ strTime)
            elif test_query == 'stop':
                speak('Thanks for your time sir')
                quit()
            elif test_query == 'who are you':
                speak(intro)
            elif test_query == 'how are you':
                speak('I am fine sir thank you how do you do sir')
            elif test_query == 'open google':
                os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
              #  webbrowser.open('google.com')
            elif test_query == 'stop google':
                os.system("TASKKILL /F /IM chrome.exe")
            elif test_query == 'play music':
                play_music()
                '''
                music_dir = 'G:\\Desktop\\FILES\\WALLETS'
                songs = os.listdir(music_dir)
                # print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                '''
            elif test_query == 'YouTube':
                webbrowser.open('youtube.com')
 #           else:
  #              speak('Is there any work for me Sir I am here to help you feel free to tell me ')

#####################################################
#####################################################

         elif 'open flipkart' in query:
             webbrowser.open('flipkart.com')
         elif 'YouTube' in query:
             webbrowser.open('youtube.com')
         elif 'who are you' in query:
             speak(intro)
         elif 'how are you' in query:
             speak('I am fine sir thank you how do you do sir')
         elif 'open google' in query:
            # webbrowser.open('google.com')
             os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
     #    elif 'who is jara' or 'who is zara' in query:
       #      speak('I am jara yes sir, I am here to help you')

         elif test_query == 'stop google':
             os.system("TASKKILL /F /IM chrome.exe")
         elif 'time' in query:
             strTime = datetime.datetime.now().strftime('%H:%M:%S')
             speak("Sir the time is " + strTime)
         elif 'play music' in query:
             play_music()
             '''
             music_dir = 'G:\\Desktop\\FILES\\WALLETS'
             songs = os.listdir(music_dir)
             #print(songs)
             os.startfile(os.path.join(music_dir,songs[0]))
             '''
          #   if 'quit music' in query:
           #      os.close(os.path.join(music_dir,songs[0]))
      #   elif 'stop music' in query:

       #      #quit(play_music())

         elif 'power point' in query:
             ms_path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
             os.startfile(ms_path)
         elif 'send email' in query:
             try:
                 speak('What should I say')
                 content = take_command()
                 to = 'mgrein007@gmail.com'
                 send_e_mail(to, content)
                 speak('Email has been sent')
             except Exception as e:
                 print(e)
                 speak('Sorry email was not sent try again thank you')

         elif 'stop' in query:
             speak('thanks for your time sir good bye')
             quit()


####################################################################
# For online searching on wikipedia

         elif test_query in query:
             try:
                speak('Searching...')
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences=2)
                speak('According to wikipedia')
                # print(results)
                speak(results)

             except Exception as e:
                 speak('Voice was not clear please say again thank you')

#######################################################################


















