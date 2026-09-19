##
# This program tests the Menu class.
#
"""import importlib
import menu
importlib.reload(menu)"""
from menu import Menu
mainMenu = Menu()

# Add more options
mainMenu.addOption("Open new account")
mainMenu.addOption("Log into existing account")
mainMenu.addOption("Help")
mainMenu.addOption("Quit")

choice = mainMenu.getInput()
print("Input:", choice)