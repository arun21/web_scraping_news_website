#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import csv
#import hyperlink

source = requests.get("https://inshorts.com/en/read/world").text
soup = BeautifulSoup(source, 'lxml')

today_date = datetime.now().strftime("%d %b %Y")

for i, article in enumerate(soup.find_all('div', class_="news-card-title news-right-box")):
    titles = article.find('a', class_='clickable').text.strip()
    d_filter = article.find('div', class_='news-card-author-time news-card-author-time-in-title').text.split("/")[1].strip().replace('\n', '')
    date = d_filter.split(",")[0].partition("on")[-1]
    article_link = "https://inshorts.com" + article.a['href']
    #links = hyperlink.parse(url=ulink)
    
    if i == 0:
        operator = 'w'
    else:
        operator = 'a'
        
    with open('Inshorts.csv', operator) as csv_file:
        fieldnames=["Date", "News Title", "Link"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if i == 0:
            writer.writeheader()
        if date.strip() == today_date:
            writer.writerow({'Date': date, 'News Title': titles, 'Link': article_link})
        
print("Inshorts.csv Successfully Created")

try:
          receiver = "arun21@gmail.com"
          body = "Lastest News from Insorts"
          filename = "Inshorts.csv"

          yag = yagmail.SMTP(user='my_username@gmail.com', password='password')
          yag.send(
          to=receiver,
          subject="Insorts Top news",
          contents=body, 
          attachments=filename,
          )
          print("Email sent successfully")
except:
    print("Error, email was not sent")
          