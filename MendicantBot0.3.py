import pymongo
import json

class MendicantBot(object):
	def __init__(self):
		self.name = None
	def nameBot(self):
		self.name = name


class MendicantNodeFactory(object):
	def __init__(self):
		self.message = "Creating node^^^"
	def spawnNode(self, nodename):
		newNode = MendicantBot()
		newNode = nameBot(name)


class NodeManager(object):
	def __init__(self):
		self.nodelist = []
		MendicantBot = MendicantNodeFactory()
		self.botcount = 0
	
	def addNodeNamed(self, nodename):

	def killNodeNamed(self, nodename):

	def findNodeNamed(self, nodename):

	def reallocateNodeNamed(self, nodename):

	def rampantNodeCheck(self, nodename):








class MendicantArchive(object):
	def __init__(self):
	self.db = pymongo.MongoClient().Archive#creates connection to MongoDB and creates 'Archive' database
	self.db.Archive.insert(data)#inserts into db
	data = json.loads(Archive)#passes json into self.db.Archive.insert
	db.Archive.save(self, Archive)#where data the bot has scraped is stored for recall later