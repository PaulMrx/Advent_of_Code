# Look up for students

# def main():
#     print()
dict = []


def read_file():
    with open("Examples/Example04_students_list.csv") as file:
        for line in sorted(file):
            name, age, country = line.rstrip().split(",")
            row = {"name":name, "age":age, "country":country}
            dict.append(row)

def get_name(student):
    return student["name"]

def get_age(student):
    return student["age"]

def get_country(student):
    return student["country"]

read_file()



for student in sorted(dict, key=get_name, reverse=True):
    print(f"{student['name']} is {student['age']} and comes from {student['country']}")