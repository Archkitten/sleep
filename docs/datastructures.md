## TPT 2

### Factor Finder Function:

```python
class FindFactors:
  def __init__(self):
    print("1", end=" ")
  def __call__(self, n):
    for val in range(2,n + 1):
      if n % val == 0:
        print(val, end=" ")
    print()

def factorfinder():
  print("Factor Finder")
  num = int(input("Enter any Number to Find its Factors: "))
  factors = FindFactors()
  factors(num)
```

### Factorial Function

```python
class Factorial:
  def __init__(self):
    pass
  def __call__(self, n):
    if n == 0 or n == 1:
      return 1
    else:
      return n * self(n - 1)

def factorial():
  fac = Factorial()
  print("Factorial")
  num = int(input("Enter Number to Find its Factorial: "))
  print(fac(num))
```
