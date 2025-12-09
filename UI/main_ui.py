from multiprocessing import set_start_method
from UI.menu_manager import MenuManager
from UI.team_captain_ui import TeamCaptainUI
from UI.user_ui import UserUI
from LL.api_ll import APILL
import os
import platform
import sys
import atexit

def clear_terminal():
    """Clears the terminal"""
    system_name = platform.system()
    if system_name == "Windows":
        os.system("cls")
    else:  # macOS or Linux
        os.system("clear")
    
        
GREEN_COLOR = "\033[92m" 
RED_COLOR = "\033[91m"
RESET_CODE = "\033[0m"

def set_system_color_red():
    """Changes system color to red"""
    sys.stdout.write(RED_COLOR)

def set_system_color_green():
    """Changes system color to green"""
    sys.stdout.write(GREEN_COLOR)

def reset_system_color():
    """Resets the system to default colors
        done when exiting the system"""
    sys.stdout.write(RESET_CODE)





#automatic reset at exit of system
atexit.register(reset_system_color)





def print_welcome_sign():
    """Welcome sign for the system"""
    return(r"""
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
""")

def print_logo():
    """Logo that stays up throughout the system"""
    return(r"""
░█▀▄░█▀▄░█▀█░█▀▀░█░█░█▀▀░█▀█░▀█▀░▀▀█░█▀▀░█▀▄
░█▀▄░█▀▄░█▀█░█░░░█▀▄░█▀▀░█░█░░█░░▄▀░░█▀▀░█▀▄
░▀▀░░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀                                   
""")

class MainUI:
    """Main ui functions are in here"""
    def __init__(self):
        self.APILL = APILL()
        self.menu_manager = MenuManager(self.APILL)
        self.previous_screen = ""
        self.current_screen = "LOGIN_MENU"

    def run(self) -> None:
        """Main loop handling navigation"""
        
        # 1. PRINT WELCOME SIGN ONCE (Before the loop starts)
        clear_terminal()
        set_system_color_green()
        print(print_welcome_sign()) 
        set_system_color_red()
        
        # Optional: Pause so the user can actually see the welcome sign
        input("\nPress Enter to start")

        while True:
            func = self.menu_manager.pages.get(self.current_screen)

            if func is None:
                print(f"Unknown screen: {self.current_screen}")
                break

            # 2. PRINT SMALL LOGO ALWAYS (Inside the loop)
            clear_terminal()
            set_system_color_green()
            print(print_logo()) 
            set_system_color_red()

            next_screen = func()

            if next_screen in (None, "QUIT"):
                break

            self.current_screen = next_screen
