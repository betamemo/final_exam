def rec_sum(li):
    n = len(li)
    if n == 0:
        return 0
    elif n == 1:
        return li[0]
    else:
        tmp = li[0] + li[1]
        li[1] = tmp
        del (li[0])
        return rec_sum(li)


# testcase
print(rec_sum([1, 2, 5]))
