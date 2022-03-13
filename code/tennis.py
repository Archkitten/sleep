import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"

# print tennis racket and ball with colors and leading spaces
def tennis_print(position):
    print(ANSI_HOME_CURSOR)
    sp = " " * position
    print(cyan + "  ____")
    print(" /xxxx\ " + sp + green + "     ,-'''-. ")
    print(cyan + "|xxxxxx|" + sp + green + "    /" + white + "\     /" + green + "\ ")
    print(cyan + "|xxxxxx|" + sp + green +  "    | " + white + "|   |" + green + " | ")
    print(cyan + "\\xxxxxx/" + sp + green + "    \\" + white + "/     \\" + green + "/ ")
    print(cyan + " \\xxxx/" + sp + green + "      '-...-' ")  
    print(cyan + "  \\--/")
    print(cyan + "   ||")
    print(cyan + "   ||")
    print(cyan + "   ||")
    print(cyan + "   ||")
    print(cyan + "   []" + white)


# tennis function, iterface into this file
def tennis():
    # loop control variables
    start = 0  # start at zero
    distance = 45  # how many times to repeat
    step = 2  # count by 2

    for position in range(start, distance, step):
        tennis_print(position)  # call to function with parameter
        time.sleep(.1)

# call tennis
# tennis()