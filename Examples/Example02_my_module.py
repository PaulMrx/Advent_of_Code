import sys

def main():
    print("Hello world!")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

# That way main() will run only if specifically called in another file
# "__name__" will always be "name" -- it has nothing to do with the variable I chose in the functions above !
if __name__=="__main__":
    main()