def MagicSquare(n):
    row = 0
    col = n // 2
    arr = [[0 for _ in range(n)] for _ in range(n)]

    for num in range(1, n*n+1):
        arr[row][col] = num
        row -= 1
        col += 1

        if row == -1 and col == n : #corner logic
            row += 2
            col -= 1
        elif col == n : #col folding
            col = 0 
        elif row == -1 : #row folding
            row = n - 1
        elif arr[row][col] != 0 : #pre-occupied logic
            row += 2
            col -= 1
    
    return arr

while True :
    n = int(input("Enter the size of the magic square : "))
    if n%2 == 1 :
        break

res = MagicSquare(n)

magicSum = 0

for i in range(len(res)):
    for j in range(len(res)):
        if i==j :
            magicSum += res[i][j]
        print(res[i][j], end=" ")
    print()

print("Magic Sum for",n, "is :",magicSum)

# magicSum(n) = n * ((n*n + 1) // 2)