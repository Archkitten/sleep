# fibonacci fun

def fibonacci():
    x = int(input("Term of Fibonacci Sequence: ")) # user input
    y = 0 # loop variable
    comp1 = 0 # first component
    comp2 = 1 # second component
    if x < 0:
        print("Postive Values Only");
    elif x == int("0"):
        print("0")
    elif x == int("1"):
        print("1")
    else:
        while y < x-1:
            total1 = comp1 + comp2 # total
            comp1 = comp2 # re-arrange variables
            comp2 = total1 # ''
            y += 1 # for the loop
        print(total1)