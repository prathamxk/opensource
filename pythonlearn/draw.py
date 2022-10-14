# draw.py
# The first time a module is loaded into a running Python script, 
# it is initialized by executing the code in the module once. If another module in your code imports the same module again, 
# it will not be loaded again, so local variables inside the module act as a "singleton," meaning they are initialized only once.

def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...
def clear_screen(screen):
    ...
class Screen():
    ...

# initialize main_screen as as singleton
main_screen = Screen()