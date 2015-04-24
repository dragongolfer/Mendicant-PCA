#libraries to import, has to be +2
import Slavy to call from to generate intelligent agents#not open source cant use
import wget to aid scrapy amongst other things
import fuzzywuzzy
import progressbar adds a progressbar#for when Instances are working on larger problems
import scrapy for webscraping
import uuid to store hasinig, key/value stores, unique ids(for the agents)
import subprocess to manage nodes
import math
import numbers# see 9.1.1. The numeric tower in python documentation
#10 functions
#robots.txt is a warning file not a forbid file so you can still scrape a site that doesnt want you to but it might be violating there Terms of Use
define the intelligent control system that controls all of the "node" agents
define behavior by overriding actions
define the agent and the behavior tha agent will preform
define an application class for the agent to act on the behavior it will recieve
define webscraping most likely with scrapy
define storage of archived material probably with mongodb
define mathematics agent(for complex math required by other fuinctions to call from)
define text interface for communication between node and master agents and the user
if not included define communication between nodes 


define MendicantBot():
	Master bot, run when program starts and call from botmanager
	define control system that talks to BotManager
	call BotManager to spawn a node for a particular task that it oversees 
# Functions below except maybe botmanger call all from another file
define BotManager():
	subprocess.spawn(MendicantBotNode) #spawns MendicantBotNodes
		define agent type from a list of possible agents
		Popen.
		define communication between bots and MendicantBot

define MendicantBotInstance():
	call functions from another file

define math():
	here all the different types of math to do and they can all go in one function

define MendicantArchive():
	where data the bot has scraped is stored for recall later




	