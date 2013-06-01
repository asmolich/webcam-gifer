import webapp2
from google.appengine.ext.webapp import util

from lib.images2gif_custom import writeGif
from PIL import Image
import os
import cStringIO


class ImageHandler(webapp2.RequestHandler):

    def get(self):
        path = os.path.dirname(__file__)
        file_names = sorted((fn for fn in os.listdir('static') if fn.endswith('.jpeg')))
        print file_names
        images = [Image.open("%s/../static/%s" % (path, fn)) for fn in file_names]

        size = (300, 300)
        for im in images:
            im.thumbnail(size, Image.ANTIALIAS)

        out = cStringIO.StringIO()

        writeGif(out, images, duration=0.2)
        self.response.headers['Content-Type'] = "image/gif"
        self.response.out.write(out.getvalue())


def main():
    application = webapp2.WSGIApplication([('/image', ImageHandler)], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
