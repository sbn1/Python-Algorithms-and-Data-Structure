# -*- coding: utf-8 -*-
"""
Given a value N, if we want to make change for N cents, and we 
have infinite supply of each of S = { S1, S2, .. , Sm} valued coins,
 how many ways can we make the change? The order of coins doesn’t
 matter. For example, for N = 4 and S = {1,2,3}, there are four 
 solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
 
"""

def coins(n,s):
    
    m = len(s)
    # initialization of the empty matrix
    dynamic_matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if j==0:                                                    
              dynamic_matrix[i][j] = 1
            
            elif i==0:                                                
              dynamic_matrix[i][j] = 0
                
            else:
                if s[i-1] <= j:
                    dynamic_matrix[i][j] = dynamic_matrix[i][j-s[i-1]]+dynamic_matrix[i-1][j]
                else:
                    dynamic_matrix[i][j] = dynamic_matrix[i-1][j]
    return dynamic_matrix[m][n]
    
    



n = 4
s = [1,2,3]
print(coins(n,s))