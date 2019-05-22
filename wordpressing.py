#Wordpress exploiting tool designed by DavideCube
#Works on Wordpress version <= 4.5.3 and the WooCommerce Plugin version
import BeautifulSoup
import re
import urllib

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
url = input("Please provide a wordpress url:")

print("The target is", url)

data = urllib.urlopen(url).read() #read the content of the webpage

#extract somehow the version tag

#soup = BeautifulSoup.BeautifulSoup(data)
#element = soup.find('meta', attrs={'name': 'generator', 'content': re.compile("^Wordpress.*")})
#print(element.text)