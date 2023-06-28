import string
import sys

# Enter multilines puzzle input
print("Enter puzzle input:")
inputlist = sys.stdin.readlines()
inputstring = ' '.join(inputlist).strip()

game = inputstring.split("\n ")
list = []

A = X = 1
B = Y = 2
C = Z = 3

draw = {"A": "X", "B": "Y", "C": "Z"}
win = {"A": "Y", "B": "Z", "C": "X"}
lose = {"A": "Z", "B": "X", "C": "Y"}

for n in game:

    play = n.split(" ")
    if play[1]=="X":
        input = eval(lose[play[0]])
    elif play[1]=="Y":
        input = 3 + eval(draw[play[0]])
    elif play[1]=="Z":
        input = 6 + eval(win[play[0]])
    list.append(input)

result = sum(list)

print("result: " , result)