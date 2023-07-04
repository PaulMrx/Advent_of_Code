

# # Open file with "append" function, write the input name, close the file
# file = open("Example03_names.text", "a")
# file.write(f"{name} \n")
# file.close()

# Same but in a better / shorter way
# with open("Example03_names.text", "a") as file:
#     file.write(f"{name} \n")



# Now proper test

def write_names():
    with open("Examples/Example03_names.text", "a") as file:
        file.write(f"{name} \n")

def read_names():
    with open("Examples/Example03_names.text", "r") as files:
        for file in files:
            print(f"My name is {file} \n")


while True:
    name = input("What's your name?").strip().title()
    if name != "Done":
        write_names()
    else:
        read_names()
        break           