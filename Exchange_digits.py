def Exchange_digits(num1, num2):
    digits = list(str(num1))
    smallest_greater = [float('inf')]

    def backtrack(path, used):
        if len(path) == len(digits):
            current_number = int(''.join(path))
            if current_number > num2:
                smallest_greater[0] = min(smallest_greater[0], current_number)
            return

        for i in range(len(digits)):
            if not used[i]:
                used[i] = True
                path.append(digits[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

    backtrack([], [False] * len(digits))

    if smallest_greater[0] != float('inf'):
        return smallest_greater[0]
    else: 
        return -1

result = Exchange_digits(459,500)
print(result)
