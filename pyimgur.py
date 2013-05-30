"""
PyImgur - Python IMGUR API wrapper
"""

import pycurl
from xml.dom import minidom
import cStringIO
from xml.dom import minidom as xml
import local_settings

# SET YOUR ANONYMOUS IMGUR KEY IN LOCAL_SETTINGS.PY (RENAME FROM .DIST)
anon_key = local_settings.ANNON_KEY

class UploadImage():
	"""Upload images to imgur
	  returns either .error or .imageURL

	TO DO:

	POSSIBLE TO DO:
		- add stats and image info functions
		- allow for full JSON responses instead of having to manually parse XML
	"""
	def __init__(self,image="",dhash="",delete=False):
		self.c = pycurl.Curl()
		self.response = cStringIO.StringIO()
		self.minidom = minidom
		self.image = image
		self.dhash = dhash.__str__()
		self.delete = delete
		self.message = ""
		self.imageURL = {}
		self.error = []

		if self.dhash and self.delete:
			self.wipe()
		else:
			self.upload()

	def upload(self):
		"Upload anonymously to imgur"
		params = [
				("key", anon_key),
				("image", (self.c.FORM_FILE, self.image))
			]
		self.c.setopt(self.c.URL, "https://api.imgur.com/2/upload.xml")
		self.c.setopt(self.c.HTTPPOST, params)
		self.c.setopt(self.c.WRITEFUNCTION, self.response.write)

		try:
			self.c.perform()
			self.c.close()
		except:
			self.error.append("Problem uploading image.")

		if not self.error:
			self.parseXML()

		return self.message,self.imageURL,self.error

	def wipe(self):
		deleteURL = "https://api.imgur.com/2/delete/%s" % self.dhash
		self.c.setopt(self.c.URL, deleteURL)
		self.c.setopt(self.c.WRITEFUNCTION, self.response.write)

		try:
			self.c.perform()
			self.c.close()
		except:
			self.error.append("Problem deleting image.")

		if not self.error:
			self.parseXML(delete=True)

	def parseXML(self,delete=False):
		try:
			xml = self.minidom.parseString(self.response.getvalue())
			if delete:
				self.message = xml.getElementsByTagName("message")[0].firstChild.data
			else:
				self.imageURL['url'] = xml.getElementsByTagName("original")[0].firstChild.data
				self.imageURL['hash'] = xml.getElementsByTagName("hash")[0].firstChild.data
				self.imageURL['deletehash'] = xml.getElementsByTagName("deletehash")[0].firstChild.data
				self.imageURL['smallthumb'] = xml.getElementsByTagName("small_square")[0].firstChild.data
				self.imageURL['bigthumb'] = xml.getElementsByTagName("large_thumbnail")[0].firstChild.data
		except:
			self.error.append("Problem parsing XML output.")
