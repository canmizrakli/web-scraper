def getLink(soup):
    news_link = soup.find_all('link')[0].text
    return news_link


def getTitle(soup):
    news_title = soup.find_all('title')[0].text
    return news_title


def getDescription(soup):
    try:
        description_ = soup.find('meta', {'name': 'Description'})['content']
        return description_
    except:
        # print("Description not found")
        try:
            description_ = soup.find('meta', {'name': 'description'})['content']
            return description_
        except:
            print("Description 2 not found")


def getImage(soup):
    if soup.findAll("meta", property="og:image"):
        return soup.find("meta", property="og:image")["content"]
    else:
        return
    return
