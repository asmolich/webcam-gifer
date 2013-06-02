import urllib
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
        self.response.write('Hello world!')


app = webapp2.WSGIApplication([(root_path, HwHandler,),
                               (image_path, ImageHandler,),
                               (upload_path, UploadHandler,),
                               ('/serve/([^/]+)?', ServeHandler,)], debug = True)


# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         upload_url = blobstore.create_upload_url('/upload')
#         self.response.out.write('<html><body>')
#         self.response.out.write('<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url)
#         self.response.out.write("""Upload File:<br/>
#             <input type="file" name="file"><br/>
#             <input type="file" name="file"><br/>
#             <input type="file" name="file"><br/>
#             <input type="submit" name="submit" value="Submit" />
#             </form></body></html>""")
#
#
# class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
#     def post(self):
#         upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
#         blob_info = upload_files[0]
#         self.redirect('/serve/%s' % blob_info.key())
#
#
# class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
#     def get(self, resource):
#         resource = str(urllib.unquote(resource))
#         blob_info = blobstore.BlobInfo.get(resource)
#         self.send_blob(blob_info)
#
# app = webapp2.WSGIApplication([('/', MainHandler),
#                                ('/upload', UploadHandler),
#                                ('/serve/([^/]+)?', ServeHandler)],
#                               debug=True)