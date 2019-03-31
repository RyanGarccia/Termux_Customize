from os import system
from time import sleep
C = '\033[36m'
E = '\033[0m'
def Return_Banner():
    system("python $HOME/Termux_Customize/Termux_Customize.py")

def Choose_Banner():
    system("clear")
    print (C+"""
   ____    __        __     ___
  / __/__ / /__ ____/ /_   / _ )___ ____  ___  ___ ____
 _\ \/ -_) / -_) __/ __/  / _  / _ `/ _ \/ _ \/ -_) __/
/___/\__/_/\__/\__/\__/__/____/\_,_/_//_/_//_/\__/_/
By: ₹₰₳₦ ₲₳₹₡₡₰₳™    /___/        Beta Version: 1.0


     {01}~{ BackTrack Linux
     {02}~{ Json
     {03}~{ Gárgula
     {04}~{ Pônei 01
     {05}~{ Pônei 02
     {06}~{ Abóbora de Halloween
     {07}~{ Error 404
     {00}~{ Back to main menu

    """)
    Menu = input("M∆ST£R DRØID ~> : ")
    if Menu == "01" or Menu == "1":
        system("python $HOME/Termux_Customize/core/banners/BackTrack_Linux/BackTrack_Linux.py")
        sleep(3)
        print ("  Você deseja definir 'BackTrack Linux' como Tema?")
        print ("                       [Y]~[N]")
        option = input("M∆ST£R DRØID ~> : ")
        if option == "Y" or option == "y":
            system('rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc')
            system('cd $HOME/Termux_Customize/core/banners/BackTrack_Linux && cp -r bash.bashrc /data/data/com.termux/files/usr/etc ')
            print (" Tudo Ok!")
            sleep(3)
            Return_Banner()
        else:
            print ("Ops! o comando: '" + option + "' não foi encontrado!.")
            sleep(3)
            Return_Banner()
    elif Menu == "02" or Menu == "2":
        system("cat $HOME/Termux_Customize/core/banners/Json/Json.hwtxt")
        sleep(3)
        print ("  Você deseja definir 'Json' como Tema?")
        print ("                 [Y]~[N]")
        option = input("M∆ST£R DRØID ~> : ")
        if option == "Y" or option == "y":
            system('rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc')
            system('cd $HOME/Termux_Customize/core/banners/Json && cp -r bash.bashrc /data/data/com.termux/files/usr/etc/')
            print (" Tudo Ok!")
            sleep(3)
            Return_Banner()
        else:
            print ("Ops! o comando: '" + option + "' não foi encontrado!.")
            sleep(3)
            Return_Banner()
    elif Menu == "03" or Menu == "3":
        system("cat $HOME/Termux_Customize/core/banners/Gárgola/Gárgola.hwtxt")
        sleep(3)
        print ("  Você deseja definir 'Gárgola' como Tema?")
        print ("                  [Y]~[N]")
        option = input("M∆ST£R DRØID ~> : ")
        if option == "Y" or option == "y":
            system('rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc')
            system('cd $HOME/Termux_Customize/core/banners/Gárgola && cp -r bash.bashrc /data/data/com.termux/files/usr/etc/')
            print (" Tudo Ok!")
            sleep(3)
            Return_Banner()
        else:
            print ("Ops! o comando: '" + option + "' não foi encontrado!.")
            sleep(3)
            Return_Banner()
    elif Menu == "04" or Menu == "4":
        system("cat $HOME/Termux_Customize/core/banners/Pônei1/Pônei1.aftxt")
        sleep(3)
        print ("  Você deseja definir 'Pônei1' como Tema?")
        print ("                  [Y]~[N]")
        option = input("M∆ST£R DRØID ~> : ")
        if option == "Y" or option == "y":
            system('rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc')
            system('cd $HOME/Termux_Customize/core/banners/Pônei1 && cp -r bash.bashrc /data/data/com.termux/files/usr/etc/')
            print (" Tudo Ok!")
            sleep(3)
            Return_Banner()
        else:
            print ("Ops! o comando: '" + option + "' não foi encontrado!.")
            sleep(3)
            Return_Banner()
    elif Menu == "05" or Menu == "5":
        system("cat $HOME/Termux_Customize/core/banners/Pônei2/Pônei2.aftxt")
        sleep(3)
        print ("  Você deseja definir 'Pônei2' como Tema?")
        print ("                  [Y]~[N]")
        option = input("M∆ST£R DRØID ~> : ")
        if option == "Y" or option == "y":
            system('rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc')
            system('cd $HOME/Termux_Customize/core/banners/Pônei2 && cp -r bash.bashrc /data/data/com.termux/files/usr/etc/')
            print (" Tudo Ok!")
            sleep(3)
            Return_Banner()
        else:
            print ("Ops! o comando: '" + option + "' não foi encontrado!.")
            sleep(3)
            Return_Banner()
    elif Menu == "06" or Menu == "6":
        system("cat $HOME/Termux_Customize/core/banners/Abóbora/Abóbora.hwtxt")
        sleep(3)
        print ("  Você deseja definir 'Abóbora' como Tema?")
        print ("                  [Y]~[N]")
        option = input("M∆ST£R DRØID ~> : ")
        if option == "Y" or option == "y":
            system('rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc')
            system('cd $HOME/Termux_Customize/core/banners/Abóbora && cp -r bash.bashrc /data/data/com.termux/files/usr/etc/')
            print (" Tudo Ok!")
            sleep(3)
            Return_Banner()
        else:
            print ("Ops! o comando: '" + option + "' não foi encontrado!.")
            sleep(3)
            Return_Banner()
    elif Menu == "07" or Menu == "7":
        system("cat $HOME/Termux_Customize/core/banners/404/404.txt")
        sleep(3)
        print ("  Você deseja definir 'Error 404' como Tema?")
        print ("                  [Y]~[N]")
        option = input("M∆ST£R DRØID ~> : ")
        if option == "Y" or option == "y":
            system('rm -rf /data/data/com.termux/files/usr/etc/bash.bashrc')
            system('cd $HOME/Termux_Customize/core/banners/404 && cp -r bash.bashrc /data/data/com.termux/files/usr/etc/')
            print (" Tudo Ok!")
            sleep(3)
            Return_Banner()
        else:
            print ("Ops! o comando: '" + option + "' não foi encontrado!.")
            sleep(3)
            Return_Banner()
    elif Menu == "00":
            Return_Banner()
    else:
        print ("Ops! o comando: '" + Menu + "' não foi encontrado!.")
        sleep(3)
        Return_Banner()
