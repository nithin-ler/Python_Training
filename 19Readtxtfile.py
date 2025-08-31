# 19. Write a program to count the number of words in a text file.
f = open("somefile.txt",'w')
f.write("Yes! This is a sample file\n")
f.write("The purpose of this file is to be used as a test file\n")
f.write("Checking count of words in this file....\n")
f.close()

f = open("somefile.txt",'r')
count =0
for i in f:
    count=count + len(i.split())
print("Count of words:",count)
f.close()
