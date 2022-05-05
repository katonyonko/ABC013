import io
import sys

_INPUT = """\
6
4 5
100 4 60 1 4
10 1
5000 2 2000 1 300
9 23
170 8 120 5 12
653 314159
6728 123456 5141 41928 222222
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,H=map(int,input().split())
  A,B,C,D,E=map(int,input().split())
  ans=10**100
  tmp=E*N-H+1
  for i in range(N+1):
    c=max(0,(tmp-(E+B)*i-1)//(E+D)+1)
    ans=min(ans,A*i+C*c)
  print(ans)