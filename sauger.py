import urllib
site = urllib.urlopen('http://www.netzmafia.de/software/wordlists/deutsch.txt')
site = site.read()
file1 = open('wordlisteDeutsch.txt','w')
f1 = file1.write(site)
file1.close()
