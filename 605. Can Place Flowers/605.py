flowerbed = list(map(int, input().split()))
n = int(input())
for i in range(len(flowerbed)):
    if flowerbed[i] == 0:
        if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -= 1
    if n <= 0:
        break
if n <= 0:
    print("Yes")
else:
    print("No")
