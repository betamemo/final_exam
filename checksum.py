def cal_checksum(payload):
    li = list(payload)
    n = len(li)
    digits = []

    for i in range(n):
        tmp = int(li[i])

        if n % 2 == 0:  # if length is even, the multipliers start with 1
            if i % 2 != 0:
                tmp *= 2
        else:  # if length is odd, the multipliers start with 2
            if i % 2 == 0:
                tmp *= 2

        # if the digits of result are more than 1
        if tmp > 10:
            tmp -= 9

        digits.append(tmp)

    sum_digits = sum(digits)

    return (10 - (sum_digits % 10)) % 10


# testcase 1
payload = '62'
print('checksum of', payload, 'is', cal_checksum(payload))

# testcase 2
payload = '250219941'
print('checksum of', payload, 'is', cal_checksum(payload))

# testcase 3
payload = '7992739871'
print('checksum of', payload, 'is', cal_checksum(payload))
