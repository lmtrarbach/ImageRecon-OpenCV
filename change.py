import re
import sys, os
import urllib
images= open("pos.txt", "r+")
nova=open("pos2.txt", "r+")
for line in images.readlines():
	string = ('/pos/%s 1 0 0 100 40'  % (line))
	limpar =  string.replace('\n','')
	nova.write(limpar + '\n')
