import signal
import pretty_errors
import subprocess
import sys
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
import vlc
import wolframalpha
import json
import random
import operator
import speech_recognition as sr  # Will be replaced by my speech recognition algorithm
import datetime
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import socket
import platform
import getpass
import colorama
from colorama import Fore, Style

# New IP search function
# Add Ohdis Sound effect for when to speak
# Keyword Variables Used for Keyword Voice Detection System

# Decision Tree model (Supervised)
# api key for new api alpha vantage is: W01B6S3ALTS82VRF

OhdisVoice = 'en-US_KevinV3Voice'

assistname = "otis" or "hey otis" or "odys" or "Can you please help me" or "ohdis" or "hey ohdis"

voice_activation = False

uname = "Redgar Parker"
assistversion = "Ohdis Version 1 point 4 Active and Ready"

authenticator = IAMAuthenticator("qAPNQIeTYGiJlQvD0rDWoPN_5Qiyoo8HQV1PKaUBMSHj")
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(
    'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/b5d1a5f2-1c1d-466c-8659-4394a313bc7f')

try:
    ()  # I invoke the text to speech method right here
except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)


def entryGreet():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new('boot_sound.mp3')
        player.set_media(media)
        player.play()
        time.sleep(.100)
        duration = player.get_length() / 1000
        time.sleep(duration)

        with open('Ohdis_voice.wav', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    'Good Morning Edgar!',
                    voice=OhdisVoice,
                    accept='audio/wav'
                ).get_result().content)
            vlc_instance = vlc.Instance()
            player = vlc_instance.media_player_new()
            media = vlc_instance.media_new('Ohdis_voice.wav')
            player.set_media(media)
            player.play()
            time.sleep(.100)
            duration = player.get_length() / 1000
            time.sleep(duration)

    elif 12 <= hour < 18:
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new('boot_sound.wav')
        player.set_media(media)
        player.play()
        time.sleep(.100)
        duration = player.get_length() / 1000
        time.sleep(duration)

        with open('Ohdis_voice.wav', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    'Good Afternoon Edgar!',
                    voice=OhdisVoice,
                    accept='audio/wav'
                ).get_result().content)
            vlc_instance = vlc.Instance()
            player = vlc_instance.media_player_new()
            media = vlc_instance.media_new('Ohdis_voice.wav')
            player.set_media(media)
            player.play()
            time.sleep(.100)
            duration = player.get_length() / 1000
            time.sleep(duration)
    else:
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new('boot_sound.wav')
        player.set_media(media)
        player.play()
        time.sleep(.100)
        duration = player.get_length() / 1000
        time.sleep(duration)

        with open('Ohdis_voice.wav', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    'Good Evening Edgar!',
                    voice=OhdisVoice,
                    accept='audio/wav'
                ).get_result().content)
            vlc_instance = vlc.Instance()
            player = vlc_instance.media_player_new()
            media = vlc_instance.media_new('Ohdis_voice.wav')
            player.set_media(media)
            player.play()
            time.sleep(.100)
            duration = player.get_length() / 1000
            time.sleep(duration)
    with open('Ohdis_voice.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                '''Hello, I am Ohdis. Edgar's Virtual Assistant''',
                voice=OhdisVoice,
                accept='audio/wav'
            ).get_result().content)
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new('Ohdis_voice.wav')
        player.set_media(media)
        player.play()
        time.sleep(.100)
        duration = player.get_length() / 1000
        time.sleep(duration)


