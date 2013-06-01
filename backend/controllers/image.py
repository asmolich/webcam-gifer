from google.appengine.ext import webapp

from google.appengine.ext.webapp import util

from lib.images2gif import writeGif
from PIL import Image
import os


class ImageHandler(webapp.RequestHandler):
    def get(self):
        path = os.path.dirname(__file__)
        file_names = sorted((fn for fn in os.listdir('static') if fn.endswith('.jpeg')))
        print file_names
        images = [Image.open("%s/../static/%s" % (path, fn)) for fn in file_names]

        size = (150, 150)
        for im in images:
            im.thumbnail(size, Image.ANTIALIAS)

        print writeGif.__doc__

        filename = path + "my_gif.GIF"
        writeGif(filename, images, duration=0.2)

        self.response.out.write('Hi there! Upload images')
        #writeGif(self.response.out, images, duration=0.2)


def main():
    application = webapp.WSGIApplication([('/image', ImageHandler)], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
