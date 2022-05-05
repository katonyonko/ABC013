import io
import sys

_INPUT = """\
6
5 7 1
1 4 3 4 2 3 1
5 7 2
1 4 3 4 2 3 1
10 20 300
9 1 2 5 8 1 9 3 5 6 4 5 4 6 8 3 2 7 9 6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M,D=map(int,input().split())
  A=list(map(int,input().split()))
  d=[i for i in range(N)]
  for i in reversed(range(M)):
    d[A[i]-1],d[A[i]]=d[A[i]],d[A[i]-1]
  doubling=[[d[i]] for i in range(N)]
  for i in range(30):
    for j in range(N):
      doubling[j].append(doubling[doubling[j][i]][i])
  D=[i for i in range(31) if (D>>i)&1==1]
  for k in range(N):
    ans=k
    for d in D:
      ans=doubling[ans][d]
    print(ans+1)