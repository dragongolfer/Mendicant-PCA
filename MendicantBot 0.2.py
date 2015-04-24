#libraries to import, has to be +2
#import Slavy to call from to generate intelligent agents#not open source cant use
import wget to aid scrapy amongst other things
import fuzzywuzzy
import progressbar adds a progressbar#for when Instances are working on larger problems
import scrapy for webscraping
import uuid to store hasinig, key/value stores, unique ids(for the agents)
import subprocess to manage nodes
import mongodb#manages database 
import math
import numbers# see 9.1.1. The numeric tower in python documentation
#10 functions
#robots.txt is a warning file not a forbid file so you can still scrape a site that doesnt want you to but it might be violating there Terms of Use
#define the intelligent control system that controls all of the "node" agents
#define behavior by overriding actions
#define the agent and the behavior tha agent will preform
#define an application class for the agent to act on the behavior it will recieve
#define webscraping most likely with scrapy
#define storage of archived material probably with mongodb
#define mathematics agent(for complex math required by other fuinctions to call from)
#define text interface for communication between node and master agents and the user
#if not included define communication between nodes 

def main():#main function drives enterity of the program
	MasterBot = MendicantBot()#creates masterbot 
	MasterBot.startNodeManager()#starts nodemanager
	continue
class MendicantBot(object):#Master bot, run when program starts and call from nodemanager
	def __init__(self):#constructor tied to MasterBot in main() above
		print "MendicantBot is now running, how may we help you?"
	def startNodeManager(self):#ties node manager into Masterbot
		NodeManager = NodeManager()
		print "NodeManager is running..."	
		
	#define control system that talks to BotManager
	#call BotManager to spawn a node for a particular task that it oversees 
# Functions below except maybe botmanger call all from another file
class NodeManager(object):
	def startMendicantNodeFactory(self):#ties nodefactory into nodemanager
		MendicantNodeFactory = MendicantNodeFactory()#creates node
		MendicantNodeFactory.startMendicantNodeFactory()
		pass
	self.nodename = name
	self.botlist = []
	def __init__(self, name):
		print "Spawning", self.nodename

	def __del__(self, name):
		print "Killing", self.nodename

class MendicantNodeFactory(object):
	nodeCount = 0
	def __new__(MendicantBotNodes, name, function):
		MendicantBotNodes.name = name
		MendicantBotNodes.function = function
		NodeManager.nodeCount += 1
		#subprocess.spawn(MendicantBotNode) #spawns MendicantBotNodes
		#define agent type from a list of possible agents
		#define bot function givin bot instance number
		#Popen.
		#define communication between bots and MendicantBot

class MendicantBotNodes(object):
	def __init__(self):
	#call functions from another file

class MendicantArchive(object):
	def __init__(self):
	self.db = pymongo.MongoClient().Archive#creates connection to MongoDB and creates 'Archive' database
	self.db.Archive.insert(data)#inserts into db
	data = json.loads(Archive)#passes json into self.db.Archive.insert
	db.Archive.save(self, Archive)#where data the bot has scraped is stored for recall later

if __name__ == "__main__":
	main()

class math(object):
	def __init__(self):
		self.numbers = numbers.complex("Enter your problem/s", raw_input())
		print self.numbers
		#here all the different types of math to do and they can all go in one function


	