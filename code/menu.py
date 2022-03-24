# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders

# module imports
import os

# file imports
import fib, swap, matrix, tree, tennis, color, stats
import tpt.tpt1

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
stats_sub_menu = [
    ["2 Prop Z-Test", stats.two_propzt],
    ["1 Prop Z-Test", stats.one_propzt]
]

pattern_sub_menu = [
    ["Tennis", tennis.tennis],
    ["Christmas Tree", tree.not_christmas_time],
]

math_sub_menu = [
    ["Matrices", matrix.in_the_matrix],
    ["TPT 1 - Fibo", tpt.tpt1.tester2]
]

data_sub_menu = [
    ["Swap", swap.swap],  
    ["TPT 1 - InfoDB", tpt.tpt1.tester]
]

random_sub_menu = [
    ["Color", color.test],
    ["Fibonacci", fib.fibonacci],
]


# Menu banner is typically defined by menu owner
magenta = "\033[35m"
white = "\033[37m"
border = "=" * 34
sleep = """    
       .__                        
  _____|  |   ____   ____ ______  
 /  ___/  | _/ __ \_/ __ \\____ \ 
 \___ \|  |_\  ___/\  ___/|  |_> >
/____  >____/\___  >\___  >   __/ 
     \/          \/     \/|__|    
"""
banner = f"\n{border}\nPlease Select An Option zZ\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = magenta + sleep + white + banner
    menu_list = main_menu.copy()
    menu_list.append(["Statistics", stats_submenu])
    menu_list.append(["Pattern", pattern_submenu])
    menu_list.append(["Math", math_submenu])
    menu_list.append(["Data", data_submenu])
    menu_list.append(["Random", random_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def stats_submenu():
    title = "Statistics Submenu" + banner
    buildMenu(title, stats_sub_menu)

def pattern_submenu():
    title = "Pattern submenu" + banner
    buildMenu(title, pattern_sub_menu)

def math_submenu():
    title = "Math submenu" + banner
    buildMenu(title, math_sub_menu)

def data_submenu():
    title = "Data submenu" + banner
    buildMenu(title, data_sub_menu)

def random_submenu():
    title = "Random Function Submenu" + banner
    buildMenu(title, random_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '-', value[0])

    # get user choice
    choice = input("Type your choice: ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            try:
              os.system('clear')
            except:
              os.system('cls')
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again

if __name__ == "__main__":
    menu()