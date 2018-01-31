![ucos](https://user-images.githubusercontent.com/22849169/35648625-2fec7bce-068b-11e8-9807-fc75f51ddb78.png | width = 100)
# UnicomOS
UnicomOS or UCOS is an open source bash like shell written in python by Geremachek2

# Before You Start...
Please install python on your computer fist before runing! Be sure it can be launched in the terminal!
Put all of these system files in its own folder, called USYS or just UCOS

# UCOS Boot Screen
```
Booting Into UnicomOS 12.0...
```
You can execute dev commands on this screen, check the /ucos.py source code or BOOTCMD.md to find out what you can do!

After this you will see a prompt that looks like this
```
Username: 
```
The default user name is 'root', if this doesn't work check what global username is equal to in the config file

Then after that you will see

```
Password: 
```
Type 'root' on this screen to log in!
# Prompt
You will see this prompt after logging in
```
$ 
```
Type ls, help, about, or any other command!
# Config File
The config file (ucos_config.py) is very useful in UCOS if you want to change usernames, passwords, and a few other things
The unedited version of the file looks like this
```python
global user_prompt
user_prompt = "$ "
global username
username = "root"
global password
password = "root"
```
You can change the password, username, and prompt character by changing what their equal to
# Tricks and easter eggs
if you use the print command like so
```
$ print ucos.py
```
you should get the entire UCOS source code printed in the terminal, pretty cool huh?

The 'python' application may just seem like a way to execute python code in UCOS, but you can also meddle with the source code it self!
try this commmand
```
$ python
>>> prompt = "The new Prompt!$ "
>>> exit
The new Prompt!$ 
```
If you want to do a quick calculation that doesn't require any scientific functions and you don't wan't to use the calculator program
use this command!
```
$ echov 9*54
486
$ 
```
