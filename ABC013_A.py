import io
import sys

_INPUT = """\
6
A
B
C
D
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  print(ord(input())-ord('A')+1)