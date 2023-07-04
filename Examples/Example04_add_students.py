# Add Student to file

def main():
    print()
    name = input("What is the student's name? ").strip().title()
    age = input("How old is (s)he? ").strip()
    country = input("what is the student's country? ").strip().title()
    print()
    add_student(name, age, country)

def add_student(name, age, country):
    with open("Examples/Example04_students_list.csv", "a") as file:
        file.write(f"{name},{age},{country}\n")

while True:
    use = input("Do you want to add a student? ").strip().upper()
    if use == "Y":
        if __name__ == "__main__":
            main()
    else:
        break

