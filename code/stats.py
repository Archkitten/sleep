import math
import numpy as np # math stuff
from scipy.integrate import quad # integration

# colors

red = "\033[31m"
green = "\033[32m"
white = "\033[37m"

# HELP: https://www.dropbox.com/s/br7yrtpgmeup4j5/Inference%20Procedure%20Summary.pdf?dl=0 

def two_propzt():
  # getting statistical values
  print("2 sample z-test for p1-p2")
  x1 = int(input("Successes x1: "))
  x2 = int(input("Successes x2 "))
  n1 = int(input("Pop. size n1: ")) 
  n2 = int(input("Pop. size n2: "))

  # proportion values
  p1 = float(x1/n1) # p hat 1
  p2 = float(x2/n2) # p hat 2
  pc = (x1+x2)/(n1+n2) # combined proportion  

  # calculations
  pd = p1-p2 # difference in proportions
  sd = math.sqrt(pc*(1-pc)*((1/n1)+(1/n2))) # standard deviation
  z = pd/sd # z-score
  def zform(x):
    pi = math.pi
    integrand = (1/(math.sqrt(2*pi)))*math.exp((-pow(x,2))/2) # https://github.com/mGalarnyk/Python_Tutorials/blob/master/Statistics/standard_normal_table/standard_normal_table.ipynb
    return(integrand)

  result = quad(zform, -math.inf, z) 
  pval = 2*(1 - result[0]) # 2 tailed test
  
  # just testing
  print("props:", round(p1, 4), round(p2, 4), round(pc, 4))
  print("SD:", round(sd, 4))
  print("z-score:", round(z,4))
  print("p-value:", round(pval, 4))

  if (pval < 0.05):
    print(green + "reject H0" + white)
  else:
    print(red + "fail to reject H0" + white)
  
  exit()