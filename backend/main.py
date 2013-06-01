import webapp2
from controllers.hw import HwHandler
from controllers.image import ImageHandler


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


app = webapp2.WSGIApplication([('/', HwHandler,),
                               ('/image', ImageHandler,)], debug=True)
