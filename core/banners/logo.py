# Import Modules
from time import sleep
from sys import stdout, exit
from os import system
# End.
#
# Def colors
CYAN, END = '\033[36m', '\033[0m'
def banner():
    print ("\033[H\033[J")
    print (CYAN+'''
          ______           __  _
         / __/ /____ _____/ /_(_)__  ___ _
        _\ \/ __/ _ `/ __/ __/ / _ \/ _ `/ _ _
       /___/\__/\_,_/_/  \__/_/_//_/\_, (_|_|_)
       By: ₹₰₳₦ ₲₳₹₡₡₰₳™           /___/ v1.0
    ''')
    for i in range(101):
        sleep(0.03)
        stdout.write("\r  {0}[{1}°_°{0}]{1} Configurando recursos necessários... {0}[{1}%d%%{0}]{1}".format(CYAN, END) % i)
        stdout.flush()
