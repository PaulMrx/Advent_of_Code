import hou

string = input("Enter puzzle input")

bucket = string.split("\n\n")
list = []

for n in bucket:
    food = n.split("\n")
    res = [eval(i) for i in food]
    list.append(sum(res))
    
    maxCalories = max(list)
    lastOnes = sum(sorted(list)[-3:])

print("result": maxCalories)
print("lastOnes": lastOnes)
