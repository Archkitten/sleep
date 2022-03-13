# HARDCODED SO WE NUKE THIS

# run = "(python3.10 --version || install-pkg python3.10) && clear && python3.10 code/menu2.py" 

import sys;print(sys.version) # checking for python3.10 (code fails without it)
import runpy
import os
import time
import color
import tennis

def rerun():
  os.system('clear')
  main()

def main():
  magenta = "\033[35m"
  white = "\033[37m"
  
  print("Welcome to Michael's sleep tracker!")
  
  sleep = """    
         .__                        
    _____|  |   ____   ____ ______  
   /  ___/  | _/ __ \_/ __ \\____ \ 
   \___ \|  |_\  ___/\  ___/|  |_> >
  /____  >____/\___  >\___  >   __/ 
       \/          \/     \/|__|    
  """
  
  print(magenta + sleep + white)
  
  print("Select which tool you want to use")
  
  menu = """
  1. Tracker
  2. Sleep Calculator
  3. Blah Blah Blah
  4. A Placeholder for an Incredible Program
  5. What.

Number: """
  
  select = int(input(menu))

  
  def selection(select):
    match select:
      case 1:
        print("Tracker")
        os.system('clear')
        tennis.tennis()
        # runpy.run_module(mod_name='tennis')
        # rerun()
      case 2:
        print("Sleep Calculator")
        color.test()
        # runpy.run_module(mod_name='color')
        # rerun()
      case 3:
        print("Blah^3")
      case 4:
        print("Placeholder")
      case 5:
        print("What")
      case _:
        print("Try Again...")
        time.sleep(1)
        rerun()
  
  selection(select)

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()