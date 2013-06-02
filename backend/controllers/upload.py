import webapp2
import urllib
from lib.images2gif_custom import writeGif
from PIL import Image
import cStringIO
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import base64
import json
import logging


class UploadHandler(webapp2.RequestHandler):

    def post(self):
        #upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
        file_param = self.request.get_all('file', default_value='{}')
        logging.debug("file_param =  %s", type(file_param))
        upload_files = json.loads(file_param[0])

        images = []
        if type(upload_files) is list:
            for fn in upload_files:
                # print fn
                # file_from = cStringIO.StringIO()
                # file_from.write(fn)
                # file_to = cStringIO.StringIO()
                # print
                # print file_from
                # base64.decode(file_from, file_to)
                # print
                # print file_to
                images.append(Image.fromstring("RGBA", (800, 600), fn))
        else:
            images.append(Image.open(upload_files))

        # images = [Image.open(fn) for fn in upload_files]

        size = (300, 300)
        for im in images:
            im.thumbnail(size, Image.ANTIALIAS)

        out = cStringIO.StringIO()

        writeGif(out, images, duration=0.2)
        self.response.headers['Content-Type'] = "image/gif"
        self.response.out.write(out.getvalue())


# class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
#     def post(self):
#         upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
#         blob_info = upload_files[0]
#         self.redirect('/serve/%s' % blob_info.key())


class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        self.send_blob(blob_info)
