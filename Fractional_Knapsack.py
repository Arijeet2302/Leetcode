n = int(input("Enter no of objs: "))
Knapsack_weight  = int(input("Enter knapsack weight: "))
value = list(map(int,input("Enter values: ").split()))
weight = list(map(int,input("Enter weights: ").split()))

ratio = [(value[i]/weight[i],value[i],weight[i]) for i in range(n)]

ratio.sort( key = lambda x: x[0], reverse=True)

profit = 0

for element in ratio:
    if element[2] <= Knapsack_weight and Knapsack_weight > 0:
        profit += element[1]
        Knapsack_weight -= element[2]
    
    elif  Knapsack_weight > 0  and element[2] > Knapsack_weight:
        profit += element[1]* ( Knapsack_weight / element[2])
        Knapsack_weight = 0
    else : 
        break

print(profit)