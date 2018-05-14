from lxml import html
import requests
import sys
import re

topics = ['WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'ENTERTAINMENT', 'SPORTS', 'SCIENCE', 'HEALTH']
for topic in topics:
    #topic = sys.argv[1]
    url = 'https://news.google.com/news/headlines/section/topic/%s?ned=us&hl=en&gl=US' % topic
    page = requests.get(url)
    tree = html.fromstring(page.content)
    raw_headlines = tree.xpath('//a[@role="heading"]/text()')

    headlines = []
    for h in raw_headlines:
        h = re.split(r"[\-\s]+", h)
        words = [re.sub(r'\W+', '', word).lower() for word in h]
        print(topic + ',' + ' '.join(words))

