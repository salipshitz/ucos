#Imports
import math
import os
from datetime import datetime
import random
import ucos_config
#Title of Terminal Window
os.system("title UCOS")
#Manual Logs
def man(name):
  if name == "date":
    print("Displays Date")
  elif name == "time":
    print("Displays Time")
  elif name == "micro":
    print("A text simple text editor that can work with the commands print, run, runvbs, and runpy")
  elif name == "calc":
    print("A Simple calculator with some scientific functions")
  elif name == "print":
    print("Prints the contence of text files")
  elif name == "rand":
    print("A random number between 1 and 100")
  elif name == "randui":
    print("Generates a number between numbers chosen by the user")
  elif name == "win":
    print("Opens a new instance of UCOS in a GUI window")
  elif name == "cmd":
    print("Execute commands to the parent teminal")
  elif name == "ping":
    print("Pings a IP or URL of the user's choice")
  elif name == "trace":
    print("Traceroutes a IP or URL of the user's choice")
  elif name == "goblin":
    print("Runs the game Goblin")
  elif name == "python":
    print("Execute python code")
  elif name == "echo":
    print('Prints the text after "echo"')
  elif name == "echov":
    print("Evaluates the exspression following echov")
  elif name == "print":
    print("Prints text files")
  elif name == "rmv":
    print("Deletes Filles")
#Calculator app function 
def root(number6):
  print(math.sqrt(number6))
def fact(number5):
  print(math.factorial(number5))
def circ(number4):
  solu4 = number4 * int(math.pi)
  print(solu4)
def power(number3, power):
  solu3 = number3 ** power
  print(solu3)
def square(number2):
  solu2 = number2 ** 2
  print(solu2)
def cube(number):
  solu = number ** 3
  print(solu)
  (number, solu)
def calc():
  c = input("> ")
  print(eval(c))
  if c == "cube":
    m1 = input("cbu> ")
    cube(int(m1))
  elif c == "square":
    m2 = input("sqr> ")
    square(int(m2))
  elif c == "power":
    m3 = input("numb> ")
    m3a = input("pow> ")
    power(int(m3), int(m3a))
  elif c == "circ":
    m4 = input("circ> ")
    circ(int(m4))
  elif c == "fact":
    factui = input("fact> ")
    fact(int(factui))
  elif c == "root":
    rootui = input("root> ")
    root(int(rootui))
#OS Start
os.system('cls')
dev_input = input("Booting Into UCOS v12.0... ")
prompt = ucos_config.user_prompt
if dev_input == "sharktank":
  print("Username: " + str(ucos_config.username))
  print("Password: " + str(ucos_config.password))
  input("")
elif dev_input == "hex":
  os.system('color 1f')
elif dev_input == "neo":
  os.system('color 0a')
elif dev_input == "prompt":
  prompt = input('Prompt: ')
os.system('cls')
uname = input("Username: ")
if uname != ucos_config.username:
  print("Invalid Username") 
