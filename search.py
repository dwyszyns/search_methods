import timeit


# naive algorythm
def nfind(pattern, text):
    naive_position = []
    if pattern and text:
        for n in range(0, len(text) - len(pattern) + 1):
            m = 0
            while m < len(pattern) and text[n + m] == pattern[m]:
                m += 1
                if m == len(pattern):
                    naive_position.append(n)
    if pattern == text == "":
        return [0]
    return naive_position


# prefix table
def lps(string):
    lps_array = [0] * len(string)
    i = 0
    j = 1
    while j < len(string):
        if string[i] == string[j]:
            lps_array[j] = i + 1
            i += 1
            j += 1
        elif i != 0:
            i = lps_array[i - 1]
        else:
            j += 1
    return lps_array


# KMP algorythm
def kmpfind(pattern, text):
    kmp_position = []
    if pattern and text:
        prefix = lps(pattern)
        n = 0
        m = 0
        while n < len(text):
            if text[n] == pattern[m]:
                n += 1
                m += 1
            elif m != 0:
                m = prefix[m - 1]
            else:
                n += 1
            if m == len(pattern):
                kmp_position.append(n - m)
                m = prefix[m - 1]
    if pattern == text == "":
        return [0]
    return kmp_position


def karp_rabin_search(pattern, text):
    results = []
    pattern_len = len(pattern)
    text_len = len(text)

    if pattern == text == "":
        return [0]
    if pattern and text and len(text) >= len(pattern):
        p_value = sum(ord(char) for char in pattern)
        t_value = sum(ord(char) for char in text[:pattern_len])

        for i in range(text_len - pattern_len + 1):
            if p_value == t_value:
                if pattern == text[i:i + pattern_len]:
                    results.append(i)

            if i < text_len - pattern_len:
                t_value = t_value - ord(text[i]) + ord(text[i + pattern_len])

        return results
    return results


def Rabin_Karp_Matcher(pattern, text):
    d = 257
    q = 7919
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q
    p = 0
    t = 0
    result = []
    if pattern and text and len(text) >= len(pattern):
        for i in range(m):  # preprocessing
            p = (d*p+ord(pattern[i])) % q
            t = (d*t+ord(text[i])) % q
        for s in range(n-m+1):
            if p == t:
                match = True
                for i in range(m):
                    if pattern[i] != text[s+i]:
                        match = False
                        break
                if match:
                    result = result + [s]
            if s < n-m:
                t = (t-h*ord(text[s])) % q  # remove letter s
                t = (t*d+ord(text[s+m])) % q  # add letter s+m
                t = (t+q) % q  # make sure that t >= 0
    if pattern == text == "":
        return [0]
    return result


def KR_find(pattern, text):
    results = []
    pattern_len = len(pattern)
    text_len = len(text)
    d = 256
    q = 10001
    hash_max = 1
    for i in range(pattern_len-1):
        hash_max = (hash_max * d) % q

    p_hash = 0
    t_hash = 0
    if pattern and text and len(text) >= len(pattern):
        for i in range(pattern_len):
            p_hash = (d * p_hash + ord(pattern[i])) % q
            t_hash = (d * t_hash + ord(text[i])) % q
        for i in range(text_len - pattern_len + 1):
            if t_hash == p_hash:
                if pattern == text[i:i + pattern_len]:
                    results.append(i)

            if i < text_len-pattern_len:
                t_hash -= ord(text[i]) * hash_max
                t_hash = d * t_hash + ord(text[i + pattern_len])
                t_hash %= q
    if pattern == text == "":
        return [0]
    return results


# Test data
pattern = "example"
text = "This is an example text for example pattern matching. Let's find the word 'example'."

# Benchmarking the algorithms
nfind_time = timeit.timeit(lambda: nfind(pattern, text), number=10000)
kmpfind_time = timeit.timeit(lambda: kmpfind(pattern, text), number=10000)
KR_time = timeit.timeit(lambda: karp_rabin_search(pattern, text), number=10000)
print(f'Naive: {nfind_time}, KMP: {kmpfind_time}, KR: {KR_time}')
