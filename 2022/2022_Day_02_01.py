import string
import sys

# Enter multilines puzzle input and strip unnecessary spaces
print("Enter puzzle input:")
inputlist = sys.stdin.readlines()
inputstring = ' '.join(inputlist).strip()

# Separate input by game
game = inputstring.split("\n ")
list = []

for n in game:
    if n=="A Y" or n=="B Z" or n=="C X":
        res = 6
    elif n=="A X" or n=="B Y" or n=="C Z":
        res = 3
    else:
        res = 0
    play = n.split(" ")
    if play[1]=="X":
        input = 1
    elif play[1]=="Y":
        input = 2;
    elif play[1]=="Z":
        input = 3
    list.append(res+input)

result = sum(list)

print("result: " , result)