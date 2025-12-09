import os
import platform
import sys
import atexit


def clear_terminal():
    system_name = platform.system()
    if system_name == "Windows":
        os.system("cls")
    else:  # macOS or Linux
        os.system("clear")


GREEN_COLOR = "\033[92m"
RED_COLOR = "\033[91m"
RESET_CODE = "\033[0m"


def set_system_color_red():
    sys.stdout.write(RED_COLOR)


def set_system_color_green():
    # switch to Green
    sys.stdout.write(GREEN_COLOR)


def reset_system_color():
    # reset to default colors
    sys.stdout.write(RESET_CODE)


#    automatically back to regular color when program exits (even if it crashes)
atexit.register(reset_system_color)


def print_welcome_sign():
    # No clear_terminal() here, we handle it in the loop/logic
    return r"""
     __       __  ________  __        ______    ______   __       __  ________        ________   ______                      
    |  \  _  |  \|        \|  \      /      \  /      \ |  \     /  \|        \      |        \ /      \                     
    | $$ / \ | $$| $$$$$$$$| $$     |  $$$$$$\|  $$$$$$\| $$\   /  $$| $$$$$$$$       \$$$$$$$$|  $$$$$$\                    
    | $$/  $\| $$| $$__    | $$     | $$   \$$| $$  | $$| $$$\ /  $$$| $$__             | $$   | $$  | $$                    
    | $$  $$$\ $$| $$  \   | $$     | $$      | $$  | $$| $$$$\  $$$$| $$  \            | $$   | $$  | $$                    
    | $$ $$\$$\$$| $$$$$   | $$     | $$   __ | $$  | $$| $$\$$ $$ $$| $$$$$            | $$   | $$  | $$                    
    | $$$$  \$$$$| $$_____ | $$_____| $$__/  \| $$__/ $$| $$ \$$$| $$| $$_____          | $$   | $$__/ $$                    
    | $$$    \$$$| $$     \| $$     \\$$    $$ \$$    $$| $$  \$ | $$| $$     \         | $$    \$$    $$                    
     \$$      \$$ \$$$$$$$$ \$$$$$$$$ \$$$$$$   \$$$$$$  \$$      \$$ \$$$$$$$$          \$$     \$$$$$$                     
     _______                                __                            __                               
    |       \                              |  \                          |  \                              
    | $$$$$$$\  ______   ______    _______ | $$   __   ______   _______   \$$ ________   ______    ______  
    | $$__/ $$ /      \ |      \  /       \| $$  /  \ /      \ |       \ |  \|        \ /      \  /      \ 
    | $$    $$|  $$$$$$\ \$$$$$$\|  $$$$$$$| $$_/  $$|  $$$$$$\| $$$$$$$\| $$ \$$$$$$$$|  $$$$$$\|  $$$$$$\
    | $$$$$$$\| $$   \$$/      $$| $$      | $$   $$ | $$    $$| $$  | $$| $$  /    $$ | $$    $$| $$   \$$
    | $$__/ $$| $$     |  $$$$$$$| $$_____ | $$$$$$\ | $$$$$$$$| $$  | $$| $$ /  $$$$_ | $$$$$$$$| $$      
    | $$    $$| $$      \$$    $$ \$$     \| $$  \$$\ \$$     \| $$  | $$| $$|  $$    \ \$$     \| $$      
     \$$$$$$$  \$$       \$$$$$$$  \$$$$$$$ \$$   \$$  \$$$$$$$ \$$   \$$ \$$ \$$$$$$$$  \$$$$$$$ \$$ 
"""


def print_logo():
    # Use the smaller ASCII art here
    return r"""
░█▀▄░█▀▄░█▀█░█▀▀░█░█░█▀▀░█▀█░▀█▀░▀▀█░█▀▀░█▀▄
░█▀▄░█▀▄░█▀█░█░░░█▀▄░█▀▀░█░█░░█░░▄▀░░█▀▀░█▀▄
░▀▀░░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀                                   
"""


def refresh_logo():
    clear_terminal()
    set_system_color_green()
    print(print_logo())
    set_system_color_red()
