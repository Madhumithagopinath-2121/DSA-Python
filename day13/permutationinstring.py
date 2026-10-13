
def checkInclusion(s1, s2):
    m = len(s1)
    n = len(s2)

    if m > n:
        return False

    pattern = {}
    window = {}

    for i in range(m):
        if s1[i] in pattern:
            pattern[s1[i]] += 1
        else:
            pattern[s1[i]] = 1

        if s2[i] in window:
            window[s2[i]] += 1
        else:
            window[s2[i]] = 1

    if window == pattern:
        return True

    for i in range(m, n):
        incoming = s2[i]

        if incoming in window:
            window[incoming] += 1
        else:
            window[incoming] = 1

        outgoing = s2[i - m]
        window[outgoing] -= 1

        if window[outgoing] == 0:
            del window[outgoing]

        if window == pattern:
            return True

    return False


s1 = input().strip()
s2 = input().strip()

print(checkInclusion(s1, s2))
