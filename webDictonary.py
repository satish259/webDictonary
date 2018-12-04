import logging
logger = logging.getLogger()

def parseURLtoText(url):
    '''
        Scrape url and return data as string without control character and in lower case.
    '''
    import requests
    from bs4 import BeautifulSoup

    try:
        page = requests.get(url)
        html = BeautifulSoup(page.text, 'html.parser')

        # Delete tags scripts, styles, head, title, meta etc from html.
        [script.extract() for script in html(['meta','script','style','head','title','[document]'])]

        return html.text.lower().translate(dict.fromkeys(range(32)))
    except requests.exceptions.RequestException as e:
        logger.debug(e)

def countWords(string):
    '''
        Takes in string, removes numbers and special character such as = and ?, splits by space and returns a Counter of words (and their occurances)
        #TODO: Handles English words only!!! All non-English characters are removed. 
        #TODO: Variables, spelling mistakes etc. are all counted as words.
    '''
    import re
    from collections import Counter
    words= re.sub('\d',' ',re.sub(r'\W+', ' ', string)) #Replace non-alpha character with spa
    return Counter(words.split())

def topWords(counter,topX,wordsOnly=False):
    '''
        Returns the topX elements of counter as list with frequency.
        If wordsOnly is True, just the words without their frequency are returned.
    '''
    topXValues=counter.most_common(topX)
    if wordsOnly: topXValues=[n[0] for n in topXValues]
    return topXValues