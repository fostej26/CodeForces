#https://codeforces.com/problemset/problem/12/B

def correctSolution(alice, bob):
    alice.sort()
    index = 1
    if alice[0] == "0":
        while alice[0] == "0" and index < len(alice):
            alice[0], alice[index] = alice[index], alice[0]
            index += 1
    if alice == bob:
        print("OK")
    else:
        print("WRONG_ANSWER")

alice = [char for char in input()]
bob = [char for char in input()]

correctSolution(alice, bob)