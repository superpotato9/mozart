import requests
from bs4 import BeautifulSoup
import re


def getHTMLdocument(url):
    # request for HTML document of given url
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text


#url = str(input('song name:'))
def scrape(url):
    url_to_scrape = 'https://www.google.com/search?q=' + url.replace(' ', '+') + '+lyrics'

    html_document = getHTMLdocument(url_to_scrape)




    def remove_tags(html):
        # parse html content
        soup = BeautifulSoup(html, "html.parser")

        for data in soup(['style', 'script']):
            # Remove tags
            data.decompose()

        # return data by retrieving the tag content
        return ' '.join(soup.stripped_strings)


    # Print the extracted data
    text_dirty = remove_tags(html_document)


    #print(text_dirty_list)
    first = text_dirty.find('/')
    text_dirty = text_dirty[first:].replace('/', '',1)


    second = text_dirty.find('Source:')

    #print(text_dirty[:second])
    if ' Google Search G o o g l e G o o g l e' in text_dirty[:second]:
        return ''
    else:
        return text_dirty[:second]

    #print(text_dirty)



# print(scrape('promises beach bunny'))
#print(text_less_dirty)





















