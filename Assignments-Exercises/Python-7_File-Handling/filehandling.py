
# read sample.txt file
with open('sample.txt', 'r') as file:
    contents = file.read()
    print("Contents of the sample.txt file:")
    print(contents)
    file.close()

# open('sample.txt', 'r')
# contents = open('sample.txt', 'r').read()
# print("Contents of the file:")
# print(contents)
print("\n")
# write to a new file
with open('newfile.txt', 'w') as lego:
    lego.write("This is a new file with new content.\n")

# read the new file
with open('newfile.txt', 'r') as car:
    newcontent = car.read()
    print("Contents of newfile.txt: ")
    print(newcontent)

#  append to new file
with open('newfile.txt', 'a') as file:
    newline = file.write("This is a new line appended to new file.\n")

# read the appended new file
with open('newfile.txt', 'r') as file:
    appfile = file.read()
    print("New content of newfile.txt: ")
    print(appfile)
    file.close