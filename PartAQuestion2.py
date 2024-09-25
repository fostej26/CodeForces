#https://codeforces.com/problemset/problem/10/A

def power_consumption(n, p1, p2, p3, t1, t2, interval_list):
    total = 0
    previous_end = interval_list[0][0]
 
    for i in range(n):
        start, end = interval_list[i]
        total += (end - start) * p1
 
        if i > 0:
            idle_time = start - previous_end
            if idle_time <= t1:
                total += idle_time * p1
            elif idle_time <= t1 + t2:
                total += t1 * p1 + (idle_time - t1) * p2
            else:
                total += t1 * p1 + t2 * p2 + (idle_time - t1 - t2) * p3
        
        previous_end = end
 
    return total
 
n, p1, p2, p3, t1, t2 = map(int, input().split())
interval_list = [list(map(int, input().split())) for _ in range(n)]
print(power_consumption(n, p1, p2, p3, t1, t2, interval_list))