def find_middle(s):
    n = len(s)
    middle = int(n / 2)

    if n % 2 == 0:  # even
        start = middle - 1
        end = middle + 1
        return s[start:end]
    else:
        return s[middle]


# testcase
print(find_middle('test'))
print(find_middle('testing'))
print(find_middle('middle'))
