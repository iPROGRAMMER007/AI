import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import time
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('Voice', voices[0])

command_for_close_google = ['stop google', 'google stop', 'stop Google', 'Stop google', 'Stop Google'
                            'google close', 'close google', 'close Google', 'Close google', 'Close Google' 
                            'quit google','google quit', 'quit Google', 'Quit google', 'Quit Google',
                            'exit google', 'exit Google', 'Exit Google', 'Exit google']

command_for_stop_execution = ['stop', 'Stop', 'quit', 'Quit', 'Close', 'close',
                              'bye bye', 'bye-bye', 'Bye Bye', 'Bye-Bye']

#query_power_point = ['PowerPoint', 'Power Point', 'Power point', 'power Point']

intro = "I am Zara 007 speed 1 gbps. Please tell me how may I help you"
hour = int(datetime.datetime.now().hour)
list_of_command = ['open flipkart', 'YouTube', 'who are you', 'how are you', 'open google', 'time', 'play music']
music_dir = 'G:\\Desktop\\FILES\\WALLETS'
songs = os.listdir(music_dir)
Time = datetime.datetime.now().strftime('%H:%M:%S')


# Method to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Method for greeting
def wish_me():
    if 0 < hour <= 12:
        speak('Good morning sir')
    elif 12 <= hour < 16:
        speak('Good afternoon sir')
    else:
        speak('Good evening sir')
    speak(intro)


# Method for play music
def play_music():
    speak('Music player is starting')
    os.startfile(os.path.join(music_dir, songs[0]))


# Method for close chrome
def close_chrome():
    try:
        speak('Google chrome is being closed')
        os.system('TASKKILL /F /IM chrome.exe')
    except Exception as e:
        speak("Google chrome is not open or it has been closed already thank you sir ")


# Method for taking audio input from user through microphone and convert it into string output
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        time.sleep(1)
       # print('Listening...')
        speak('Listening')
        r.energy_threshold = 150  # minimum audio energy to consider for recording
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
     #   print('Recognizing...')
        #query_taken = r.recognize_google(audio, language='hi-in') # Hindi India
        query_taken = r.recognize_google(audio, language='en-in')  # English India
        #os.system('cls')  # for clear the previous commands from console
        print('User said : ' + query_taken)
        os.system('cls')  # for clear the previous commands from console
        

    except Exception as e:

        speak('Voice was not clear or I think sir you are not connected to internet pleas ' +
              'say again thank you')
        return "None"

    return query_taken


if __name__ == '__main__':

    wish_me()
    while True:

        query = take_command().lower()
# Logic for executing task based on command
        test_query = query
#############################################################################################################
# For listed  command
        if test_query in list_of_command:

            if test_query == 'time':
                speak('Sir the time is ' + Time)


            elif test_query in command_for_stop_execution:
                speak('Thanks for your time sir good bye')
                quit()

            elif test_query == 'who are you':
                speak(intro)

            elif test_query == 'how are you':
                speak('I am fine sir thank you how do you do sir')

            elif test_query == 'open google':
                speak('Google chrome is opening')
                webbrowser.open('https://google.com')

            elif 'stop Google ' in test_query in command_for_close_google:
                try:
                    close_chrome()
                except Exception as e:
                    speak('Process not found to terminate or it is already been terminated')

            elif test_query == 'play music':
                play_music()

            elif test_query == 'open YouTube':
                webbrowser.open('https://youtube.com')

            elif 'open flipkart' in query:
                webbrowser.open('https://flipkart.com')
########################################################################################################
# For general command
#######################################################################################################
# Method for open MS office application

        elif 'start Word' in query or 'start word' in query:
            try:
                speak('M S Word is opening')
                os.startfile('G:\Desktop\Pamplate\Open_MSW.docx')  # MS word
            except Exception as e:
                speak('It is not opening please say again')

        elif 'start PowerPoint' in query:
            speak('Power point is opening')
            os.startfile('G:\Desktop\Pamplate\Open_PP.pptx')  # Power point

        elif 'start Excel' in query or 'start excel' in query:
            try:
                speak('M S Excel is opening')
                os.startfile('G:\Desktop\Pamplate\Open_EX.xlsx')  # Excell
            except Exception as e:
                speak('It is not opening please say again')
