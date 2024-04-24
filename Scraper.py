import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')
# Merging pages
# response2 = requests.get('https://news.ycombinator.com/?p=2')
# soup2 = BeautifulSoup(response2.text, 'html.parser')
# links2 = soup2.select('.titleline > a')
# subtext2 = soup2.select('.subtext')
# merged_links = links + links2
# merged_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))
# pprint.pprint(create_custom_hn(merged_links, merged_subtext))
