# No Libc For You
This writeup for 32 bit linux(Original binary for 64 bit linux).

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
