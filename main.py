import numpy as np

n=4
m=4
hospital = np.random.randint(2, size=(m+1, n+1))
path = np.zeros((m+1, n+1), dtype=int)



coord1=[1, 0, -1, 0]
coord2=[0, 1, 0, -1]


def valid(ii, jj):
    print("abc")
    if ii<0 or ii>m-1 or jj<0 or jj>n-1: return False
    print("def")
    return True

def backtracking(i, j, pas):
    for k in range(4):
        ii=i+coord1[k]
        jj=j+coord2[k]

        if valid(ii, jj) is True:
            path[ii][jj] = pas+1
            if ii==0 or ii==m-2 or jj==0 or jj==n-2: show()
            backtracking(ii, jj, pas+1)
        path[ii][jj]=0


def show():
    for i in range(m):
        for j in range(n):
            print(path[i][j], end=' ')

        print('\n')
    print('\n')


for i in range(m):
    for j in range(n):
        print(hospital[i][j], end=' ')
    print('\n')

print('\n')

path[0][0]=1
backtracking(2,1,1)