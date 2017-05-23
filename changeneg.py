import re
import sys, os
import urllib
images= open("neg.txt", "r+")
nova=open("bg.txt", "r+")
for line in images.readlines():
	string = ('/neg/%s'  % (line))
	limpar =  string.replace('\n','')
	nova.write(limpar + '\n')
