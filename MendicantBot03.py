import pymongo
from pymongo import MongoClient
import json

class MendicantBot(object):#this works 
	def __init__(self):
		self.nodename = None
		self.knowledgebase = {}
	def nameBot(self, nodename):
		self.nodename = nodename
	def intro(self):
		print "This one is", self.nodename
	def outro(self):
		print "This one is", self.nodename



class MendicantNodeFactory(object):#this works
	def __init__(self):
		self.message = "Creating node^^^"
	def spawnNode(self, nodename):# spawns nodes when called, adds name from function above, then identifys itself
		newNode = MendicantBot()
		newNode.nameBot(nodename)
		newNode.intro()
		return newNode


class NodeManager(object):#this works 
    def __init__(self):
		self.nodelist = []
		self.nodeFactory = MendicantNodeFactory()
		self.nodecount = None #starts at None/0 and increases when bots are created
		self.client = MongoClient()
		self.db = self.client.node_structure
		self.collection = self.db.nodes 
	
    def addNodeNamed(self, nodename):#this works no more errors
        newNode = self.nodeFactory.spawnNode(nodename)
        self.nodelist.append(newNode)

    def killNodeNamed(self, nodename):#this function kills nodes that you chose and removes it #not working yet
        chosenNode = None
        for node in self.nodelist:
        	if node.nodename(nodename) is nodename:
        		chosenNode = nodename
        		break
        if chosenNode:
        	self.nodelist.remove(chosenNode)
        else:
        	print "Node does not exist currently biologicals, please try again."
    def findNodeNamed(self, nodename):#this function findes nodes if its in nodelist above
        for node in self.nodelist:
        	if nodename in self.nodelist:
        		print self.nodelist[node]
        	else:
        		print "Node does not exist currently biologicals, please try again."
        		break

    def reallocateNodeNamed(self, nodename):##add these later, harder to integrate
        pass
    def rampantNodeCheck(self, nodename):#ddd these later harder to integrate
        pass

    def printNodeNamed(self):#this now works as well
    	for node in self.nodelist:
    		print "This bots name", node.nodename







#class MendicantArchive(object):
#	def __init__(self):
#	    self.db = pymongo.MongoClient().Archive#creates connection to MongoDB and creates 'Archive' database
#	    self.db.Archive.insert(data)#inserts into db
#	    data = json.loads(Archive)#passes json into self.db.Archive.insert
#	    db.Archive.save(self, Archive)#where data the bot has scraped is stored for recall later