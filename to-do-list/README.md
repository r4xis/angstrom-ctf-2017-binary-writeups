# TO DO LIST
```
$ file todo_list
todo_list: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=dec307bc68b2c89d41a984b11f9d2a5a7e94dbb3, not stripped
```
## CHECKSEC
```
gdb-peda$ checksec
CANARY    : ENABLED
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```
## ASLR
```
# cat /proc/sys/kernel/randomize_va_space
0
```
## CREATE USER
```
$ ./todo_list 
Welcome to Noah's ListKeeper Pro!
Keep your todo lists safely online and never worry about them again!
Access them from your computer, phone, tablet, game console, car dashboard, or smart fridge!

Let's start by getting you logged in
Enter username: user
Enter password: pass
Welcome, user! Here are the commands you can use: 
c - Create a new list
v - View the contents of a list
a - Add to an existing list
d - Delete a list
s - Show all the existing lists
p - Change the user's password
l - Login as a different user
h - Print this very menu
x - Exit the program

> x
```
## RESULT
