"""
問題文
E869120 は 
1 円硬貨を 
A 枚と 
500 円硬貨を無限枚持っています.
これらの硬貨だけを使うことによって, ちょうど 
N 円を支払うことができるかを判定しなさい.

制約
N は 
1 以上 
10000 以下の整数
A は 
0 以上 
1000 以下の整数
"""

n = int(input())
a = int(input())

remaining = n % 500
test_list = []

for i in range(0, a+1):
  test_list.append(i)

print("Yes" if remaining in test_list else "No")
