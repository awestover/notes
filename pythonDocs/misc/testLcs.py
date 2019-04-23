def lcs(S, T):
    L = [[0]*(len(T)+1) for x in range(len(S)+1)]
    longest = 0

    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] == T[j]:
                if i == 0 or j == 0:
                    L[i][j] = 1
                else:
                    L[i][j] = L[i-1][j-1] + 1

                if L[i][j] > longest:
                    longest = L[i][j]
            else:
                L[i][j] = 0
    return longest

import numpy as np

x = np.random.choice(["a", "b", "c"], size=(2,int(1e4)))
a = "".join(x[0])
b = "".join(x[1])
print(a)
print(b)
print(lcs(a,b))

