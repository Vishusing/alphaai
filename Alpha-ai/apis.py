import requests
import pyttsx3 as p

def speak(text):
    engine.say(text)
    engine.runAndWait()

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def jokes(topic):
 url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"

 querystring = {"format":"json","contains":f"{topic}","idRange":"0-150","blacklistFlags":"nsfw,racist"}

 headers = {
	"X-RapidAPI-Key": "868380ffddmsh4880ca9d7d65994p1acc6fjsn1a25186c8770",
	"X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
}

 response = requests.get(url, headers=headers, params=querystring).json()
 if 'message' in response:
   speak('No matching jokes found... Consider another topic...')
 else:
  print(f"1. {response['setup']}")
  speak(response['setup'])
  print(f"   {response['delivery']}")
  speak(response['delivery'])
jokes('ice')


def news(topic):
 url = "https://real-time-news-data.p.rapidapi.com/search"

 querystring = {"query":f"{topic}","country":"IN","lang":"en"}

 headers = {
	"X-RapidAPI-Key": "868380ffddmsh4880ca9d7d65994p1acc6fjsn1a25186c8770",
	"X-RapidAPI-Host": "real-time-news-data.p.rapidapi.com"
}

 response = requests.get(url, headers=headers, params=querystring).json()

 for i in range(len(response['data'])):
  print(f"{response['data'][i]['title']} \n")
  speak(response['data'][i]['title'])
