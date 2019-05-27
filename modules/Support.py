#exploit class used to set up the exploit list
class Exploit:
	def __init__(self,name,description, executable=1):
		self.id = name
		self.desc = description
		self.executable = executable



##################################################
#				function definition				 #
##################################################

#check if the inserted input is a valid number
def is_valid_number(var):
	if (not(var.isdigit()) or int(var) > 4 or int(var) <= 0):
		return False
	else:
		return True

#check if there is at least one possible exploit
def exploits_possible(list):
	for x in list:
  		if x.executable == 1:
  			return True
  		return False
