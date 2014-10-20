gis_file = open('/Users/Heather/Documents/501/lab3/GISisBest/GIS_is_the_best.txt', 'r')
file_list = gis_file.read()

new_file = open('GIS_2.txt', 'w+')

for word in file_list.split(' '):
        if word ==  'Science':
                word = 'Systems'
                new_file.write(word + ' ')
        elif word == 'science':
                word = 'systems'
                new_file.write(word + ' ')
        elif word == 'GIScience':
                word = 'GISystem'
                new_file.write(word + ' ')
        else:
                new_file.write(word + ' ')
