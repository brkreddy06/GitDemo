# with - command takes care of open & close methods.
# w - indicates write the file
# r - indicates read the file
# if you don't put w or r python will consider r by default
# reversed() - it will reverse the items present in the file
# write() - it will write the file

#read the file and store all the values in list
#reverse the list
#write the list back to the file

with open('test.txt', 'r') as reader: # reader is an object
    content = reader.readlines()  # created the variable(content) and it holds the list of all the items present in the file. ex: [abcdefgh, bat, cat, ...., jain]
    reversed(content)       #[jain,...., cat, bat, abcdefgh]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)