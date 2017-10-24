# No Libc For You
```
$ file nolibc4u
nolibc4u: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=10866629ff13bfa14e4578af076336ff96890d25, not stripped
```
## CHECKSEC
```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```
## RESULT
![screenshot](https://user-images.githubusercontent.com/16120472/31752845-cf979e80-b495-11e7-8d56-a6ff9f57de89.png)
