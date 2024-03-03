for i in range(int(input())):
    n = int(input())
    s = input().strip()
    mp = {0: 1}
    total = 0
    sum_val = 0
    for i in range(n):
        sum_val += int(s[i]) - 1
        total += mp.get(sum_val, 0)
        mp[sum_val] = mp.get(sum_val, 0) + 1

    print(total)