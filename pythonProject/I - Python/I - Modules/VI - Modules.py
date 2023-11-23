# MODULE = file containig python code. May contain functions, classes, etc.
#          used with modular programming, which is to separate a program into useful parts

import Modules_Messages

Modules_Messages.hello()
Modules_Messages.bye()

    # you can rename a module
import Modules_Messages as msg

msg.hello()
msg.bye()

    # you can import functins from modules directly
from Modules_Messages import hello, bye, introduce

hello()
bye()
introduce("kevin","math")

# imports all in a module
# from ModulesMessages import *


help("modules")

