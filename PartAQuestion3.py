def increasingSequence(n, d, sequence):
    moves = 0
    for i in range(1, n):
        if sequence[i] <= sequence[i - 1]:
            required = (sequence[i - 1] - sequence[i]) // d + 1
            sequence[i] += required * d
            moves += required
    return moves

n, d = map(int, input().split())
sequence = list(map(int, input().split()))

print(increasingSequence(n, d, sequence))