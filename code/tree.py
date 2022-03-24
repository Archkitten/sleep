def not_christmas_time():
  treeSize = int(input("Tree Size: "))
  for i in range(treeSize):
    for n in range(treeSize-i):
      print(" ", end="")
    for p in range(int(2*i)+1):
      print("^", end="")
    print()
  for i in range(int(treeSize/4)):
    for t in range(treeSize-int(treeSize/5)): 
      print(" ", end="")
    for t in range(int(treeSize/2)-1):
      print("*", end="")
    print()

# not_christmas_time()

