def calculate(s):

    path = ['']
    result = 0
    pathlen = 0

    for line in s.split('\n'):
        level = 0
        while level < len(line) and line[level] == ' ':
            level += 1

        while level < len(path) - 1:
            pathlen -= len(path.pop())

        if '.' not in line:
            path.append(line.strip())
            pathlen += len(path[-1])
        else:
            if line.endswith('.jpeg') or line.endswith('.gif') or line.endswith('.png'):
                result += pathlen + max(len(path) - 1, 1) + len(line.strip())

    return result

a = open('data').read()
print calculate(a)
