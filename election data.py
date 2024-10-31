'''
name: Jack Pauley
discription: mid way through creating a code that makes a pie chart off of 
log: 10/31/24
bugs: doesnt print inot the cvs file and doesnt create the graph
features: None
sources:my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

# Sort by value in ascending order
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict)
google response 
https://stackoverflow.com/questions/37289951/how-to-write-to-a-csv-line-by-line
'''
import csv

#opens the kamala text file and counts the number of words and lines



fhand = open('kamala_new.txt')# opens the kamala speach text file 
counts = dict()# creates a dictionary call counts

#if the word is in the list continue if it is not add it to the list and add 1 to the count
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        if word in ['the', 'and', 'of', 'to','I','our','a','in','for','is']:
            continue
        elif word not in counts:
            counts[word] =1
        else:
            counts[word] += 1
#sorted_dict = counts[words]
sorted_dict = dict(sorted(counts.items(), key=lambda x:x[1], reverse = True))# dorts the dictionary using the counts list
print(sorted_dict) #prints the sorted dictionary 


# Specify the CSV file name



##text=List of strings to be written to file
with open('kamala_output.csv','w') as file:
        for key, value in sorted_dict.items():
            if value >= 10: 
                file.writelines(key + "," + str(value) + "\n")

