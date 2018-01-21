#WARING THIS CODE IS UNSTABLE
import os
import random
os.system('cls')
os.system('title Goblin: The Turn Based RPG')
title = """
 A Turn Based RPG By Geremachek2:
 
  ▄████  ▒█████   ▄▄▄▄    ██▓     ██▓ ███▄    █ 
 ██▒ ▀█▒▒██▒  ██▒▓█████▄ ▓██▒    ▓██▒ ██ ▀█   █ 
▒██░▄▄▄░▒██░  ██▒▒██▒ ▄██▒██░    ▒██▒▓██  ▀█ ██▒
░▓█  ██▓▒██   ██░▒██░█▀  ▒██░    ░██░▓██▒  ▐▌██▒
░▒▓███▀▒░ ████▓▒░░▓█  ▀█▓░██████▒░██░▒██░   ▓██░
 ░▒   ▒ ░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ 
  ░   ░   ░ ▒ ▒░ ▒░▒   ░ ░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░
░ ░   ░ ░ ░ ░ ▒   ░    ░   ░ ░    ▒ ░   ░   ░ ░ 
      ░     ░ ░   ░          ░  ░ ░           ░ 
                       ░                        """
print(title.center(40, ' '))
print("")
print("Menu: Stats, Exit, Start, About")
opt = input(">")
if opt == "":
  print("")
elif opt == "exit":
  exit()
elif opt == "stats":
  print("-STATS-")
  print("fireball: 1,10 DMG")
  print("magicmissle: 10,50 DMG")
  print("doomportal: 10,100 DMG")
  input("")
elif opt == "start":
  print("")
elif opt == "about":
  print("Goblin is a turn based RPG created by Jonah 'Geremachek2' Rongstad created to test rgAI created by Jonah. rgAI was created using random.py to simulate an acutal goblin opponent. rgAI stands for 'Random Goblin Artifical Intellegence'")
  input("")
os.system('cls')
print("Your Hero's Health")
php = input("> ")
os.system('cls')
print("The Goblin's Health")
ehp = input("> ")
os.system('cls')
while 1 == 1:
   print("Attack Choice")
   attcc = input("> ")
   if attcc == "fireball":
      ehp = int(ehp) - int(random.randint(1,10))
      print("You Did DMG To The Goblin!")
      print("The Goblin's Current Heath: " + str(ehp))
   elif attcc == "magicmissle":
       ehp = int(ehp) - int(random.randint(10,50))
       print("You Did DMG To The Goblin!")
       print("The Goblin's Current Heath: " + str(ehp))
   elif attcc == "doomportal":
      ehp = int(ehp) - int(random.randint(10,100))
      print("You Did DMG To The Goblin!")
      print("The Goblin's Current Heath: " + str(ehp))
   else:
      print("Invalid Attack Name, Try magicmissle, fireball, and doomportal")
   a = int(random.randint(1,10))
   b = int(random.randint(10,100))
   php = int(php) - int(random.randint(a,b))
   print("")
   print("The Goblin Did DMG To You")
   input("Your Current Health: " + str(php))
   os.system('cls')
   while int(php) <= 0:
    input("-YOU DIED-")
    exit()
   while int(ehp) <= 0:
    input("-YOU WIN-")
    exit()
