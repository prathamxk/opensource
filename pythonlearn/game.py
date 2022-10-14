# In programming, a module is a piece of software that has a specific functionality. 
# For example, when building a ping pong game, one module may be responsible for the game logic,
#  and another module draws the game on the screen.
# Modules in Python are just Python files with a .py extension. The name of the module is the same as the file name. 
# Modules are imported from other modules using the import command.

# game.py
# import the draw module
# import single object from module

# there are a couple of ways to tell the Python interpreter where to look for modules, aside from the default local directory
# and built-in modules. You can use environment variable PYTHONPATH to specify path of custom modules.
# PYTHONPATH=/game python game.py
# or another way is using sys.path.append function.
# sys.path.append("/game")

from draw import draw_game

def play_game():
    ...

def main():
    result = play_game()
    draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

# import all objects from module
# from draw import *


# custom import name
# Modules may be loaded under any name you want, this is useful when importing a module conditionally to use the same name in the rest of the code.

# Built in modules, two important modules dir, help and urllib 
import urllib

# use it
urllib.urlopen(...)

# We can look for which functions are implemented in each module by using the dir function:
dir(urllib)
# When we find the function in the module we want to use, 
# we can read more about it with the help function, using the Python interpreter:
help(urllib.urlopen)
