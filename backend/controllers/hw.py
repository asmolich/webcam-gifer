import webapp2
from google.appengine.ext.webapp import util


class HwHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
            <html><body><form action="/upload" method="get">Upload File:<br/>
            <input type="file" name="file" /><br/>
            <input type="file" name="file" /><br/>
            <input type="file" name="file" /><br/>
            <input type="submit" name="submit" value="Submit" />
            </form></body></html>""")


def main():
    application = webapp2.WSGIApplication([('/', HwHandler)], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
