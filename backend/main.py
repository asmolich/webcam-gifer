import webapp2
from controllers.hw import HwHandler
from controllers.image import ImageHandler
from controllers.upload import UploadHandler
from controllers.upload import ServeHandler
from google.appengine.ext import blobstore

root_path = '/'
image_path = '/image'
upload_path = '/upload'


class MainHandler(webapp2.RequestHandler):
    def get(self):
        upload_url = blobstore.create_upload_url(upload_path)
        self.response.write('Hello world!')


app = webapp2.WSGIApplication([(root_path, HwHandler,),
                               (image_path, ImageHandler,),
                               (upload_path, UploadHandler,),
                               ('/serve/([^/]+)?', ServeHandler,)], debug = True)
