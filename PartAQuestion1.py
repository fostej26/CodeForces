def alternatingSum(t, test_cases):
    results = []

    for case in test_cases:
        n, sequence = case
        sum = 0

        for i in range(n):
            if i % 2 == 0:
                sum += sequence[i]
            else:
                sum -= sequence[i]
        results.append(sum)
    
    for result in results:
        print(result)


t = int(input())
test_cases = []
for i in range(t):
    n = int(input())
    sequence = list(map(int, input().split()))
    test_cases.append((n, sequence))

alternatingSum(t, test_cases)