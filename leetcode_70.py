def soln(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev_prev = 1  
    prev = 2  
    current = 0

    for i in range(3, n + 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current

stairs=5
print(soln(stairs))