def usrname():
    columns = shutil.get_terminal_size().columns

    print("💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯".center(columns))
    print("Welcome", uname.center(columns))
    print("💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯💯".center(columns))

    with open('Ohdis_voice.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                "How can i Help you, sir",
                voice=OhdisVoice,
                accept='audio/wav'
            ).get_result().content)
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new('Ohdis_voice.wav')
        player.set_media(media)
        player.play()
        time.sleep(.100)
        duration = player.get_length() / 1000
        time.sleep(duration)


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        vlc_instance = vlc.Instance()
        player = vlc_instance.media_player_new()
        media = vlc_instance.media_new('voice_activate.mp3')
        player.set_media(media)
        player.play()
        time.sleep(.100)
        duration = player.get_length() / 1000
        time.sleep(duration)
        print("Listening...")
        r.pause_threshold = .5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Ohdis processing...")
        query = r.recognize_sphinx(audio)
        print("User said: {query}\n")

    except Exception as e:
        print(e)
        print("Inactivity detected")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in .login('your email id', 'your email password')gmail
    server
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    entryGreet()
    usrname()

    while True:
        if assistname in takeCommand().lower():
            voice_activation = True
            vlc_instance = vlc.Instance()
            player = vlc_instance.media_player_new()
            media = vlc_instance.media_new('voice_activate.mp3')
            player.set_media(media)
            player.play()
            time.sleep(.100)
            duration = player.get_length() / 1000
            time.sleep(duration)
            query = takeCommand().lower()
            # All the commands said by user will be
            # stored here in 'query' and will be
            # converted to lower case for easily
            # recognition of command

            if "open youtube" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Youtube right here sir\n",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Google right here sir\n",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "StackOverflow right here sir. They never helped you though. Come on sir.",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                webbrowser.open("stackoverflow.com")

            elif 'play music' in query or "play a song" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Music Right here sir",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

                music_dir = "C:\\Users\\bedga\\Music"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[1]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("H:% M:% S")
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "sir, the time is {strTime}",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif 'whats my ip' in query:  # Hashtag is how you do it. Not \\\ like in java idiot. (Anyway, keyword here)

                # Function to display hostname and
                # IP address
                def get_Host_name_IP():
                    try:
                        host_name = socket.gethostname()
                        host_ip = socket.gethostbyname(host_name)
                        with open('Ohdis_voice.wav', 'wb') as audio_file:
                            audio_file.write(
                                text_to_speech.synthesize(
                                    "Ohdis 1.4 Running On : ", host_name,
                                    voice=OhdisVoice,
                                    accept='audio/wav'
                                ).get_result().content)
                            vlc_instance = vlc.Instance()
                            player = vlc_instance.media_player_new()
                            media = vlc_instance.media_new('Ohdis_voice.wav')
                            player.set_media(media)
                            player.play()
                            time.sleep(.100)
                            duration = player.get_length() / 1000
                            time.sleep(duration)
                        with open('Ohdis_voice.wav', 'wb') as audio_file:
                            audio_file.write(
                                text_to_speech.synthesize(
                                    "Your Eye Pee is ", host_ip,
                                    voice=OhdisVoice,
                                    accept='audio/wav'
                                ).get_result().content)
                            vlc_instance = vlc.Instance()
                            player = vlc_instance.media_player_new()
                            media = vlc_instance.media_new('Ohdis_voice.wav')
                            player.set_media(media)
                            player.play()
                            time.sleep(.100)
                            duration = player.get_length() / 1000
                            time.sleep(duration)

                        print("Ohdis 1.4 Running On : ", host_name)
                        print("IP : ", host_ip)
                    except:
                        with open('Ohdis_voice.wav', 'wb') as audio_file:
                            audio_file.write(
                                text_to_speech.synthesize(
                                    "Unable to get Hostname and IP",
                                    voice=OhdisVoice,
                                    accept='audio/wav'
                                ).get_result().content)
                            vlc_instance = vlc.Instance()
                            player = vlc_instance.media_player_new()
                            media = vlc_instance.media_new('Ohdis_voice.wav')
                            player.set_media(media)
                            player.play()
                            time.sleep(.100)
                            duration = player.get_length() / 1000
                            time.sleep(duration)
                        print("Unable to get Hostname and IP")

                    # Driver code


                get_Host_name_IP()  # Function call

                # This code is contributed by "Sharad_Bhardwaj".
                # This code has been modified to function with The Redgar Octal Intelligence System

            elif 'how are you' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "I am good sir.",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "How are you sir?",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif 'predict the stocks of apple' in query or 'apple stocks please' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Just a moment. Let me plot you their business",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                    key = 'W01B6S3ALTS82VRF'
                    ts = TimeSeries(key, output_format='pandas')
                    ti = TechIndicators(key)
                    aapl_data, aapl_meta_data = ts.get_daily(symbol='AAPL')
                    aapl_sma, aapl_meta_sma = ti.get_sma(symbol='AAPL')

                    figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
                    aapl_data['4. close'].plot()
                    plt.tight_layout()
                    plt.grid()
                    plt.show(block=False)
                    plt.pause(7.5)
                    plt.close()

            elif 'good' in query or 'fine' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "That is good. It is my sole purpose to know that you are alright.",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif 'Not so great' in query or 'meh' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "I wish I could help sir.",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif 'Ohdis you there?' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "At your service sir",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif "version" in query or "version please" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            assistversion,
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif "what's your name" in query or "what is your name" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "I am Ohdis. An advanced artificial intelligence by Edgar",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                print("Ohdis AI 1.1")

            elif 'exit' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Thank you sir, be sure to update my security protocols often",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                exit()

            elif "who made you" in query or "who created you" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "I have been created by Redgar Technologies",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif 'tell me a joke' in query or "make me laugh" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            pyjokes.get_joke(),
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif "calculate" in query:

                app_id = '''Q3VJ62-L4633H2774'''
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "The answer is " + answer,
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif 'search' in query or 'play' in query:

                query = query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)

            elif "Import selected data from Redgar Secure Servers" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "I wasn't able to connect to Redgar Servers. Please update my abilities",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif 'power point presentation' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Opening the Powerpoint presentation",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                power = r"C:\\Users\\bedga\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
                os.startfile(power)

            elif "who are you" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "I am a powerful virtual assistant created by you",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif 'what is the reason for you' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "I was created as an all purpose assistant for Redgar",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif 'change background' in query:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                           0,
                                                           "Location of wallpaper",
                                                           0)
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Background changed successfully",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif 'open chrome' in query:
                appli = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                os.startfile(appli)

            elif 'open bluestack' in query:
                appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
                os.startfile(appli)

            elif 'give me the latest Ohdis news' in query:

                try:
                    jsonObj = urlopen(
                        "http://newsapi.org/v2/top-headlines?country=us&apiKey=dca53cb1a8a34b10890c6b1f4031eb79")
                    data = json.load(jsonObj)
                    i = 1
                    with open('Ohdis_voice.wav', 'wb') as audio_file:
                        audio_file.write(
                            text_to_speech.synthesize(
                                "Here are some News Articles in Modern Day America",
                                voice=OhdisVoice,
                                accept='audio/wav'
                            ).get_result().content)
                        vlc_instance = vlc.Instance()
                        player = vlc_instance.media_player_new()
                        media = vlc_instance.media_new('Ohdis_voice.wav')
                        player.set_media(media)
                        player.play()
                        time.sleep(.100)
                        duration = player.get_length() / 1000
                        time.sleep(duration)
                    print('''=============== Ohdis News Service ============''' + '\n')

                    for item in data['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        with open('Ohdis_voice.wav', 'wb') as audio_file:
                            audio_file.write(
                                text_to_speech.synthesize(
                                    str(i) + '. ' + item['title'] + '\n',
                                    voice=OhdisVoice,
                                    accept='audio/wav'
                                ).get_result().content)
                            vlc_instance = vlc.Instance()
                            player = vlc_instance.media_player_new()
                            media = vlc_instance.media_new('Ohdis_voice.wav')
                            player.set_media(media)
                            player.play()
                            time.sleep(.100)
                            duration = player.get_length() / 1000
                            time.sleep(duration)
                        i += 1
                except Exception as e:

                    print(str(e))


            elif 'lock window' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Locking the Device as we speak",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                ctypes.windll.user32.LockWorkStation()

            elif 'shutdown system' in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Shutting down system. Please wait",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                subprocess.call('shutdown / p /f')

            elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Recycled sir",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif "don't listen" in query or "stop listening" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "How long do you want me to stop listening to commands?",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                a = int(takeCommand())
                time.sleep(a)
                print(a)

            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "User asked to locate",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            location,
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")

            elif " Ohdis, capture this" in query or "Ohdis, take a photo" in query:
                ec.capture(0, "Ohdis Camera ", "img.jpg")

            elif "restart" in query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in query or "sleep" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "hibernating, sir",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                subprocess.call("shutdown / h")

            elif "send a message Myself " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'ACd1de7515ba7a952a177abbe1a31284ca'
                auth_token = 'e84ed74773e47aa18cbe484ba46759f9'
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body=takeCommand(),
                    to='+2033433094',
                    from_='+20555707522'
                )
                print(message.sid)

            elif "send a message to Dad" in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'ACd1de7515ba7a952a177abbe1a31284ca'
                auth_token = 'e84ed74773e47aa18cbe484ba46759f9'
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body=takeCommand(),
                    to='+2036412470',
                    from_='+20555707522'
                )
                print(message.sid)


            elif "log off" in query or "sign out" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Make sure all applications are closed before I log you off",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "write a note" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "What should I write sir?",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                note = takeCommand()
                file = open('OhdisNotes.txt', 'w')
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Should I include the date and time sir?",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime(datetime.datetime.now())
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "show note" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Showing notes",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                file = open("Ohdis.txt", "r")
                print(file.read())
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            file.read(6),
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif "update assistant from Redgar Web Servers" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "Make sure to replace this version with the one you downloaded",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                url = '# url after uploading file'
                r = requests.get(url, stream=True)

                with open("Voice.py", "wb") as Pypdf:

                    total_length = int(r.headers.get('content-length'))

                    for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                           expected_size=(total_length / 1024) + 1):
                        if ch:
                            Pypdf.write(ch)

            elif "weather" in query:

                # Google Open weather website
                # to get API of Open weather
                api_key = "7371ccb8ebcab3ed0b15865b879ed1e2"
                base_url = "http://api.openweathermap.org/ data/2.5/weather?"
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            " City name ",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                print("City name : ")
                city_name = takeCommand()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidity = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in kelvin unit) = " + str(
                        current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                        current_pressure) + "\n humidity (in percentage) = " + str(
                        current_humidity) + "\n description = " + str(weather_description))

                else:
                    with open('Ohdis_voice.wav', 'wb') as audio_file:
                        audio_file.write(
                            text_to_speech.synthesize(
                                "City not found",
                                voice=OhdisVoice,
                                accept='audio/wav'
                            ).get_result().content)
                        vlc_instance = vlc.Instance()
                        player = vlc_instance.media_player_new()
                        media = vlc_instance.media_new('Ohdis_voice.wav')
                        player.set_media(media)
                        player.play()
                        time.sleep(.100)
                        duration = player.get_length() / 1000
                        time.sleep(duration)

            elif "wikipedia" in query:
                webbrowser.open("wikipedia.com")

            elif "Good Morning" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "A warm" + query,
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "How are you sir?",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif "what do you say?" in query or "are we all set?" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "I have indeed been uploaded sir",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif "how are you" in query:
                with open('Ohdis_voice.wav', 'wb') as audio_file:
                    audio_file.write(
                        text_to_speech.synthesize(
                            "I am always fine. I am glad that you said that",
                            voice=OhdisVoice,
                            accept='audio/wav'
                        ).get_result().content)
                    vlc_instance = vlc.Instance()
                    player = vlc_instance.media_player_new()
                    media = vlc_instance.media_new('Ohdis_voice.wav')
                    player.set_media(media)
                    player.play()
                    time.sleep(.100)
                    duration = player.get_length() / 1000
                    time.sleep(duration)

            elif "what is" in query or "who is" in query:

                # Use the same API key
                # that we have generated earlier
                client = wolframalpha.Client("Q3VJ62-L4633H2774")
                res = client.query(query)

                try:
                    print(next(res.results).text)
                    with open('Ohdis_voice.wav', 'wb') as audio_file:
                        audio_file.write(
                            text_to_speech.synthesize(
                                next(res.results).text,
                                voice=OhdisVoice,
                                accept='audio/wav'
                            ).get_result().content)
                        vlc_instance = vlc.Instance()
                        player = vlc_instance.media_player_new()
                        media = vlc_instance.media_new('Ohdis_voice.wav')
                        player.set_media(media)
                        player.play()
                        time.sleep(.100)
                        duration = player.get_length() / 1000
                        time.sleep(duration)
                except StopIteration:
                    print("No results")

                # elif "" in query:
            # Command go here
            # For adding more commands
            else:
                continue
