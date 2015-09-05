import requests
from bs4 import BeautifulSoup as bs
import csv

import datetime
now = str(datetime.datetime.now().isoformat())

def num(raw):
    return ''.join(raw.split(","))

startTime = datetime.datetime.now().isoformat()

count = 0
with open("links.txt", "r") as links, open("output/output-"+now+".csv", "w",  encoding='utf-8') as output:
    csvw = csv.writer(output)
    csvw.writerow(['title', 'watchViewCount', 'likeCount', 'unlikeCount', 'subscriberCount', 'commentCount'])

    for link in links.readlines():
        id = link.split("v=")[-1]
        url = 'https://www.youtube.com/watch?v=' + id

        res = requests.get(url)
        soup = bs(res.text, "html.parser")

        title = soup.select('#eow-title')[0].text.strip()
        watchViewCount = num(soup.select('.watch-view-count')[0].text.strip())
        likeCount = num(soup.select('.like-button-renderer-like-button > .yt-uix-button-content')[0].text.strip())
        unlikeCount = num(soup.select('.like-button-renderer-dislike-button > .yt-uix-button-content')[0].text.strip())

        try:
            commentUrl = 'https://www.youtube.com/all_comments?v=' + id
            res2 = requests.get(commentUrl.strip())
            soup2 = bs(res2.text, "html.parser")
            commentCount = num(soup2.select('.all-comments > a')[0].text.strip().split()[-1].strip('()'))
        except Exception as e:
            commentCount = 0
            # print(commentUrl.strip()) print(soup2.select('a')[0].text, e)

        try:
            subscriberCount = ''.join(soup.select('.yt-subscriber-count')[0].text.split(',')).strip()
        except:
            subscriberCount = 0

        csvw.writerow([title, watchViewCount, likeCount, unlikeCount, subscriberCount, commentCount])
        print('#{} completed.'.format(count))
        count += 1

endTime = datetime.datetime.now().isoformat()

print('開始抓取時間{}\t結束抓取時間{}'.format(startTime, endTime))
