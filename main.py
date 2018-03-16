import os
import shutil
from os.path import isfile
from langdetect import detect
#print detect("My name is here") 

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

ist=os.listdir(".")
ensure_dir('English_Songs')

print "List of files moved: "
for v in ist:
	temp=v[-3:]
	if isfile(v) and temp=='mp3':
		res=detect(v)
		if res == 'en':
			print v
		 	shutil.move("./"+v, "./English_Songs/"+v)

