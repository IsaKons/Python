# we have travel DAYS and cost of 1 day ticket = 2, 7 day = 7 and 30 day = 15. 
# Find cheapest way
days = [1,4,6,7,8,20], 
costs = [2,7,15]
dp = [0]*(days[-1]+1)
for i in range(1,len(dp)):        
    if i in days:
        dp[i] = min(dp[max(i-1,0)]+costs[0],dp[max(i-7,0)]+costs[1],dp[max(i-30,0)]+costs[2])
    else:
        dp[i]=dp[i-1]
print(dp[-1])