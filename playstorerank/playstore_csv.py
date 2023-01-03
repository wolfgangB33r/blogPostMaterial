"""
Example script for checking the Google App store position 
given an appid and search terms

Streamlit

"""
import requests, time, sched, random, os, ssl
from datetime import datetime
import os.path

YOUR_DT_API_URL = ''
YOUR_DT_API_TOKEN = ''
YOUR_APP_ID = 'at.smartlab.tshop'


KEYWORDS = [
    'pos', 
    'point of sale', 
    'kasse', 
    'restaurant pos', 
    'invoice print', 
    'cashier', 
    'cash register'
    ]
    
LANGUAGES = { 
    'en-US' : "en-US",
    'de-DE' : "de-DE",
    'es-MX' : "es-MX",
    'id-ID' : "id-ID"
}

USERAGENTS = {
    'Android5' : "Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36",
    'Android11' : 'Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36'
}

def checkAppPosition(appid, searchterm, language, useragent):
	try:
		r = requests.get('https://play.google.com/store/search?q=' + searchterm + '&c=apps', headers={"accept-language" : language, "user-agent" : useragent})
		seg = r.text.split('JpEzfb')
		c = 1
		for s in seg:
			if s.find(appid) > 0:
				break
			c = c + 1
		return c - 2
	except ssl.SSLError:
		print("SSL Error")

def persist(appid, agent, lang, searchterm, rank):
    if not os.path.isfile('apprank.csv'):
        f = open("apprank.csv","a")
        f.write("date,metric,store,agent,lang,searchterm,rank\n")
        f.close()
    line = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ",business.store.rank,playstore," + YOUR_APP_ID + ",\"" + agent + "\",\"" + lang + "\",\"" + searchterm + "\"," + rank + "\n"
    f = open("apprank.csv","a")
    f.write(line)
    f.close()

def main():
    for lang in LANGUAGES:
        l = LANGUAGES[lang]
        for agent in USERAGENTS:
            a = USERAGENTS[agent]
            for kw in KEYWORDS:
                rank = str(checkAppPosition(YOUR_APP_ID, kw, l, a))
                persist(YOUR_APP_ID, agent, lang, kw, rank)	
    

if __name__ == '__main__':
    while True:
        main()
        print('.')
        time.sleep(600)
        
    