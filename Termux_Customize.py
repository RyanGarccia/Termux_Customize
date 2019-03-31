#!/usr/bin/env python2
# Informations ########################################
#
# -*- coding: utf-8 -*-
# Author: RyanGarccia
# YouTube: https://youtu.be/hzDb53dOH4w
#
# Groups ##############################################
#
# WhatsApp:
# Telegram:
#
# Import Modules ######################################
import os
from time import sleep
from core.banners.logo import *
from core.Menu_Banners import *
from core.Menu_Prompt import *
from core.Menu_Themes import *
from core.Menu_Help import *
import sys
#######################################################
C, E, W, D = '\033[36m', '\033[0m', '\033[1;37m', '\033[7m'
def Restart_Program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
try:
    banner()
    print ("\n\n Ferramenta simples para personalizar o App do Termux.")
    sleep(3)
    print (" ")
    os.system("clear")
    print (C+"""
 ______          __      ____       __  _
/_  __/__  ___  / /__   / __ \___  / /_(_)__  ___  ___
 / / / _ \/ _ \/ (_-<  / /_/ / _ \/ __/ / _ \/ _ \(_-<
/_/  \___/\___/_/___/__\____/ .__/\__/_/\___/_//_/___/
By: ₹₰₳₦ ₲₳₹₡₡₰₳™  /___/   /_/      Beta Version: 1.0

     {1}~{ Selecionar Banner
     {2}~{ Selecionar Prompt de Comando
     {3}~{ Selecionar Temas
     {4}~{ Help
     {5}~{ Exit

    """)
    options = input("M∆ST£R DRØID ~> : ")
    if options == "1":
        Choose_Banner()
    elif options == "2":
        Chooser_Prompt()
    elif options == "3":
        Info_Themes()
        Choose_Themes()
    elif options == "4":
        Help()
    elif options == "5":
        os.system("clear")
        print (C+"""
   ____                           __     __          __
  / __/__ ___   __ _____  __ __  / /__ _/ /____ ____/ /
 _\ \/ -_) -_) / // / _ \/ // / / / _ `/ __/ -_) __/_/
/___/\__/\__/  \_, /\___/\_,_/ /_/\_,_/\__/\__/_/ (_)
              /___/

 Até logo!
            """)
        exit(0)

    else:
        print (' Ops, o comando: "' + options + '" não foi encontrado!')
        print ("         Reiniciando o Script!")
        sleep(4)
        Restart_Program()

except KeyboardInterrupt:
    print ("\n\n          Programa interropido pelo usuário!")
    print ("                        CTRL+C")
    sleep(3)
    exit(0)
