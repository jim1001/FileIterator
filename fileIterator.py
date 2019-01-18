#Ref: https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
import os

path = 'UsageLogs/In'

folder = os.fsencode(path)

filenames = []

for file in os.listdir(folder):
    filename = os.fsdecode(file)
    #if filename.endswith( ('.jpeg', '.png', '.gif') ): # whatever file types you're using...
    filenames.append(filename)

filenames.sort() #sorts in ascending order
for file in filenames:
    print(file + "\n")
