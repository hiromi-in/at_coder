"""
問題文
高橋君はデータの加工が行いたいです。

整数 
a,b,cと、文字列 
s が与えられます。 
a+b+c の計算結果と、文字列 
s を並べて表示しなさい。

制約
1≤a,b,c≤1,000
1≤
∣s∣
≤100
"""

a = int(input())

bc = input().split()
b = int(bc[0])
c = int(bc[1])

s = input()

print(str(a+b+c) + " " + s)
