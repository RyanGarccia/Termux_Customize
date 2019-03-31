from sys import argv, executable
from os import system, execl, getcwd
from time import sleep
C = '\033[36m'
E = '\033[0m'
ThemeDir = '/data/data/com.termux/files/home/Termux_Customize/core/themes/'
Home_Dir = '/data/data/com.termux/files/home/Termux_Customize/Termux_Customize.py'
def Restart_Menu_Themes():
        python = executable
        execl(python, python, * argv)
        curdir = getcwd()

def Return_Themes():
    system("python $HOME/Termux_Customize/Termux_Customize.py")

def Info_Themes():
    system("rm -rf /sdcard/Prints_of_Themes")
    system("cp -r Prints_of_Themes /sdcard")
    system("clear")
    print (C+"""



            # # # # # # # # # # # # # # # #
            # Os prints dos temas foram   #
            # adicionados à sua galeria   #
            # de fotos, Cofira cada tema! #
            # # # # # # # # # # # # # # # #
    """)
    sleep(5)

def Choose_Themes():
    system("clear")
    print (C+"""
    ____    __        __   ________
   / __/__ / /__ ____/ /_ /_  __/ /  ___ __ _  ___ ___
  _\ \/ -_) / -_) __/ __/  / / / _ \/ -_)  ' \/ -_|_-<
 /___/\__/_/\__/\__/\__/__/_/ /_//_/\__/_/_/_/\__/___/
 By: ₹₰₳₦ ₲₳₹₡₡₰₳     /___/         Beta Version: 1.0

     {01}~{ Black_Night
     {02}~{ Default_Theme
     {03}~{ Gruvbox_Black
     {04}~{ Isotope_Dark
     {05}~{ MyTheme
     {06}~{ Rydgel
     {07}~{ Shapeshifter_Dark
     {08}~{ Solarized_Black
     {09}~{ Solarized_Dark
     {10}~{ Summerfruit
     {00}~{ Back to main menu

    """)

    options = input("M∆ST£R DRØID ~> : ")
    if options == "1" or options == "01":
        system("clear")
        print ("     Você deseja definir 'Black_Night' como tema?")
        print ("                          [Y]/[N]")
        print (" ")
        Theme = input("M∆ST£R DRØID ~> : ")
        if Theme == "y" or Theme == "Y":
            system("cd $HOME && rm -rf .termux")
            system("cd $HOME && mkdir .termux")
            print (" ")
            system("cd " + ThemeDir + "Black_Night && cp -r * $HOME/.termux")
            print ("       Reinicie o Termux para aplicar o tema!")
        else:
            system("clear")
            print (" Tudo bem!, vamos tentar outros temas!")
            sleep(3)
            Restart_Menu_Themes()

    elif options == "2" or options == "02":
        system("clear")
        print ("     Você deseja definir 'Default_Theme' como tema?")
        print ("                          [Y]/[N]")
        print (" ")
        Theme = input("M∆ST£R DRØID ~> : ")
        if Theme == "y" or Theme == "Y":
            system("cd $HOME && rm -rf .termux")
            system("cd $HOME && mkdir .termux")
            system("cd " + ThemeDir + "Default_Theme && cp -r * $HOME/.termux")
            print (" ")
            print ("       Reinicie o Termux para aplicar o tema!")
        else:
            system("clear")
            print (" Tudo bem!, vamos tentar outros temas!")
            sleep(3)
            Restart_Menu_Themes()
    elif options == "3" or options == "03":
        system("clear")
        print ("     Você deseja definir 'Gruvbox_Black' como tema?")
        print ("                          [Y]/[N]")
        print (" ")
        Theme = input("M∆ST£R DRØID ~> : ")
        if Theme == "y" or Theme == "Y":
            system("cd $HOME && rm -rf .termux")
            system("cd $HOME && mkdir .termux")
            system("cd " + ThemeDir + "Gruvbox_Black && cp -r * $HOME/.termux")
            print (" ")
            print ("       Reinicie o Termux para aplicar o tema!")
        else:
            system("clear")
            print (" Tudo bem!, vamos tentar outros temas!")
            sleep(3)
            Restart_Menu_Themes()
    elif options == "4" or options == "04":
        system("clear")
        print ("     Você deseja definir 'Isotope_Dark' como tema?")
        print ("                          [Y]/[N]")
        print (" ")
        Theme = input("M∆ST£R DRØID ~> : ")
        if Theme == "y" or Theme == "Y":
            system("cd $HOME && rm -rf .termux")
            system("cd $HOME && mkdir .termux")
            system("cd " + ThemeDir + "Isotope_Dark && cp -r * $HOME/.termux")
            print (" ")
            print ("       Reinicie o Termux para aplicar o tema!")
        else:
            system("clear")
            print (" Tudo bem!, vamos tentar outros temas!")
            sleep(3)
            Restart_Menu_Themes()
    elif options == "5" or options == "05":
        system("clear")
        print ("     Você deseja definir 'MyTheme' como tema?")
        print ("                      [Y]/[N]")
        print (" ")
        Theme = input("M∆ST£R DRØID ~> : ")
        if Theme == "y" or Theme == "Y":
            system("cd $HOME && rm -rf .termux")
            system("cd $HOME && mkdir .termux")
            system("cd " + ThemeDir + "MyTheme && cp -r * $HOME/.termux")
            print (" ")
            print ("       Reinicie o Termux para aplicar o tema!")
        else:
            system("clear")
            print (" Tudo bem!, vamos tentar outros temas!")
            sleep(3)
            Restart_Menu_Themes()
    elif options == "6" or options == "06":
        system("clear")
        print ("     Você deseja definir 'Rydgel' como tema?")
        print ("                      [Y]/[N]")
        print (" ")
        Theme = input("M∆ST£R DRØID ~> : ")
        if Theme == "y" or Theme == "Y":
            system("cd $HOME && rm -rf .termux")
            system("cd $HOME && mkdir .termux")
            system("cd " + ThemeDir + "Rydgel && cp -r * $HOME/.termux")
            print (" ")
            print ("       Reinicie o Termux para aplicar o tema!")
        else:
            system("clear")
            print (" Tudo bem!, vamos tentar outros temas!")
            sleep(3)
            Restart_Menu_Themes()
    elif options == "7" or options == "07":
        system("clear")
        print ("   Você deseja definir 'Shapeshifter_Dark' como tema?")
        print ("                         [Y]/[N]")
        print (" ")
        Theme = input("M∆ST£R DRØID ~> : ")
        if Theme == "y" or Theme == "Y":
            system("cd $HOME && rm -rf .termux")
            system("cd $HOME && mkdir .termux")
            system("cd " + ThemeDir + "Shapeshifter_Dark && cp -r * $HOME/.termux")
            print (" ")
            print ("       Reinicie o Termux para aplicar o tema!")
        else:
            system("clear")
            print (" Tudo bem!, vamos tentar outros temas!")
            sleep(3)
            Restart_Menu_Themes()
    elif options == "8" or options == "08":
        system("clear")
        print ("   Você deseja definir 'Solarized_Black' como tema?")
        print ("                          [Y]/[N]")
        print (" ")
        Theme = input("M∆ST£R DRØID ~> : ")
        if Theme == "y" or Theme == "Y":
            system("cd $HOME && rm -rf .termux")
            system("cd $HOME && mkdir .termux")
            system("cd " + ThemeDir + "Solarized_Black && cp -r * $HOME/.termux")
            print (" ")
            print ("       Reinicie o Termux para aplicar o tema!")
        else:
            system("clear")
            print (" Tudo bem!, vamos tentar outros temas!")
            sleep(3)
            Restart_Menu_Themes()
    elif options == "9" or options == "09":
        system("clear")
        print ("   Você deseja definir 'Solarized_Dark' como tema?")
        print ("                          [Y]/[N]")
        print (" ")
        Theme = input("M∆ST£R DRØID ~> : ")
        if Theme == "y" or Theme == "Y":
            system("cd $HOME && rm -rf .termux")
            system("cd $HOME && mkdir .termux")
            system("cd " + ThemeDir + "Solarized_Dark && cp -r * $HOME/.termux")
            print (" ")
            print ("       Reinicie o Termux para aplicar o tema!")
        else:
            system("clear")
            print (" Tudo bem!, vamos tentar outros temas!")
            sleep(3)
            Restart_Menu_Themes()
    elif options == "10":
        system("clear")
        print ("   Você deseja definir 'Summerfruit' como tema?")
        print ("                         [Y]/[N]")
        print (" ")
        Theme = input("M∆ST£R DRØID ~> : ")
        if Theme == "y" or Theme == "Y":
            system("cd $HOME && rm -rf .termux")
            system("cd $HOME && mkdir .termux")
            system("cd " + ThemeDir + "Summerfruit && cp -r * $HOME/.termux")
            print (" ")
            print ("       Reinicie o Termux para aplicar o tema!")
        else:
            system("clear")
            print (" Tudo bem!, vamos tentar outros temas!")
            sleep(3)
            Restart_Menu_Themes()
    elif options == "00":
        system("python "+ Home_Dir)
    else:
        system("clear")
        print ("    Ops, parece que algo deu errado!!!")
        print (' O comando: "' + options + '" não foi encontrado... :(')
        sleep(3)
        Restart_Menu_Themes()
