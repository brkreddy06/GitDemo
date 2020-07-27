# 'open'method is used to get the file (text, doc, excel etc)
# 'read' method is used to read the contents of file
# 'close' method must be used to close the open file, to avoid memory leaks
# read(5) - it will read n number of characters by passing parameter. if nothing is mentioned in the method it will read all the content
# readline() method - it will read single line at a time
# readlines() method - it will store all the content in the form of indexes like LIST

file = open('test.txt')
#Read all the contents of the file
#print(file.read())
#print(file.read(5))
#print(file.readline())  # if you don't comment 10 line the output is considers after 5th character ex: abcde & fgh, if u comment and execute then output is abcdefgh
#print(file.readline())

# interview question: print all the content line by line using readline method
#line = file.readline()
#while line != "":
#    print(line)
#    line = file.readline()

# another logic for printing the content line by line using 'for loop'
# readlines() stores all the values in LIST format [abcdefgh, bat, cat, ...., jain]
for line1 in file.readlines():
    print(line1)





file.close()