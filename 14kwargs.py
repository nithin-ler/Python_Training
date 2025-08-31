# 14. Write a function that accepts **kwargs and returns the sum of values.
import sys

print(f"{sys.argv}")

sumarg = sum(int(x) for x in sys.argv[1:len(sys.argv)])
print("Sum of args =",sumarg)
