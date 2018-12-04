import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.web
from webDictonary import parseURLtoText, countWords, topWords

def generateWordCloud(words):
    '''
        Builds and returns an image of a wordcloud
    '''
    from wordcloud import WordCloud
    wordcloud = WordCloud(background_color='white').generate(words)
    return wordcloud.to_image()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", wordcloud=None)

    def post(self):
        url = self.get_argument('get_url', None)
        topCommonWords = topWords(countWords(parseURLtoText(url)),100)
        wordcloud = generateWordCloud(topCommonWords)
        self.render("index.html", wordcloud=wordcloud)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        settings = {
            "debug": True,
            "static_path": os.path.join(os.path.dirname(__file__), "bootstrap")
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
tornado.ioloop.IOLoop.instance().start()
