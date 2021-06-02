def catalan(n):
    if(n==0 or n==1):
        return 1
    catNums = [0]*(n+1)
    catNums[0] = 1
    catNums[1] = 1
    for i in range(2,n+1):
        for j in range(0,i):
            catNums[i] += catNums[j]*catNums[i-j-1]
    return catNums[n]

#driver code:
val = catalan(10)
print("The 10th Catalan Number is: ",val)