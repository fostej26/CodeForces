#https://codeforces.com/problemset/gymProblem/102697/187

def mountainBiking(n, elevationList):
    incline = 0
    max_incline = 0
    for index in range(1, n):
        if elevationList[index] > elevationList[index - 1]:
            incline += elevationList[index] - elevationList[index - 1]
        else:
            if incline > max_incline:
                max_incline = incline
            incline = 0
    if incline > max_incline:
        max_incline = incline
    return max_incline

n = int(input())
elevationList = list(map(int, input().split()))
print(mountainBiking(n, elevationList))