# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

blue = "\033[34m"
white = "\033[37m"

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Michael",  
               "LastName": "Chen",  
               "DOB": "December 1",  
               "Residence": "San Diego",  
               "Email": "michaelc57247@stu.powayusd.com",  
               "Owns_Cars":["2016 Ford Focus EV", "2019 Honda Pilot"]  
              })  

InfoDb.append({  
               "FirstName": "Ethan",  
               "LastName": "Vo",  
               "DOB": "Not Born",  
               "Residence": "The Moon",  
               "Email": "ethanv696969@stu.powayusd.com",  
               "Owns_Cars":["Broken Down Golf Cart"]  
              })  

InfoDb.append({  
               "FirstName": "Anirudh",  
               "LastName": "Ramachandran",  
               "DOB": "August 18",  
               "Residence": "Uranus",  
               "Email": "anirudhr42069@stu.powayusd.com",  
               "Owns_Cars":["Can't Even Drive"]  
              })  


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def for_loop():
    for x in range(len(InfoDb)):
        # print(InfoDb[x])
        print_data(x)

def while_loop(x):
    while x < len(InfoDb):
        # print(InfoDb[x])
        print_data(x)
        x += 1


def recursive_loop(x):
    if x < len(InfoDb):
        # print(InfoDb[x])
        print_data(x)
        recursive_loop(x + 1)

# hack 3: fibonnaci

def fibonacci(n):
    if n == 0:
      return 0 # for 0
    elif n == 1:
      return 1 # for 1
    else: 
      return fibonacci(n-1) + fibonacci(n-2) # recursion

def tester2():
    try:
      num = int(input("Term of Fibonacci Sequence: ")) # user input
      # check if the number is negative
      if num < 0:
          print("You tested negative for COVID-19! Unfortunately, we only accept postive values at this Wendy's") # negative input
      else:
          print(num, "terms of the Fibonacci Sequence:")
          for i in range(num):
            print(fibonacci(i)) # list 0-n
    except:
      print("INTEGER INTEGER INTEGER WHAT ARE YOU EVEN DOING") # non-integer input

# tester2()

def tester():
    print(blue + "For loop" + white)
    for_loop()
    print(blue + "While loop" + white)
    while_loop(0)  # requires initial index to start while
    print(blue + "Recursive loop" + white)
    recursive_loop(0)  # requires initial index to start recursion
    # tester2()
    exit()
    # hack3()

# tester()