'''
This is a color program that will only run in an IDE
'''

from colorama import Fore, Back, Style

print(Fore.RED + 'Hello World!')
print(Back.GREEN + 'My name is Kevin')
print(Style.DIM + 'This is ICS 200-3')
print(Style.RESET_ALL)
print('back to normal now')
print('\033[2;31;43m I - Python IDE for this is Pycharm')
