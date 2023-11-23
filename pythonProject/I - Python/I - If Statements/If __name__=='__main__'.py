# if __name__ == '__main__'
# -> allows you to run the module as a standalone program
# -> allows you to import module and be used by other modules

print(__name__)                     # returns '__main__'

if __name__ == '__main__':
    print("Running this module directly.")
else:
    print("Running other module indirectly.")

def hello():
    print("Hello!")

if __name__ == '__main__':
    hello()