import requests
from bs4 import BeautifulSoup
import getContent
import json
import feedparser

if __name__ == '__main__':
    news_links = ['https://www.fotomac.com.tr/nba/2023/01/24/alperen-sengunlu-houston-rockets-13-mac-sonra-kazandi',
                  'https://www.donanimhaber.com/google-20-yillik-calisanini-e-posta-ile-kovdu--159730',
                  'https://www.hurriyet.com.tr/kelebek/magazin/shakiraya-yeni-sok-bu-is-artik-resmi-gerard-pique-yeni-askiyla-ilk-instagram-paylasimini-yapti-42209904']

    all_news_links = []

    url = "https://www.cumhuriyet.com.tr/rss/gundem.xml"

    news_feed = feedparser.parse(url)

    # all_news_links.append(news_feed.entries[1].link)

    for each_news in range(0, len(news_feed.entries)):
        all_news_links.append(news_feed.entries[each_news].link)

    print(all_news_links)

    feed_data = []
    for feed_news in range(0, len(all_news_links)):
        title = news_feed.entries[feed_news].title
        description = news_feed.entries[feed_news].description
        og_image = news_feed.entries[feed_news].thumbnail

        news_data = {
            'title': title,
            'image': og_image,
            'description': description
        }
        # print(str(title) + "\n" + str(description) + "\n" + str(og_image))
        feed_data.append(news_data)

    with open("sample_all_feed.json", "w") as write_file:
        json.dump(feed_data, write_file, indent=4, ensure_ascii=False)

    data = []
    for new in news_links:
        reqs = requests.get(new)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        title = getContent.getTitle(soup)
        description = getContent.getDescription(soup)
        og_image = getContent.getImage(soup)

        news_data = {
            'title': title,
            'image': og_image,
            'description': description
        }
        # print(str(title) + "\n" + str(description) + "\n" + str(og_image))
        data.append(news_data)

    with open("sample.json", "w") as write_file:
        json.dump(data, write_file, indent=4, ensure_ascii=False)
