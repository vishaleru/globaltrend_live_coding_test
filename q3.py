def knapsack(values, weight,capacity):
    len1 = len(values)
    dp = [[0 for x in range(capacity+1)] for x in range(len1+1)]
    for i in range(len1+1):
        for w in range(capacity+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weight[i-1]<=capacity:
                dp[i][w] = max(values[i-1]+dp[i-1][w-weight[i-1]],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    return dp[len1][capacity]            
                    
values = [10,15,40]
weight = [1,2,3]
capacity = 5
print(f"Maximum value in Knapsack = {knapsack(values,weight,capacity)}")