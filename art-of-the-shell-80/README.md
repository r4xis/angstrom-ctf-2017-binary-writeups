# Art of the shell
```
$ file art_of_the_shell
art_of_the_shell: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8b200dd7064035990b36ab643a57321a344d1736, not stripped
```
## CHECKSEC
```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : disabled
PIE       : disabled
RELRO     : Partial
```

## RESULT
![screenshot](https://user-images.githubusercontent.com/16120472/31752021-70949fc2-b491-11e7-98f2-d6ab9f1c9796.png)

