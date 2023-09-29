def check_dup(s):
    s = s.upper()
    li = list(s)
    di = {}
    for i in li:
        try:
            if di[i]:
                di[i] += 1
        except:
            di[i] = 1

    count = 0
    for i in di:
        if di[i] > 1:
            count += 1
    return count


# testcase
print(check_dup('abcd'))
print(check_dup('aabbcde'))
print(check_dup('aabBcde'))
print(check_dup('indivisibility'))
print(check_dup('indivisibilities'))
print(check_dup('aA11'))
print(check_dup('ABBA'))
