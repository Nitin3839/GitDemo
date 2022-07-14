#read all the content of file
file = open("text.txt")
#read n number of charecter by passing parameter
#print(file.read(5))
#print(file.read(12))

#read one single line at a time readline()
#print(file.readline())
line = file.readline()
while line != "":
    print(line)
    line = file.readline()

    readlin
file.close()