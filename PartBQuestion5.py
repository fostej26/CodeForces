#https://codeforces.com/problemset/problem/2010/C1

def messageError(string):
    
    n = len(string)
    for i in range((n // 2) + 1, n):
        check1 = string[:i]
        check2 = string[-i:]
        if check1 == check2:
            print("YES")
            print(check1)
            return
    print("NO")

string = input().strip()
messageError(string)