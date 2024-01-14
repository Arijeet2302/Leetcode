
def Uniquedigits(l,r):
	count = 0
	for num in range (l, r + 1):
		visited = [0,0,0,0,0,0,0,0,0,0]
		flag = 0
		while num:
			if visited[num % 10] == 1:
				flag =1
				break
			visited[num % 10] = 1
			num //= 10
		
		if flag == 0:
			count +=1
	return count


#set approach

def Uniquedigits_sets(l,r):
	count = 0
	for num in range(l,r+1):
		num_str = str(num)
		num_set = set(num_str)
		if len(num_set) == len(num_str):
			count+=1
	return count

print(Uniquedigits(10, 15))
print(Uniquedigits_sets(10, 15))