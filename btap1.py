arr = []
for num in range(1000, 3001):
    is_even = True
    for digit in str(num):
        if int(digit) % 2 != 0:
            is_even = False
            break
    if is_even:
        arr.append(str(num))
print(",".join(arr))