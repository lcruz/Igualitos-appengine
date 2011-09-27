from google.appengine.ext import db

class Igualito(db.Model):
	imagen1 = db.BlobProperty(default=None)
	imagen2 = db.BlobProperty(default=None)
	nombre = db.StringProperty(multiline=False)
	fecha = db.DateTimeProperty(auto_now_add=True)