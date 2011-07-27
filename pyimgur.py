"""
PyImgur - Python IMGUR API wrapper
"""

import pycurl
from xml.dom import minidom
import cStringIO
from xml.dom import minidom as xml


# SET YOUR ANONYMOUS IMGUR KEY HERE
anon_key = "******************"

class UploadImage():
	"""
	Upload images to imgur
	  returns either .error or .imageURL

	TO DO:

	POSSIBLE TO DO:
		- add stats and image info functions
		- allow for full JSON responses instead of having to manually parse XML

	"""

	# Not very verbose at the moment in terms of errors - will build on that later
	def __init__(self,image="",dhash="",delete=False):

		# setup some initial items and placeholders we will need
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
			# if we have a hash and a delete trigger, lets try to wipe the image
			self.wipe()
		
		else:
			# fire away an upload - we will return an imageURL dictionary with attributes or an error
			self.upload()


	def upload(self):
		"Upload anonymously to imgur"

		# setup the basic parameters
		params = [
				("key", anon_key),
				("image", (self.c.FORM_FILE, self.image))
			]
			
		# setup the url and pipe in our key and image
		self.c.setopt(self.c.URL, "http://api.imgur.com/2/upload.xml")
		self.c.setopt(self.c.HTTPPOST, params)
		
		# we want to capture the output so lets set the write output to go to our cStringIO so we can parse it
		self.c.setopt(self.c.WRITEFUNCTION, self.response.write)

		try:
			# run it
			self.c.perform()
			self.c.close()
			
		except:
			self.error.append("Problem uploading image.")

		if not self.error:
			# parse the xml
			self.parseXML()
			

		return self.message,self.imageURL,self.error
		

	def wipe(self):
		"Wipe an anonymouse image from imgur"

		deleteURL = "http://api.imgur.com/2/delete/%s" % self.dhash
		
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
		"Parse the XML ouput from IMGUR and write to the imageURL dictionary"
		
		try:
			# parse the XML string into the dom
			xml = self.minidom.parseString(self.response.getvalue())

			if delete:
				self.message = xml.getElementsByTagName("message")[0].firstChild.data

			else:
				# grab out some helpful/interesting data and setup in the imageURL dictionary
				self.imageURL['url'] = xml.getElementsByTagName("original")[0].firstChild.data
				self.imageURL['hash'] = xml.getElementsByTagName("hash")[0].firstChild.data
				self.imageURL['deletehash'] = xml.getElementsByTagName("deletehash")[0].firstChild.data
				self.imageURL['smallthumb'] = xml.getElementsByTagName("small_square")[0].firstChild.data
				self.imageURL['bigthumb'] = xml.getElementsByTagName("large_thumbnail")[0].firstChild.data

		except:
			self.error.append("Problem parsing XML output.")
