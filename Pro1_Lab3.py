## For this problem we had to do three things to a folder of files 
#1 convert the files to .txt
#2 change the file names to be all lower case
#3 add to the beginning of each filename file_


#First we must import the os module as we will be manipulating the file path
import os, sys
path = "C:/Users/Heather/Documents/501/lab3/GISisBest/text_files"

for filename in os.listdir(path): #this opens up the directory and puts all of the files into it in a list, which I can now iterate through
	oldname=filename
	#1 file ext to .txt
	#we define dotchar by telling python to look for the "." character in the filename
	dotchar=filename.find(".")
	# we then tell python we only want to keep the filename up to dotchar. this takes care of the extensions
	filename=filename[:dotchar]
	#when then add on to the filename the new extension we want
	filename=filename+".txt"

	#2 everything is lower case
	#we use the lower function to redefine filename
	filename=filename.lower()

	#3name file starting file_
	#concatonate file_ to filename
	filename="file_"+filename
	
	#print filename
	os.rename(oldname, filename) #(source or actual file directory, new name for the file directory)
