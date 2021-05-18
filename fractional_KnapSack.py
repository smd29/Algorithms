def frac_knapSack(profits,weights, capacity):
    n = len(profits)
    prof_per_weight = []
    for i in range(0,n):
        prof_per_weight.append(profits[i]/weights[i])
    indices = sorted(range(len(prof_per_weight)),reverse=True, key=prof_per_weight.__getitem__)
    i = 0
    totalProfit = 0
    while (i<=n and weights[indices[i]] <= capacity):
        capacity = capacity - weights[indices[i]]
        totalProfit = totalProfit + profits[indices[i]]
        i = i+1

    if(capacity < weights[indices[i]]):
        totalProfit = totalProfit + ((capacity/weights[indices[i]])*profits[indices[i]])

    print("Total profit is: ",totalProfit)


#driver code
prof = [25,24,15]
wt = [18,15,10]
capacity = 20
frac_knapSack(prof,wt,capacity)