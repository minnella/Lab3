#must open a text file assigning a class of gis_file
gis_file = open('/Users/Heather/Documents/501/lab3/GISisBest/GIS_is_the_best.txt', 'rU')

# new function to read gis_file
file_string = gis_file.read()

#assign variables so the computer knows they exist
system_count = 0
science_count = 0
total_words = 0

# In order for python to read through the file you have to essentially create a list this code creates a list of words and iterates through them.
#word is an arbitrary term for the variable
#split is the opposite of join it is used as a separator to split the input string into elements
for word in file_string.split(' '):

        #we have to make sure the words are all similar case, in this instance lower case
        #checks if the word is either systems or science
        if word.lower() == 'systems':
                system_count = system_count + 1
        elif word.lower() == 'science':
                science_count = science_count +1
        total_words = total_words + 1

def print_count (word, count):
	print "Number of times "+ word +" occurs = " + str(count)  
print "total words = " + str(total_words)
#print "Number of times systems occurs = " + str(system_count)
print_count("science", science_count)
print_count("systems", system_count)
