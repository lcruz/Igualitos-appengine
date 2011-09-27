from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import appengine_admin
import admin

application = webapp.WSGIApplication([
	# Admin pages
	(r'^(/admin)(.*)$', appengine_admin.Admin),
])

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()