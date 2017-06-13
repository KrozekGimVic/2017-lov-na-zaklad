def load(i, N):
    # Ta funkcija izrise lepse nalaganje
    if i % (N//1000) == 0:
        print("{:3.1f}% [{}{}]".format(i/(N//100), "#"*(i//(N//100)),
              " "*(100-(i//(N//100)))), end="\r")


num = int(input("Vnesi stevilo: "))

print("Prvi korak")
# for i in range(10**8+1):
#     load(i, 10**8)


print("\nDrugi korak")
for i in range(10**8+1):
    num += 1
    load(i, 10**8)

print("\nTretji korak")
for i in range(10**7+1):
    num *= 2
    num %= 1000000007
    load(i, 10**7)


print("\nResitev je:")
print(num)
