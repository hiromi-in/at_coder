"""
整数 
A, 
B があります。

A+B, 
 A−B, 
 A×B の中で最大の数を出力してください。

制約
入力は全て整数である。
−100≤A, B≤100
"""

a, b = map(int, input().split())
calc_list = [a+b, a-b, a*b]
print(max(calc_list))
