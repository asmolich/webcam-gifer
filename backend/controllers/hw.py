from google.appengine.ext import webapp

from google.appengine.ext.webapp import util


class HwHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hi there!')


def main():
    application = webapp.WSGIApplication([('/', HwHandler)], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
