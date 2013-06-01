import urllib
from lib.images2gif_custom import writeGif
from PIL import Image
import cStringIO
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
        images = [Image.open(fn) for fn in upload_files]

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
