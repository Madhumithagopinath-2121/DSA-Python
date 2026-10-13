
def findAnagrams(s, p):
    result = []
    n = len(s)
    m = len(p)

    if m > n:
        return result

    pattern = {}
    window = {}

    for i in range(m):
        if p[i] in pattern:
            pattern[p[i]] += 1
        else:
            pattern[p[i]] = 1

        if s[i] in window:
            window[s[i]] += 1
        else:
            window[s[i]] = 1

    if window == pattern:
        result.append(0)

    for i in range(m, n):
        incoming = s[i]

        if incoming in window:
            window[incoming] += 1
        else:
            window[incoming] = 1

        outgoing = s[i - m]
        window[outgoing] -= 1

        if window[outgoing] == 0:
            del window[outgoing]

        if window == pattern:
            result.append(i - m + 1)

    return result


s = input().strip()
p = input().strip()

print(findAnagrams(s, p))
