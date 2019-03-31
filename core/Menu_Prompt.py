from sys import argv, executable
from os import system, execl, getcwd
from time import sleep
C = '\033[36m'

def Restart_Menu_PS1():
    python = executable
    execl(python, python, * argv)
    curdir = getcwd()

def Back_To_Main_Menu():
    system("python /data/data/com.termux/files/home/Termux_Customize/Termux_Customize.py")

def Chooser_Prompt():
    system("clear")
    print (C+"""
       _______                        ___  _______
      / ___/ /  ___  ___  ___ ___    / _ \/ __<  /
     / /__/ _ \/ _ \/ _ \(_-</ -_)  / ___/\ \ / /
     \___/_//_/\___/\___/___/\__/__/_/  /___//_/
     By: ₹₰₳₦ ₲₳₹₡₡₰₳™        /___/ Verion: 1.0

     {1}~{ Selecionar Prompt de comando

     {2}~{ Back to main menu

    """)
    PS1 = input("M∆ST£R DRØID ~> : ")
    if PS1 == "1":
        system("sh /data/data/com.termux/files/home/Termux_Customize/core/.MyPS1.sh")
        print (" Tudo pronto!")
        Restart_Menu_PS1()
    elif PS1 == "2":
        Back_To_Main_Menu()
    else:
        print (' O comando: "' + PS1 + '" não foi encontrado!')
        sleep(4)
        Restart_Menu_PS1()

