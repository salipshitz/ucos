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
The config file is very useful in UCOS if you want to change usernames, passwords, and a few other things
The unedited version of the file looks like this
```python
#config.py
global user_prompt
user_prompt = "$ "
global username
username = "root"
global password
password = "root"
```
