
import string

string = "bvwbjplbgvbhsrlpgdmjqwftvncz"

list1 = []
final = []
for count, letter in enumerate(string):
    list1 += [string[0+count:14+count]]

#print(list1)
for i in list1:
    test = set(list(i))
    if len(test) is not 14:
        res = 1
    else:
        res = 0
    final.append(res)
print(final)
#
print(final.index(0)+14)