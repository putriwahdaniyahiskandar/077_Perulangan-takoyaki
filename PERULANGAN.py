n = int(input("Send angka : "))
x = 0
while (x < n):
    if (10 ** x < n):
        a = x
    else:
        break
    x += 1

print("Angka terkecil dari 10^x < n ialah ", 10 ** a)
