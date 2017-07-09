import requests
import os
from bs4 import BeautifulSoup
from gtts import gTTS


def news():

    content = " "
    # the target we want to open
    url = 'http://www.hindustantimes.com/top-news'

    # open with GET method
    resp = requests.get(url)

    # http_response 200 means OK status
    if resp.status_code == 200:
        print("Successfully Scrapped")
        print("The news is as follow :-\n")

        # we need a parser,Python built-in HTML parser is enough .
        soup = BeautifulSoup(resp.text, 'html.parser')
        #print(soup.prettify())
        # l is the list which contains all the text i.e news
        l = soup.find("ul", attrs={'class': 'latest-news-bx more-latest-news more-separate'})
        #Notice here its findAll, above it was find only
        # find all the elements of a, i.e anchor
        for i in l.findAll("a"):
            content += i.text
            content += "."
            content += ","
        return content
    else:
        content = "Error Occurred"
        return content


news_found = news()
language = 'en'
myobj = gTTS(text=news_found, lang=language, slow=False)
myobj.save("news.mp3")
os.system("news.mp3")

