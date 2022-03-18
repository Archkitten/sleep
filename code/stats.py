import math
import numpy as np # math stuff
from scipy.integrate import quad # integration
import os

# colors

red = "\033[31m"
green = "\033[32m"
white = "\033[37m"

# HELP: https://www.dropbox.com/s/br7yrtpgmeup4j5/Inference%20Procedure%20Summary.pdf?dl=0 

hypoz = """1 - p1 > p2
2 - p1 ≠ p2
3 - p1 < p2"""

def zform(x):
    pi = math.pi
    integrand = (1/(math.sqrt(2*pi)))*math.exp((-pow(x,2))/2) # https://github.com/mGalarnyk/Python_Tutorials/blob/master/Statistics/standard_normal_table/standard_normal_table.ipynb
    return(integrand)

def ztpval(p,Ha):
  if ((p > 0.5) or (p < 0.5)) and (Ha == 1):
    return 1 - p # 1 tailed p1 > p2
  elif ((p > 0.5) and (Ha == 2)):
    return 2*(1 - p) # 2 tailed
  elif ((p > 0.5) or (p < 0.5)) and (Ha == 3):
    return p
  elif ((p < 0.5) and (Ha == 2)):
    return 2*p # 2 tailed

def alpha(a,pval):
  if (pval < a):
    print(green + "reject H0" + white)
  else:
    print(red + "fail to reject H0" + white)

def two_propzt():
  # getting statistical values
  test = "2 sample z-test for difference in proportions"
  print(test)
  x1 = int(input("Successes x1: "))
  x2 = int(input("Successes x2: "))
  n1 = int(input("Pop. size n1: ")) 
  n2 = int(input("Pop. size n2: "))

  print(hypoz)
  Ha = int(input("Alternate Hypothesis: "))
  a = float(input("Significance Level α: "))

  # proportion values
  p1 = float(x1/n1) # p hat 1
  p2 = float(x2/n2) # p hat 2
  pc = (x1+x2)/(n1+n2) # combined proportion  

  # calculations
  pd = p1-p2 # difference in proportions
  sd = math.sqrt(pc*(1-pc)*((1/n1)+(1/n2))) # standard deviation
  z = pd/sd # z-score
  
  p = quad(zform, -math.inf, z)[0] # prelimary p-val calculation from formula (ref. zform())

  pval = ztpval(p,Ha)
  
  # just testing
  os.system('clear')
  print(test)
  print("props:", round(p1, 4), round(p2, 4), round(pc, 4))
  print("SD:", round(sd, 4))
  print("z-score:", round(z,4))
  # print("p result:", round(p, 4)) # testing purposes
  print("alpha value:", a)
  print("p-value:", round(pval,8))
  alpha(a,pval) 
  
  exit()

# two_propzt()

def one_propzt():
  test = "1 sample z-test for proportion p"
  # parameters
  print(test)
  p0 = float(input("P0: "))
  x = int(input("Successes x: "))
  n = int(input("Pop. size n: "))
  print(hypoz)
  Ha = int(input("Alternate Hypothesis: "))
  a = float(input("Significance Level α: "))

  # proportion values
  p = float(x/n) # p hat

  # calculations
  sd = math.sqrt(p0*(1-p0)*(1/n))
  z = (p-p0)/sd # z-score

  result = quad(zform, -math.inf, z)[0]
  pval = ztpval(result,Ha)

  os.system('clear')
  print(test)
  print("props:", p0, p)
  print("SD:", round(sd, 4))
  print("z-score:", round(z,4))
  print("p-value:", round(pval,8))
  alpha(a,pval)

  exit()

# one_propzt()

# def ttest():
#   test = "1 sample t-test for µ"
#   print(test)
#   # parameter values
#   m = int(input("µ: "))
#   n = int(input("n: "))

#   # calculations
#   sd = # whatever this is
#   t = # the formula

#   pval = # formula #2

#   os.system('clear')
#   print(test)
#   print("mean:", m)
#   print("population size:", n)
#   print("SD:", round(sd, 4))
#   print("t:", round(t, 4))
#   print("p-value:", round(pval, 4))
  