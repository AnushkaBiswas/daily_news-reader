#tells daily news

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak= Dispatch("SAPI.Spvoice")
    speak.Speak(str)

#based on news categories
def business():
    speak("Today's business news...")
    url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news =json.loads(news)
    art=news['articles']

    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")


def science():
    speak("Today's Science news...")
    url="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news=json.loads(news)
    art=news['articles']
    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")

def sports():
    speak("today's sports news....")
    url="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news=json.loads(news)
    art=news['articles']
    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")

def entertainment():
    speak("Today's news...")
    url="https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news=json.loads(news)
    art=news['articles']
    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")

def technology():
    speak("Today's technology news...")
    url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news=json.loads(news)
    art=news['articles']
    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")

def health():
    speak("today's Health news...")
    url="https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=cd0a4eecf0c546c6bd2d6fc97f78e6f5"
    news=requests.get(url).text
    news=json.loads(news)
    art=news['articles']
    for article in art:
        speak(article['title'])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening..!")


if __name__ == '__main__' :
    speak("Today's news....lets begin")   #function called and todays news string is passed for speaking
    speak("Press 1 for business news.. press 2 for entertainment news..press 3 for health news...press 4 for sports news..press 5 for scince news..press 6 for technology news")
    while True:
        n=int(input("Press here :"))
        if(n==1):
            business()
        elif(n==2):
            entertainment()
        elif(n==3):
            health()
        elif(n==4):
            sports()
        elif(n==5):
            science()
        elif(n==6):
            technology()
        else:
            speak("Invalid press...!")
    