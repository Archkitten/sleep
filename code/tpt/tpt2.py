# Function to find the Factors of a Number
def findFactors(number):
    print("Factors of a Given Number {0} are:".format(number))
    for value in range(1, number + 1):
        if number % value == 0:
            print("{0}".format(value), end=" ")
    print()

def factors():
    print("hello from factors")
    num = int(input("Enter any Number to find its factors: "))
    findFactors(num)

class Factorial:
  def __init__():
    return 1
  def __call__(self, n):
    return n * self(n - 1)

fac = Factorial()

print(fac(5))