else:
  pword = input("Password: ")
  if pword != ucos_config.password:
    print("Invalid Password")
  else:
    os.system('cls')
    while 1 == 1:
      ui = input(prompt)
      #List Command
      if ui == "ls":
        path = os.getcwd()
        files = os.listdir(path)
        list_files = '  '.join(files)
        print(list_files)
        print("""
date
time
micro (editor)
calc
echo[v]
rand[ui]
win
cmd
run[py,vbs]
print
ping
trace
goblin
python 
""")  #date command
      elif ui == "date":
        print(str(datetime.now().month) + "/" + str(datetime.now().day) + "/" + str(datetime.now().year))
        if str(datetime.now().month) + "/" + str(datetime.now().day) + "/" + str(datetime.now().year) == "12/25/" + str(datetime.now().year):
          print("Merry Christmas!")
      #time command
      elif ui == "time":
        print(str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second))
      #micro program
      elif ui == "micro":
          ln_numb = 0
          os.system('cls')
          fileName = input("File Name... ")
          os.system('cls')
          print("--------------" + fileName + "--------------")
          print("")
          f = open(fileName, 'w')
          while ln_numb >= 0:
            ln_numb += 1
            f.write("""
""")
            edit_ui = input(str(ln_numb) + "  ")
            if edit_ui == ":q":
              f.close()
              break
              os.system('cls')
            f.write(edit_ui)
      #clear command_1
      elif ui == "cls":
        os.system('cls')
      #clear command_2
      elif ui == "clear":
        os.system('cls')
      #dev command
      elif ui == "dev_info":
        print("Commands with arguments are now supported")
        print("micro added")
      #random command
      elif ui == "rand":
        print(random.randint(1,100))
      #exit command
      elif ui == "exit":
        print("Log Off Time: " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second))
        exit()
      #shutdown command
      elif ui == "shutdown":
        print("UCOS Will Now Shutdown Yor Computer: (Y/N)")
        sui = input(">")
        if sui == "y":
          os.system('shutdown -s')
        elif sui == "n":
          print("Shutdown Cancelled")
      #random program
      elif ui == "randui":
        rui = input("> ")
        rui1 = input("> ")
        print(random.randint(int(rui),int(rui1)))
      #GUI window program
      elif ui == "win":
        os.system('cls')
        os.system('start python ucos.py')
      #No input function
      elif ui == "":
        continue
      #python shell program
      elif ui == "python":
        while 1 == 1:
          py = input(">>> ")
          exec(py)
          if py == "exit":
            break
      #user program
      elif ui == "a":
        print("No Alpha Program, Go To Line 205 To Add Your Own UCOS Program")
      #calc program
      elif ui == "calc":
        calc()
      #command interpreter
      elif ui == "cmd":
        while 1 == 1:
          cmdui = input("> ")
          os.system(cmdui)
          if cmdui == "exit":
            break
      #ping program
      elif ui == "ping":
        ip = input("IP Or URL... ")
        os.system('ping ' + str(ip))
      #goblin program
      elif ui == "goblin":
        print("This Program Is In Very Early Development, Please Do Not Be To Harsh When You Incounter An Error")
        input("Press Enter To Continue... ")
        os.system("cls")
        os.system('python game.py')
        os.system('title UnicomOS')
      #trace command
      elif ui == "trace":
        trc = input("IP Or URL... ")
        os.system('tracert ' + str(trc))
      #Man logs
      elif ui == "man date":
        man("date")
      elif ui == "man time":
        man("time")
      elif ui == "man micro":
        man("edit")
      elif ui == "man calc":
        man("calc")
      elif ui == "man echo":
        man("echo")
      elif ui == "man rand":
        man("rand")
      elif ui == "man randui":
        man("randui")
      elif ui == "man win":
        man("win")
      elif ui == "man cmd":
        man("cmd")
      elif ui == "man run":
        man("run")
      elif ui == "man ping":
        man("ping")
      elif ui == "man trace":
        man("trace")
      elif ui == "man goblin":
        man("goblin")
      elif ui == "man python":
        man("python")
      elif ui == "man echoe":
        man("print")
      elif ui == "man echov":
        man("echov")
      elif ui == "man print":
        man("print")
      elif ui == "man rmv":
        man("rmv")
      #Help listing
      elif ui == "help":
        print("""
Type 'ls' to list commands and file names
type cls or clear to clear screen
          """)
      elif ui == "about":
        print('''
UnicomOS or UCOS is an open source, easaly hackable OS, written in python. Feel free to modify the source code via the python app included in UCOS or by directly modifing the source code. You can add your own program written in python, java C++ or anything else! Have Fun!''')
      elif ui + '.ucmd' in os.listdir(os.getcwd()):
        uipy = open(ui + '.ucmd', 'r')
        exec(uipy.read())
        uipy.close()
      #echo fixes
      elif int(len(ui)) < 3:
        print("Syntax Error, '" + str(ui) + "' is not valid")
      elif int(len(ui)) < 7:
        print("Syntax Error, '" + str(ui) + "' is not valid")
      #rmv command
      elif ui[0] + ui[1] + ui[2] + ui[3] == 'rmv ':
        rmvlen = len(ui)
        os.system('del ' + str(ui[4:int(rmvlen)]))
      #print command
      elif str(ui[0] + ui[1] + ui[2] + ui[3] + ui[4] + ui[5]) == "print ":
        prntlen = len(ui)
        pf = open(ui[6:int(prntlen)], 'r')
        print(pf.read())
        pf.close()
      #runvbs command
      elif str(ui[0] + ui[1] + ui[2] + ui[3] + ui[4] + ui[5] + ui[6]) == "runvbs ":
        vbslen = len(ui)
        os.system(ui[7:int(vbslen)])
      #runpy command
      elif str(ui[0] + ui[1] + ui[2] + ui[3] + ui[4] + ui[5]) == "runpy ":
        pylen = len(ui)
        pyf = open(ui[6:int(pylen)], 'r')
        exec(pyf.read())
        pyf.close()
      #echo command
      elif str(ui[0] + ui[1] + ui[2] + ui[3] + ui[4]) == "echo ":
        wlen = len(ui)
        print(ui[5:int(wlen)])
      #echov command
      elif str(ui[0] + ui[1] + ui[2] + ui[3] + ui[4] + ui[5]) == "echov ":
        elen = len(ui)
        print(eval(ui[6:int(elen)]))
      else:
        print("Syntax Error, '" + str(ui) + "' is not valid")
