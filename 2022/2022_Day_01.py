import string
import sys

# Enter multilines puzzle input
print("Enter puzzle input:")
inputlist = sys.stdin.readlines()
inputstring = ' '.join(inputlist).strip()

# Separate input by groups (buckets)
bucket = inputstring.split("\n \n")

# Compute max calories for each bucket and append to list
list = []
for n in bucket:
    food = n.split("\n ")
    res = [eval(i) for i in food]
    list.append(sum(res))
    
    maxCalories = max(list)
# Compute sum of the 3 most caloric buckets
    lastOnes = sum(sorted(list)[-3:])

print("result: " , maxCalories)
print("lastOnes: " , lastOnes)
