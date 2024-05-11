# CodeBy Золотая середина
from pwn import *

min_number = 0
max_number = 1000000000000000000000000

r = remote("62.173.140.174", 10200)

# бинарный поиск
while True:
    # Receive until the prompt to enter a number
    prompt = r.recvuntil("Введите число:".encode('utf-8')).decode('utf-8')
    print(prompt)  # Print the server's messages including attempts left

    # Calculate the average number
    avg_number = min_number + (max_number - min_number) // 2

    # Print the number being sent
    print(f"Sending number: {avg_number}")

    # Send the average number
    r.sendline(str(avg_number).encode('utf-8'))

    try:
        # Attempt to receive the message about whether the number is higher or lower
        result = r.recvuntil(("Загаданное число больше.".encode('utf-8'), "Загаданное число меньше.".encode('utf-8')), timeout=5).decode('utf-8')
        print(result)  # Print whether the guess was too high or too low

        if "Загаданное число больше." in result:
            min_number = avg_number  # Adjust the min_number up if the guess was too low
        else:
            max_number = avg_number  # Adjust the max_number down if the guess was too high

    except EOFError:
        print("Connection closed by the server.")
        break
    except TimeoutError:
        print("No response received from the server within the timeout period.")
        break

r.interactive()
