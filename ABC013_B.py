import io
import sys

_INPUT = """\
6
4
6
6
4
8
1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  a=int(input())
  b=int(input())
  print(min((a-b)%10,10-(a-b)%10))