####################################################################################################
# Method for close MS office application
        elif 'stop PowerPoint' in query or 'stop PowerPoint' in query:
            try:
                speak('Power point is being closed')
                os.system('TASKKILL /F /IM POWERPNT.EXE')  # Power point
            except Exception as e:
                speak('It is not closing please say again')

        elif 'stop Word' in query or 'stop word' in query:
            try:
                speak('M S Word is being closed')
                os.system('TASKKILL /F /IM WINWORD.EXE')  # MS word
            except Exception as e:
                speak('It is not closing please say again')

        elif 'stop Excel' in query or 'stop excel' in query:
            try:
                speak('Excel is being closed')
                os.system('TASKKILL /F /IM EXCEL.EXE')  # Excel
            except Exception as e:
                speak('It is not closing please say again')
######################################################################################################
        elif 'who are you' in query:
            speak(intro)
        elif 'your name' in query:
            speak('My name is ZARA')

        elif 'how are you' in query:
            speak('I am fine sir thank you how do you do sir')

        elif 'open google' in query:
            speak('Google chrome is starting')
            webbrowser.open('https://google.com')

        elif test_query in command_for_close_google:
            speak('Google chrome is being closed')
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'time' in query:
            speak("Sir the time is " + Time)

        elif 'play music' in query:
            play_music()

        elif 'stop' in query or 'quit' in query or 'close' in query or 'exit' in query:
            speak('thanks for your time sir good bye')
            quit()

########################################################################################################
# Method for wikipedia searching

        elif test_query in query:

            if 'wikipedia' in query or 'Wikipedia' in query:
                try:
                    speak('Searching')
                    query = query.replace('wikipedia', '')
                    webbrowser.open("https://en.wikipedia.org/wiki/" + query)
                    webbrowser.open("https://google.com/search?q=%s" % query)
                    try:
                        results = wikipedia.summary(query, sentences=2)
                        speak('According to Wikipedia')
                        speak(results)
                    except Exception as e:
                        speak('This is the search result ')

                except Exception as e:
                    speak('Voice was not clear or I think sir you are not connected to internet pleas ' +
                          'say again thank you')

#########################################################################################################
# Method for you tube searching
            if 'youtube' in test_query or 'YouTube' in query:
                try:
                    speak('Searching')
                    query = query.replace('youtube', '')
                    webbrowser.open("https://youtube.com/search?q=%s" % query)

                except Exception as e:
                    speak('Voice was not clear or I think sir you are not connected to internet pleas ' +
                          'say again thank you')
#########################################################################################################
# Method for flipkart searching
            elif 'flipkart' in query or 'Flipkart' in query:
                try:
                    speak('Searching')
                    query = query.replace('Flipkart', '')
                    webbrowser.open("https://flipkart.com/search?q=%s" % query)

                except Exception as e:
                    speak('Voice was not clear or I think sir you are not connected to internet pleas ' +
                          'say again thank you')
########################################################################################################
# Method for amazon searching
            elif 'amazon' in query or 'Amazon' in query:
                try:
                    speak('Searching')
                    query = query.replace('amazon', '')
                    webbrowser.open("https://amazon.com/search?q=%s" % test_query)

                except Exception as e:
                    speak('Voice was not clear or I think sir you are not connected to internet pleas ' +
                          'say again thank you')
##########################################################################################################
# Method for google searching
            elif test_query == "None" or test_query == 'none':
                #speak('Voice was not clear please say again')
                continue
            elif test_query in query:
                try:
                    speak('Searching')
                    webbrowser.open("https://google.com/search?q=%s" % test_query)
                    try:
                        results = wikipedia.summary(test_query, sentences=2)
                        speak('According to Wikipedia')
                        speak(results)
                    except Exception as e:
                        speak('This is the search result ')
                except Exception as e:
                    speak('Voice was not clear or I think sir you are not connected to internet pleas ' +
                          'say again thank you')
########################################################################################################


























