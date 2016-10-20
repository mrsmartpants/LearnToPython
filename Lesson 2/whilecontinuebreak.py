i = 1

while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue
    if i == 15:
        # breaks the while loop
        break

    print("odd value : ", i)

    i += 1
