import sys

# Enter multilines puzzle input
print("Enter puzzle input:")
inputlist = sys.stdin.readlines()
inputstring = ' '.join(inputlist).strip()


rucksac = inputstring.split("\n ")

comp1 = []
comp2 = []

res = {}

list = []
numbers = []


for n in rucksac:
    compartment1 = n[:len(n)//2]
    comp1.append(compartment1)
    compartment2 = n[len(n)//2:]
    comp2.append(compartment2)

for key in comp1:
    for value in comp2:
        res[key] = value
        comp2.remove(value)
        break

for key,value in res.items():
    common_chars = "".join(set(key).intersection(value))
    list.append(common_chars)

    for char in list:
        if char.islower():
            num = ord(char) - 96
        else:
            num = ord(char) - 38
    numbers.append(num)

result = sum(numbers)

print("result: " , result)