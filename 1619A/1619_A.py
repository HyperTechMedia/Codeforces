# https://codeforces.com/problemset/problem/1619/A

def SquareString(s):
    if len(s) % 2 == 0 and s[0:len(s)//2] == s[len(s)//2:len(s)]:
        return "YES"
    return "NO"

n = int(input())
for _ in range(n):
    print(SquareString(input()))
