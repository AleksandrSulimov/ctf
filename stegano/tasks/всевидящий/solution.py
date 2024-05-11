# codeby Всевидящий
with open("task.html", mode="r") as file:
    lines = file.read().split(";&#")

ls = []
for x in lines:
    try:
        x = int(x)
        if x > 10000:
            ls.append(chr(x))
    except:
        continue

print(''.join(ls))




