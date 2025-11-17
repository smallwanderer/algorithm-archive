def solution(triangle):
    dp =[0]
    
    for layer_idx in range(len(triangle)):
        temp = [0] * (len(triangle[layer_idx])+1)
        for idx in range(len(triangle[layer_idx])):
            temp[idx] = max(temp[idx], triangle[layer_idx][idx] + dp[idx])
            temp[idx+1] = max(temp[idx+1], triangle[layer_idx][idx] + dp[idx])
        dp = temp[:]
    return max(dp)
            