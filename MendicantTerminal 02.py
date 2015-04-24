from MendicantBot03 import NodeManager
### creating user terminal will have to modify mendicantbot 0.2 and add functions 
class UserControl(object):
	def __init__(self):
		MendicantBot = MendicantBot()
		MendicantBot.running = True
		MendicantBot.quit = "Killing Us and all processes"
		MendicantBot.rampant = "SsSomething ii/s wwww-rog witg is, attttttempting o reair rampant nnnnodes \n ...logic plague found"
		pass

	def initalize(self):
		yeOrne = str(raw_input("Start terminal if you wish biologicals [ye or ne]").lower())
		decision = None
		if yeOrne == "ye":
			while MendicantBot.running:
				decision = self.terminal()
				if decision == "1":
					nodename = raw_input("Please assign our new node a designation\n^>>")
					MendicantBot.addNodeNamed(nodename)## add this function to add node to node list
					MendicantBot.listnodename# add this function def listnodename(): to print the node name I just gave it
				elif decision == "2":
					nodename = raw_input("Which node are you trying to find?\n^>>")
					node = MendicantBot.findNodeNamed(nodename)#add/modify find nodename function in MendicantBot
					print "We are", node
				elif decision == "3":
					nodename = raw_input("Which node do you wish to reallocate\n^>>")
					node = MendicantBot.reallocateNodeNamed(nodename)
				elif decision == "4":
					nodename = raw_input("Which node do you wish to kill?\n^>>")
					node = MendicantBot.killNodeNamed(nodename)
				elif decision == "5":
					nodename = raw_input("Which node do you want to check for rampancy?\n^>>")
					node = MendicantBot.rampantNodeCheck(nodename)
					self.rampant()
				elif decision == "6":
					print "lulz I dont do anything"
				elif decision == "7":
					self.quit()# calls quit(self) function below
					MendicantBot.running = False

		else:
			self.quit()
			MendicantBot.running = False

			

	def isinitalized(self, choice):
		pass

	def quit(self):# quite and prints message
		print MendicantBot.quit

	def rampant(self):# prints error message if bot is not working right or "rampant"
		print MendicantBot.rampant


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