from MendicantBot03 import NodeManager
### this calles NodeManager from MendicantBot and all functions in that file
class UserControl(object):
	def __init__(self):
		self.nm = NodeManager()
		self.running = True
		self.quit = "Killing Us and all processes"
		self.rampant = "SsSomething ii/s wwww-rog witg is, attttttempting o reair rampant nnnnodes \n ...logic plague found"
		pass

	def initalize(self):
		yeOrne = str(raw_input("Start terminal if you wish biologicals [ye or ne]"))
		decision = None
		if yeOrne.lower() == "ye":
			while self.running:
				decision = self.terminal()
				if decision == "1":
					nodename = raw_input("Please assign our new node a designation\n^>>")
					self.nm.addNodeNamed(nodename)## this works
					self.nm.printNodeNamed()# this works
				elif decision == "2":
					nodename = raw_input("Which node are you trying to find?\n^>>")
					node = self.nm.findNodeNamed(nodename)#add/modify find nodename function in MendicantBot
					print "We are", node.getName()
				elif decision == "3":
					nodename = raw_input("Which node do you wish to reallocate\n^>>")
					node = self.nm.reallocateNodeNamed(nodename)
				elif decision == "4":
					nodename = raw_input("Which node do you wish to kill?\n^>>")
					node = self.nm.killNodeNamed(nodename)
				elif decision == "5":
					nodename = raw_input("Which node do you want to check for rampancy?\n^>>")
					node = self.nm.rampantNodeCheck(nodename)
					self.rampant()
				elif decision == "6":#this works
					print "lulz I dont do anything"
				elif decision == "7":#this works
					self.quiter()# calls quit(self) function below
					self.running = False

		else:
			self.quiter()
			self.running = False

    #def isinitalized(self, decision):
	#	pass

	def quiter(self):# quite and prints message
		print self.quit

	def rampant(self):# prints error message if bot is not working right or "rampant"
		print self.rampant


	def terminal(self):
		terminal = True
		while terminal:
			print "<<TERMINAL>>"
			print "Welcome to our terminal biologicals. \n This terminal is for you to better communicate with us. \n How may we assist?"
			print "<1> Spawn a MendicantNode"
			print "<2> Find a running MendicantNode"
			print "<3> Reallocate a running MendicantNode"
			print "<4> Kill a MendicantNode/s"
			print "<5> Identify if a MendicantNode is rampant"
			print "<6> ???"
			print "<7> Quit and shutdown MendicantBot"
			decision = str(raw_input("^>> "))
			return decision