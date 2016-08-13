def remove(number):

    if number < 10:
        return number

    a = list(str(number))

    for i in xrange(len(a) - 2):
        if a[i] >= a[i + 1] > a[i + 2]:
            return int(''.join(a[:i + 1] + a[i + 2:]))

    r = ''.join(a[:-2]) + (a[-1] if a[-1] > a[-2] else a[-2])
    return int(r)


def remove1(number):
    result = float('inf')
    a = list(str(number))

    for i in xrange(len(a) - 1):
        if a[i] > a[i + 1]:
            t = a[:i + 1] + a[i + 2:]
        else:
            t = a[:i] + a[i + 1:]

        t = int(''.join(t))
        if t < result:
            result = t
    return result


a = 9998928898989823423
print remove(a)
print remove1(a)

