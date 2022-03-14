import math
import numpy as np # math stuff
from scipy.integrate import quad # integration

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
  print("2 sample z-test for p1-p2")
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
  print("props:", round(p1, 4), round(p2, 4), round(pc, 4))
  print("SD:", round(sd, 4))
  print("z-score:", round(z,4))
  print("p result:", round(p, 4)) # testing purposes
  print("p-value:", round(pval,8))
  alpha(a,pval) 
  
  exit()

# two_propzt()

def one_propzt():
  print("1 sample z-test for p-hat")
  # parameters
  p0 = float(input("P0: "))
  x = int(input("Successes x: "))
  n = int(input("Pop. size n: "))
  print(hypoz)
  Ha = int(input("Alternate Hypothesis: "))
  a = float(input("Significance Level α: "))

  # proportion values
  p = float(x/n) # p hat 1

  # calculations
  sd = math.sqrt(p0*(1-p0)*(1/n))
  z = (p-p0)/sd # z-score

  result = quad(zform, -math.inf, z)[0]
  pval = ztpval(result,Ha)

  print("props:", p0, p)
  print("SD:", round(sd, 4))
  print("z-score:", round(z,4))
  print("p-value:", round(pval,8))
  alpha(a,pval)

  exit()

# one_propzt()