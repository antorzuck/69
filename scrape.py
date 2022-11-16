import requests
from bs4 import BeautifulSoup as B
from my_fake_useragent import UserAgent
import random
import mechanicalsoup
from requests.auth import HTTPBasicAuth
import json
import sys
import gen_thumbnail

def create_post(ttl, content, thumb):
    base_url = "https://quotesholy.com/wp-json/wp/v2/posts"

    headers = {
    "Accept" : "application/json",
    "Content-Type" : "application/json"
}

    auth = HTTPBasicAuth("Auto", "XLO2 F2EM liMY ild4 9B0R jMMd")

    data = json.dumps({                                    "status" : "draft",
"title" : ttl,
"content" : content,
"featured_media" : os.listdir(f'thumbnail/{thumb}')
})

    req = requests.post(url=base_url, data=data, headers=headers, auth=auth)



kw = str(input("Type keyword: "))


if kw == "blank":
    create_post(ttl=" ", content=" ")
    print("blank created")
    sys.exit()
scrape_num = int(input("How many pages you want to scrape? (limit is 10) "))
  
browser = [
    'chrome',
    'firefox',
    'edge',
    'ie',
    'opera',
    'safari',
]

os = [
    'windows',
    'linux',
    'mac',
    'ios',
    'chrome os',
]

ua = UserAgent(family=random.choice(browser), os_family=random.choice(os))

headers = {
    'user-agent': str(ua.random)
}



url = f"https://www.google.com/search?q={kw}"

req = requests.get(url=url, headers=headers)
print(req)
soup = B(req.text, 'html.parser')

link = soup.find_all('a')
all_links = []
main_links=[]
p = ""
body = ""
for i in link:
    if i['href'].startswith('/url?'):
        i = i['href'].replace('/url?q=', "")
        i = i.split('&')
        all_links.append(i)

for i in all_links:
    if not i[0].startswith('https://support'):
        if not i[0].startswith('https://accounts'):
            if not i[0].startswith('https://www.pinterest'):
            	main_links.append(i[0])

for c,i in enumerate(main_links):
    if c == scrape_num:
    	break
    res = requests.get(url=i)
    sp = B(res.text, 'html.parser')
    li = sp.find_all('li')
    if i.startswith('https://benextbrand'):
    	p = sp.find('div', class_='entry-content')

    for l in li:
        if len(l.text.strip()) > 20:
        	f = l.text
       
        	if not 'Caption' in f:
        		if not 'Instagram' in f:
        			if not 'Facebook' in f:
        				if not 'Status' in f:
        					if not 'Best' in f:
        						if not 'Message' in f:
        							if not 'Quotes' in f:
        								if not f in body:
        									body = body + f + '\n'
    if p:
    	for pt in p.find_all('p')[1:]:
    		if not pt.text in body:
    			body = body + pt.text + '\n'


if '"' in body:
	body = body.replace('"', "")
if '“' in body:
	body = body.replace('“', "")
	
if '”' in body:
	body = body.replace('”', "")

print("captions collected going to post this shit on wp")


thumb = gen_thumbnail.create_thumb(text=kw.title())

create_post(ttl=kw.title(), content=body, thumb=thumb)

print("posted...")
