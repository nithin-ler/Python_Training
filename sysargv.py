# *args -variable no of arguments
# **kwargs-key value pair
 
#  sys.argv is a list that contains command-line arguments passed to a Python script.
 
import sys
import math
tot=0
k=len(sys.argv)
print("Size  =" , k)
print(sys.argv[1])
max = 0
min = math.inf
for i in range(2,k):
    tmp = int(sys.argv[i])
    if tmp>max:
        max = tmp
    if tmp<min:
        min = tmp

    tot=tot+ int(sys.argv[i])
 
print("Total  =" , tot)
print("Min =",min)
print("Max =",max)