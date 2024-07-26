def lcs(A,B):
    len1 = len(A)
    len2 = len(B)
    Dp = [[0 for x in range(len2+1)] for x in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0 or j == 0:
                Dp[i][j] = 0
            elif A[i-1] == B[j-1]:
                Dp[i][j] = Dp[i-1][j-1]+1
            else:
                Dp[i][j] = max(Dp[i-1][j],Dp[i][j-1])
    l = ""
    i = len(A)
    j = len(B)
    while i>0 and j>0:
        if A[i-1] == B[j-1]:
            l =  A[i-1] + l 
            i -= 1
            j -= 1
        elif Dp[i-1][j]>Dp[i][j-1]:
            i -= 1
        else:    
            j -= 1  
     
    print("Longest common subsequence of "+A +" and " +B+  " is " + l )   
    return Dp[len1][len2]       
       
B = "abcde"
A = "ace"
lcs(A,B)