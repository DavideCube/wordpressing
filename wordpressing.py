#Wordpress exploiting tool designed by DavideCube
#Works on Wordpress version <= 4.5.3 and the WooCommerce Plugin version
from bs4 import BeautifulSoup
import re
import urllib.request
from modules import Exploit


#create the exploit list, to be used later
my_list = []

my_list.append(Exploit.Exploit('dos', 'Simple DoS Attack', 1)) #only on WordPress 4.5.3
my_list.append(Exploit.Exploit('xss', 'XSS attack', 1)) #only on WordPress 4.5.3
my_list.append(Exploit.Exploit('xss+dos', 'XSS with Dos', 1)) #only on WordPress 4.5.3
my_list.append(Exploit.Exploit('rce', 'WooCommerce RCE', 1)) #only on WooCommerce .... 

#print main menu
print("\n")
print("******************************************************************")
print("*                                                                *")
print("*         Welcome to the Wordpressing Exploiting Tool!!          *")
print("*                                                                *")
print("******************************************************************")
print("*         The tool will check if the available exploits          *")
print("*         are applicable to the wordpress site you provide.      *")
print("******************************************************************")
print("\n")
url = input("Please provide a complete wordpress url: ")

print("The target is", url)

data = urllib.request.urlopen(url).read() #read the content of the webpage

soup = BeautifulSoup(data, 'html.parser') #parse the html code

#Check if the Wordpress version is the correct one
element = soup.find('meta', attrs={'name':'generator','content':'WordPress 4.5.3'})

if element is None:
	print("The target site is not based on Wordpress 4.5.3")
	my_list[0].executable = 0
	my_list[1].executable = 0
	my_list[2].executable = 0

#now check if we can execute the Woocommerce RCE
element =  soup.find('meta', attrs={'name':'generator','content':'WooCommerce 3.0.0'})

if element is None:
	print("The target site does not have WooCommerce 3.0.0")
	my_list[3].executable = 0

for i in range(len(my_list)): 
	if my_list[i].executable == 1:
		print( (i+1), ") ", my_list[i].desc)

print("here is your checkmark: " + u'\u2713');